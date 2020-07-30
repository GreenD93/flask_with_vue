import sys
import numpy as np

#from new_color_table import *
from procs.color_table import *

def calc_dist_c(r1, g1, b1, r2, g2, b2):
    rmean = int((r1 + r2) / 2)
    r = r1 - r2
    g = g1 - g2
    b = b1 - b2

    weightR = 2 + rmean / 256
    weightG = 4.0
    weightB = 2 + (255 - rmean) / 256
    dist = (weightR * r * r + weightG * g * g + weightB * b * b)
    return dist


def min_distance_rgb_c(r1, g1, b1):
    min_dist = sys.maxsize
    ret_rgb = RGB_TABLE[0]

    for rgb in RGB_TABLE:
        r2, g2, b2 = rgb

        dist = calc_dist_c(r1, g1, b1, r2, g2, b2)

        if dist < min_dist:
            ret_rgb = rgb
            min_dist = dist

    return ret_rgb


def distance_c(img):
    new_img = img.copy()

    # get dominant_color
    dominant_color = np.unique(new_img.reshape(-1, 3), axis=0)

    # dominant_color to close color for 18 colors
    for color in dominant_color:

        is_bg_color = np.array_equal(color, np.array(BG_COLOR))

        if not is_bg_color:
            b, g, r = color

            close_color = min_distance_rgb_c(r, g, b)

            indices = np.where((new_img == color).all(axis=2))
            new_img[indices] = close_color[::-1]

    return new_img
