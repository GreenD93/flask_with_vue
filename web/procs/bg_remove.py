import numpy as np
import cv2

RESIZE_WIDTH = 100
RESIZE_HEIGHT = 100

class BgRemover():
    '''
        remove the background using grabcut and then change bg color to magenta color for valid pixel(fg)
        mask shape is in grabcut.ipynb file
    '''
    def __init__(self):
        
        self.mask = self._make_mask()
        # magenta color
        self.bg_color = [255,0,255]
    
    def _make_mask(self):
        
        mask = np.full((RESIZE_WIDTH,RESIZE_HEIGHT), 2 ,np.uint8)
        
        # assummtion : the shape of mask image is (100, 100)
        center_mask1 = np.full((20,40), 1, np.uint8)
        center_mask2 = np.full((40,20), 1, np.uint8)

        mask[40:60, 30:70] = center_mask1
        mask[30:70, 40:60] = center_mask2

        corner_mask = np.full((20,20), 0, np.uint8)

        mask[0:20, 0:20] = corner_mask
        mask[80:100, 80:100] = corner_mask
        mask[0:20, 80:100] = corner_mask
        mask[80:100, 0:20] = corner_mask
        
        return mask
        

    # https://docs.opencv.org/trunk/d8/d83/tutorial_py_grabcut.html
    def _grab_cut(self, img):
        
        #Grab Cut the object
        bgdModel = np.zeros((1,65), np.float64)
        fgdModel = np.zeros((1,65), np.float64)
        
        mask = self.mask.copy()

        cv2.grabCut(img, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)
        mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')

        img1 = img * mask[:,:,np.newaxis]

        #Get the background
        background = img - img1

        #Change all pixels in the background that are not black to magenta
        background[np.where((background > [0,0,0]).all(axis = 2))] = self.bg_color

        #Add the background and the img
        final_img = background + img1

        return final_img
    
    def _get_valid_pixel_cnt(self, img):
        
        total_pixel_cnt = img.shape[0] * img.shape[1]
        bg_pixel_cnt = len(np.where((img == [255,0,255]).all(axis = 2) )[0])

        valid_pixel_cnt = total_pixel_cnt - bg_pixel_cnt
        
        return valid_pixel_cnt
        

    def do(self, img):
        
        bg_removed_img = self._grab_cut(img)
        valid_pixel_cnt = self._get_valid_pixel_cnt(bg_removed_img)
        
        return bg_removed_img, valid_pixel_cnt

if __name__ == "__main__":
    remover = BgRemover()
    img = cv2.imread('sample/demo.jpg')
    img = cv2.resize(img, (RESIZE_WIDTH, RESIZE_HEIGHT))

    fg_img, valid_pixel_count = remover.do(img)
    cv2.imwrite('demo_fg.jpg', fg_img)
