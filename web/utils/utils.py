from urllib.request import urlopen
from PIL import Image
from io import BytesIO
import numpy as np

def load_img_from_url(url):
    resp = urlopen(url)

    im_src = Image.open(BytesIO(resp.read()))

    mode = im_src.mode
    if mode != 'RGB':
        im = im_src.convert('RGB')
    else:
        im = im_src

    img = np.array(im, dtype=np.uint8)

    return img, mode

#----------------------------------
# prod 이미지 경로
def make_wmp_deal_img_url(deal_id, cur_sec=-1, wide=False):

    #https://view01.wemep.co.kr/wmp-product/9/479/107174799/107174799.jpg?1534775126

    str_prod_id = str(deal_id)
    last_char = str_prod_id[-1:]
    mid_chars = str_prod_id[-4:-1]

    if not wide:
        img_url = 'https://view01.wemep.co.kr/wmp-deal/{0}/{1}/{2}/{2}.jpg?{3}'.format(
                        last_char,
                        mid_chars,
                        str_prod_id,
                        cur_sec
                    )
    else:
        img_url = 'https://view01.wemep.co.kr/wmp-deal/{0}/{1}/{2}/{2}_wide.jpg?{3}'.format(
                        last_char,
                        mid_chars,
                        str_prod_id,
                        cur_sec
                    )

    return img_url