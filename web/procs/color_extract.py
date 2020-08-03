import time
import numpy as np
import json
import cv2
import argparse

# sudo apt install python3-sklearn
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans

# legacy
# import color_extract_cython
# from old_bg_remove import BgRemover

# pure python
from procs.cal_color_dist import *

from procs.bg_remove import BgRemover

#from new_color_table import *
from procs.color_table import *

RESIZE_WIDTH = 100
RESIZE_HEIGHT = 100
N_DOMINANT_COLORS = 5

class ColorExtractor():
    '''
        get dominant color(18 colors) on image
    '''
    def __init__(self):

        self.rgb_table = RGB_TABLE
        self.color_match_dict = COLOR_MATCH_DICT
        # magenta color
        self.bg_color = BG_COLOR

        self.resize_width = RESIZE_WIDTH
        self.resize_height = RESIZE_HEIGHT
        self.n_colors = N_DOMINANT_COLORS

        self.bg_remover = BgRemover()

    # https://stackoverflow.com/a/48302220
    def _cluster_colors(self, img):
        arr = img.reshape((-1, 3))
        kmeans = KMeans(n_clusters=self.n_colors, random_state=42).fit(arr)
        labels = kmeans.labels_
        centroids = kmeans.cluster_centers_

        less_colors = centroids[labels].reshape(img.shape).astype('uint8')  # array label mapping
        print(centroids.astype('uint8'))

        # recovery [255,0,255]
        indices = np.where( (img == self.bg_color).all(axis = 2) )
        less_colors[indices] = self.bg_color

        return less_colors

    def _get_color_portion(self, img, min_count=0):

        portion_dict = {}

        ar =  img.reshape((-1,3))
        dominant_colors, counts = np.unique(ar, axis=0, return_counts=True)
        inds = np.where( counts>= min_count )[0]

        for i in inds:
            b, g, r = dominant_colors[i]

            is_bg_color = np.array_equal(dominant_colors[i], np.array(self.bg_color))

            if is_bg_color:
                continue

            color_str_key = '#' + '{:02x}'.format(r) +  '{:02x}'.format(g) +  '{:02x}'.format(b)
            portion_dict[color_str_key] = counts[i]

        # sorting values
        portion_dict = {k: v for k, v in sorted(portion_dict.items(), key=lambda item: item[1], reverse=True)}

        return portion_dict

    def _read_img(self, img_path):

        img = cv2.imread(img_path)
        img = cv2.resize(img, (self.resize_width, self.resize_height))

        return img

    def _get_simplified_img(self, img):

        img = self._cluster_colors(img)

        # legacy
        # simplified_img = color_extract_cython.distance_c(img, self.rgb_table)

        # pure python
        simplified_img = distance_c(img)

        return simplified_img

    def _convert_18_colors(self, portion_dict):

        # to 18 color, '#fffafa' => '#FFC5DB'
        match_dict = {}

        for key in portion_dict.keys():
            if key not in self.color_match_dict:
                continue

            match_color = self.color_match_dict[key]

            if match_color in match_dict:
                value = match_dict[match_color]
                value += portion_dict[key]
                match_dict[match_color] = value
            else:
                match_dict[match_color] = portion_dict[key]

        return match_dict

    def _make_json_string(self, match_dict, valid_pixel_count):

        json_list = []
        sorted_key = sorted(match_dict, key=lambda k : match_dict[k], reverse=True)

        whole_size = self.resize_width * self.resize_height

        for key in sorted_key:
            json_dict = dict()
            json_dict['rgb'] = key
            json_dict['in_foreground'] = '{0}%'.format(int((100.0 * match_dict[key] / valid_pixel_count)))
            json_dict['in_whole'] = '{0}%'.format(int((100.0 * match_dict[key] / whole_size)))
            json_list.append(json_dict)

        json_string = json.dumps(json_list, indent=4)

        return json_string

    def do(self, img):

        # img = self._read_img(img_path)
        # remove bg
        img = cv2.resize(img, (self.resize_width, self.resize_height), interpolation=cv2.INTER_AREA)
        fg_img, valid_pixel_count = self.bg_remover.do(img)

        cv2.imwrite('fg_img.jpg', fg_img)

        #fg_img = cv2.resize(fg_img, (20, 20), interpolation=cv2.INTER_AREA)

        # extract color
        simplified_img = self._get_simplified_img(fg_img)
        cv2.imwrite('simplified_img.jpg', simplified_img)

        portion_dict = self._get_color_portion(simplified_img)

        # pixel 테스트용
        print(portion_dict)

        match_dict = self._convert_18_colors(portion_dict)

        # make json string
        json_string = self._make_json_string(match_dict, valid_pixel_count)

        return json_string


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('img_path', type=str, help='input img path')

    args = parser.parse_args()
    img_path = args.img_path

    start = time.time()

    extractor = ColorExtractor()

    # json_string = extractor.do('sample/demo_shirt.jpg')
    json_string = extractor.do(img_path)

    end = time.time()
    print('process time : {0}'.format(end-start))
    print(json_string)

# output:
# [
#     {
#         "rgb": "#F1F223",
#         "in_foreground": "49%",
#         "in_whole": "23%"
#     },
#     {
#         "rgb": "#F4D424",
#         "in_foreground": "38%",
#         "in_whole": "18%"
#     },
#     {
#         "rgb": "#F4AA24",
#         "in_foreground": "11%",
#         "in_whole": "5%"
#     }
# ]
