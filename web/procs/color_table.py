BG_COLOR = [255, 0, 255]

###############################
# 18colors
###############################
# white(흰색) - #FFFFFF
# classic rose(분홍) - #FFC5DB
# turbo(노랑) - #F4D424
# lighting yellow(주황) - #F4AA24
# lemon(골드) - #F1F223
# scarlet(빨강) - #EC1818
# silver(실버) - #C6C6C6
# violet(자주색) - #AF1FA3
# inchworm(연두) - #A5DD0C
# cornflower(하늘) - #99D1EA
# chelsea gem(갈색) - #90572F
# grey(회색) - #8B8B8B
# dark violet(보라색) - #8316C0
# olive(카키색) - #71842F
# green(초록) - #37B400
# blue(파랑) - #3131FD
# nero(검정) - #202020
# midnight blue(남색) - #1C2C85
###############################

RGB_TABLE = [
    # white - #FFFFFF
    [255, 250, 250],
    [248, 248, 255],
    [255, 255, 255],
    [245, 245, 245],
    [220, 220, 220],
    [240, 255, 255],
    [240, 248, 255],
    [224, 255, 255],
    [238, 233, 233],
    [224, 238, 238],
    [209, 209, 209],
    [212, 212, 212],
    [214, 214, 214],
    [217, 217, 217],
    [219, 219, 219],
    [222, 222, 222],
    [224, 224, 224],
    [227, 227, 227],
    [229, 229, 229],
    [235, 235, 235],
    [237, 237, 237],
    [240, 240, 240],
    [242, 242, 242],
    [247, 247, 247],
    [250, 250, 250],
    [252, 252, 252],
    [238, 229, 222],

    # classic rose - #FFC5DB
    [255, 240, 245],
    [255, 228, 225],
    [255, 20, 147],
    [219, 112, 147],
    [240, 128, 128],
    [255, 105, 180],
    [255, 192, 203],
    [255, 182, 193],
    [221, 160, 221],
    [216, 191, 216],
    [238, 224, 229],
    [205, 193, 197],
    [238, 213, 210],
    [205, 183, 181],
    [255, 193, 193],
    [238, 180, 180],
    [205, 155, 155],
    [238, 106, 167],
    [205, 96, 144],
    [255, 181, 197],
    [238, 169, 184],
    [205, 145, 158],
    [255, 174, 185],
    [238, 162, 173],
    [205, 140, 149],
    [255, 130, 171],
    [238, 121, 159],
    [238, 0, 238],
    [255, 131, 250],
    [238, 122, 233],
    [255, 187, 255],
    [238, 174, 238],
    [255, 225, 255],
    [238, 210, 238],
    [205, 181, 205],
    [203, 185, 182],
    [220, 196, 191],
    [191, 144, 139],
    [255, 110, 180],
    [223, 204, 216],

    # turbo - #F4D424
    [255, 250, 240],
    [253, 245, 230],
    [255, 228, 196],
    [255, 218, 185],
    [255, 222, 173],
    [255, 228, 181],
    [255, 245, 238],
    [189, 183, 107],
    [238, 221, 130],
    [222, 184, 135],
    [245, 222, 179],
    [210, 180, 140],
    [255, 239, 219],
    [238, 223, 204],
    [205, 192, 176],
    [238, 213, 183],
    [205, 183, 158],
    [238, 203, 173],
    [238, 207, 161],
    [205, 201, 165],
    [205, 200, 177],
    [205, 198, 115],
    [238, 220, 130],
    [205, 190, 112],
    [205, 205, 180],
    [238, 201, 0],
    [205, 173, 0],
    [255, 211, 155],
    [238, 197, 145],
    [205, 170, 125],
    [255, 231, 186],
    [238, 216, 174],
    [205, 186, 150],

    # lighting yellow - #F4AA24
    [250, 240, 230],
    [250, 235, 215],
    [255, 239, 213],
    [255, 235, 205],
    [218, 165, 32],
    [205, 133, 63],
    [244, 164, 96],
    [210, 105, 30],
    [233, 150, 122],
    [255, 160, 122],
    [255, 140, 0],
    [255, 127, 80],
    [255, 99, 71],
    [238, 229, 222],
    [255, 193, 37],
    [238, 180, 34],
    [205, 155, 29],
    [255, 185, 15],
    [238, 173, 14],
    [205, 149, 12],
    [255, 130, 71],
    [238, 121, 66],
    [205, 104, 57],
    [255, 165, 79],
    [238, 154, 73],
    [255, 127, 36],
    [238, 118, 33],
    [205, 102, 29],
    [255, 140, 105],
    [238, 130, 98],
    [238, 149, 114],
    [255, 165, 0],
    [238, 154, 0],
    [205, 133, 0],
    [255, 127, 0],
    [238, 118, 0],
    [205, 102, 0],
    [255, 114, 86],
    [238, 106, 80],

    # lemon - #F1F223
    [255, 248, 220],
    [255, 255, 240],
    [255, 250, 205],
    [255, 255, 0],
    [240, 230, 140],
    [238, 232, 170],
    [250, 250, 210],
    [255, 255, 224],
    [255, 215, 0],
    [245, 245, 220],
    [238, 233, 191],
    [238, 232, 205],
    [238, 238, 224],
    [255, 246, 143],
    [238, 230, 133],
    [255, 236, 139],
    [238, 238, 209],
    [238, 238, 0],
    [205, 205, 0],

    # scarlet - #EC1818
    [205, 92, 92],
    [178, 34, 34],
    [165, 42, 42],
    [250, 128, 114],
    [255, 69, 0],
    [255, 0, 0],
    [255, 106, 106],
    [238, 99, 99],
    [205, 85, 85],
    [255, 48, 48],
    [238, 44, 44],
    [205, 38, 38],
    [255, 64, 64],
    [238, 59, 59],
    [205, 51, 51],
    [205, 55, 0],
    [238, 0, 0],
    [205, 0, 0],
    [215, 7, 81],
    [205, 79, 57],
    [238, 64, 0],
    [238, 92, 66],
    [205, 91, 69],
    [139, 35, 35],
    [198, 27, 48],
    [176, 48, 96],

    # silver - #C6C6C6
    [190, 190, 190],
    [211, 211, 211],
    [205, 201, 201],
    [205, 197, 191],
    [205, 205, 193],
    [161, 161, 161],
    [163, 163, 163],
    [166, 166, 166],
    [168, 168, 168],
    [171, 171, 171],
    [173, 173, 173],
    [176, 176, 176],
    [179, 179, 179],
    [181, 181, 181],
    [184, 184, 184],
    [186, 186, 186],
    [189, 189, 189],
    [191, 191, 191],
    [194, 194, 194],
    [196, 196, 196],
    [199, 199, 199],
    [201, 201, 201],
    [204, 204, 204],
    [207, 207, 207],
    [232, 232, 232],

    # violet - #AF1FA3
    [199, 21, 133],
    [238, 130, 238],
    [208, 32, 144],
    [218, 112, 214],
    [238, 18, 137],
    [205, 16, 118],
    [139, 10, 80],
    [139, 58, 98],
    [139, 99, 108],
    [139, 95, 101],
    [205, 104, 137],
    [139, 71, 93],
    [255, 52, 179],
    [238, 48, 167],
    [205, 41, 144],
    [139, 28, 98],
    [255, 62, 150],
    [238, 58, 140],
    [205, 50, 120],
    [139, 34, 82],
    [205, 0, 205],
    [139, 0, 139],
    [205, 105, 201],
    [139, 71, 137],
    [224, 102, 255],
    [209, 95, 238],
    [166, 54, 105],
    [121, 71, 100],
    [120, 94, 107],
    [167, 147, 185],
    [213, 198, 233],
    [174, 174, 228],
    [191, 167, 182],

    # inchworm - #A5DD0C
    [240, 255, 240],
    [245, 255, 250],
    [144, 238, 144],
    [102, 205, 170],
    [127, 255, 212],
    [152, 251, 152],
    [0, 255, 127],
    [124, 252, 0],
    [173, 255, 47],
    [127, 255, 0],
    [0, 250, 154],
    [154, 205, 50],
    [224, 238, 224],
    [193, 205, 193],
    [118, 238, 198],
    [193, 255, 193],
    [180, 238, 180],
    [155, 205, 155],
    [84, 255, 159],
    [78, 238, 148],
    [154, 255, 154],
    [124, 205, 124],
    [0, 238, 118],
    [0, 205, 102],
    [0, 255, 0],
    [0, 238, 0],
    [0, 205, 0],
    [118, 238, 0],
    [102, 205, 0],
    [192, 255, 62],
    [179, 238, 58],
    [202, 255, 112],
    [188, 238, 104],
    [162, 205, 90],


    # cornflower - #99D1EA
    [0, 191, 255],
    [135, 206, 235],
    [135, 206, 250],
    [176, 196, 222],
    [173, 216, 230],
    [176, 224, 230],
    [175, 238, 238],
    [0, 206, 209],
    [72, 209, 204],
    [64, 224, 208],
    [0, 255, 255],
    [193, 205, 205],
    [99, 184, 255],
    [92, 172, 238],
    [0, 178, 238],
    [0, 154, 205],
    [135, 206, 255],
    [126, 192, 238],
    [108, 166, 205],
    [176, 226, 255],
    [164, 211, 238],
    [141, 182, 205],
    [198, 226, 255],
    [185, 211, 238],
    [159, 182, 205],
    [202, 225, 255],
    [188, 210, 238],
    [162, 181, 205],
    [191, 239, 255],
    [178, 223, 238],
    [154, 192, 205],
    [209, 238, 238],
    [180, 205, 205],
    [187, 255, 255],
    [174, 238, 238],
    [150, 205, 205],
    [152, 245, 255],
    [142, 229, 238],
    [122, 197, 205],
    [0, 245, 255],
    [0, 229, 238],
    [0, 197, 205],
    [0, 238, 238],
    [0, 205, 205],
    [0, 139, 139],
    [151, 255, 255],
    [141, 238, 238],
    [121, 205, 205],
    [135, 153, 166],
    [183, 197, 202],
    [132, 171, 212],
    [199, 234, 229],
    [175, 213, 207],
    [188, 197, 208],
    [178, 187, 205],
    [133, 139, 155],
    [206, 210, 226],
    [153, 170, 176],
    [217, 225, 240],
    [189, 199, 220],

    # chelsea gem - #90572F
    [139, 0, 0],
    [184, 134, 11],
    [188, 143, 143],
    [139, 69, 19],
    [160, 82, 45],
    [139, 131, 120],
    [139, 125, 107],
    [205, 175, 149],
    [139, 119, 101],
    [205, 179, 139],
    [139, 121, 94],
    [139, 137, 112],
    [139, 136, 120],
    [139, 129, 76],
    [139, 117, 0],
    [139, 105, 20],
    [139, 101, 8],
    [139, 105, 105],
    [139, 58, 58],
    [139, 71, 38],
    [139, 115, 85],
    [139, 126, 102],
    [139, 90, 43],
    [139, 26, 26],
    [139, 76, 57],
    [205, 129, 98],
    [139, 87, 66],
    [139, 90, 0],
    [139, 69, 0],
    [139, 62, 47],
    [139, 54, 38],
    [139, 37, 0],
    [146, 93, 68],
    [146, 97, 103],
    [105, 6, 49],
    [116, 68, 38],
    [84, 44, 19],
    [89, 68, 53],
    [148, 111, 86],
    [150, 95, 96],
    [152, 130, 117],
    [170, 153, 148],
    [175, 163, 134],
    [198, 177, 166],
    [154, 139, 124],
    [201, 166, 157],
    [205, 112, 84],
    [180, 134, 126],

    # grey - #8B8B8B
    [105, 105, 105],
    [139, 137, 137],
    [139, 134, 130],
    [139, 139, 131],
    [131, 139, 131],
    [139, 131, 134],
    [139, 125, 123],
    [131, 139, 139],
    [139, 139, 122],
    [139, 123, 139],
    [77, 77, 77],
    [79, 79, 79],
    [82, 82, 82],
    [84, 84, 84],
    [87, 87, 87],
    [89, 89, 89],
    [92, 92, 92],
    [94, 94, 94],
    [97, 97, 97],
    [99, 99, 99],
    [102, 102, 102],
    [107, 107, 107],
    [110, 110, 110],
    [112, 112, 112],
    [115, 115, 115],
    [117, 117, 117],
    [120, 120, 120],
    [122, 122, 122],
    [125, 125, 125],
    [127, 127, 127],
    [130, 130, 130],
    [133, 133, 133],
    [135, 135, 135],
    [138, 138, 138],
    [140, 140, 140],
    [143, 143, 143],
    [145, 145, 145],
    [148, 148, 148],
    [150, 150, 150],
    [153, 153, 153],
    [156, 156, 156],
    [158, 158, 158],
    [169, 169, 169],

    # dark violet - #8316C0
    [106, 90, 205],
    [147, 112, 219],
    [123, 104, 238],
    [132, 112, 255],
    [138, 43, 226],
    [186, 85, 211],
    [153, 50, 204],
    [148, 0, 211],
    [160, 32, 240],
    [131, 111, 255],
    [122, 103, 238],
    [105, 89, 205],
    [205, 150, 205],
    [139, 102, 139],
    [180, 82, 205],
    [122, 55, 139],
    [191, 62, 255],
    [178, 58, 238],
    [154, 50, 205],
    [104, 34, 139],
    [155, 48, 255],
    [145, 44, 238],
    [125, 38, 205],
    [85, 26, 139],
    [171, 130, 255],
    [159, 121, 238],
    [137, 104, 205],
    [93, 71, 139],
    [201, 204, 245],
    [81, 42, 66],
    [139, 131, 175],
    [125, 103, 133],
    [154, 139, 154],

    # olive - #71842F
    [128, 128, 0],
    [85, 107, 47],
    [143, 188, 143],
    [107, 142, 35],
    [105, 139, 105],
    [105, 139, 34],
    [110, 139, 61],
    [139, 134, 78],
    [139, 139, 0],
    [137, 130, 92],
    [127, 133, 100],
    [144, 160, 153],
    [87, 99, 93],
    [55, 62, 57],
    [113, 128, 121],
    [93, 90, 76],
    [146, 149, 143],
    [102, 122, 91],
    [150, 153, 147],
    [53, 67, 43],

    # green - #37B400
    [0, 100, 0],
    [46, 139, 87],
    [60, 179, 113],
    [32, 178, 170],
    [50, 205, 50],
    [34, 139, 34],
    [102, 139, 139],
    [0, 134, 139],
    [69, 139, 116],
    [67, 205, 128],
    [84, 139, 84],
    [0, 139, 69],
    [0, 139, 0],
    [69, 139, 0],
    [128, 170, 123],
    [48, 97, 52],
    [47, 79, 79],
    [72, 160, 146],

    # blue - #3131FD
    [119, 136, 153],
    [100, 149, 237],
    [0, 0, 205],
    [65, 105, 225],
    [30, 144, 255],
    [70, 130, 180],
    [95, 158, 160],
    [72, 118, 255],
    [67, 110, 238],
    [58, 95, 205],
    [0, 0, 255],
    [0, 0, 238],
    [28, 134, 238],
    [24, 116, 205],
    [79, 148, 205],
    [83, 134, 139],
    [82, 139, 139],
    [83, 115, 174],

    # nero - #202020
    [0, 0, 0],
    [3, 3, 3],
    [5, 5, 5],
    [8, 8, 8],
    [10, 10, 10],
    [13, 13, 13],
    [15, 15, 15],
    [18, 18, 18],
    [20, 20, 20],
    [23, 23, 23],
    [26, 26, 26],
    [28, 28, 28],
    [31, 31, 31],
    [33, 33, 33],
    [36, 36, 36],
    [38, 38, 38],
    [41, 41, 41],
    [43, 43, 43],
    [46, 46, 46],
    [48, 48, 48],
    [51, 51, 51],
    [54, 54, 54],
    [56, 56, 56],
    [59, 59, 59],
    [61, 61, 61],
    [64, 64, 64],
    [66, 66, 66],
    [69, 69, 69],
    [71, 71, 71],
    [74, 74, 74],

    # midnight blue - #1C2C85
    [112, 128, 144],
    [25, 25, 112],
    [0, 0, 128],
    [72, 61, 139],
    [71, 60, 139],
    [39, 64, 139],
    [0, 0, 139],
    [16, 78, 139],
    [54, 100, 139],
    [0, 104, 139],
    [74, 112, 139],
    [96, 123, 139],
    [108, 123, 139],
    [110, 123, 139],
    [104, 131, 139],
    [122, 139, 139],
    [48, 52, 99],
    [63, 112, 153],
    [53, 75, 116],
    [75, 75, 101],
    [29, 43, 72],
    [23, 26, 39],
    [92, 97, 134],
    [43, 60, 79],
    [110, 122, 139],
    [130, 139, 162],
    [58, 78, 96],
    [90, 103, 122],
    [136, 147, 158],
    [62, 81, 106],
    [124, 135, 150],
    [84, 93, 107],
    [110, 124, 142],
    [62, 69, 84],
    [66, 98, 145],
]

COLOR_MATCH_DICT = {
    # white - #FFFFFF
    '#fffafa': '#FFFFFF',
    '#f8f8ff': '#FFFFFF',
    '#ffffff': '#FFFFFF',
    '#f5f5f5': '#FFFFFF',
    '#dcdcdc': '#FFFFFF',
    '#f0ffff': '#FFFFFF',
    '#f0f8ff': '#FFFFFF',
    '#e0ffff': '#FFFFFF',
    '#eee9e9': '#FFFFFF',
    '#e0eeee': '#FFFFFF',
    '#d1d1d1': '#FFFFFF',
    '#d4d4d4': '#FFFFFF',
    '#d6d6d6': '#FFFFFF',
    '#d9d9d9': '#FFFFFF',
    '#dbdbdb': '#FFFFFF',
    '#dedede': '#FFFFFF',
    '#e0e0e0': '#FFFFFF',
    '#e3e3e3': '#FFFFFF',
    '#e5e5e5': '#FFFFFF',
    '#ebebeb': '#FFFFFF',
    '#ededed': '#FFFFFF',
    '#f0f0f0': '#FFFFFF',
    '#f2f2f2': '#FFFFFF',
    '#f7f7f7': '#FFFFFF',
    '#fafafa': '#FFFFFF',
    '#fcfcfc': '#FFFFFF',
    '#eee5de': '#FFFFFF',


    # classic rose - #FFC5DB
    '#fff0f5': '#FFC5DB',
    '#ffe4e1': '#FFC5DB',
    '#ff1493': '#FFC5DB',
    '#db7093': '#FFC5DB',
    '#f08080': '#FFC5DB',
    '#ff69b4': '#FFC5DB',
    '#ffc0cb': '#FFC5DB',
    '#ffb6c1': '#FFC5DB',
    '#dda0dd': '#FFC5DB',
    '#d8bfd8': '#FFC5DB',
    '#eee0e5': '#FFC5DB',
    '#cdc1c5': '#FFC5DB',
    '#eed5d2': '#FFC5DB',
    '#cdb7b5': '#FFC5DB',
    '#ffc1c1': '#FFC5DB',
    '#eeb4b4': '#FFC5DB',
    '#cd9b9b': '#FFC5DB',
    '#ee6aa7': '#FFC5DB',
    '#cd6090': '#FFC5DB',
    '#ffb5c5': '#FFC5DB',
    '#eea9b8': '#FFC5DB',
    '#cd919e': '#FFC5DB',
    '#ffaeb9': '#FFC5DB',
    '#eea2ad': '#FFC5DB',
    '#cd8c95': '#FFC5DB',
    '#ff82ab': '#FFC5DB',
    '#ee799f': '#FFC5DB',
    '#ee00ee': '#FFC5DB',
    '#ff83fa': '#FFC5DB',
    '#ee7ae9': '#FFC5DB',
    '#ffbbff': '#FFC5DB',
    '#eeaeee': '#FFC5DB',
    '#ffe1ff': '#FFC5DB',
    '#eed2ee': '#FFC5DB',
    '#cdb5cd': '#FFC5DB',
    '#cbb9b6': '#FFC5DB',
    '#dcc4bf': '#FFC5DB',
    '#bf908b': '#FFC5DB',
    '#ff6eb4': '#FFC5DB',
    '#dfccd8': '#FFC5DB',

    # turbo (lighting yellow) - #F4D424
    '#fffaf0': '#F4D424',
    '#fdf5e6': '#F4D424',
    '#ffe4c4': '#F4D424',
    '#ffdab9': '#F4D424',
    '#ffdead': '#F4D424',
    '#ffe4b5': '#F4D424',
    '#fff5ee': '#F4D424',
    '#bdb76b': '#F4D424',
    '#eedd82': '#F4D424',
    '#deb887': '#F4D424',
    '#f5deb3': '#F4D424',
    '#d2b48c': '#F4D424',
    '#ffefdb': '#F4D424',
    '#eedfcc': '#F4D424',
    '#cdc0b0': '#F4D424',
    '#eed5b7': '#F4D424',
    '#cdb79e': '#F4D424',
    '#eecbad': '#F4D424',
    '#eecfa1': '#F4D424',
    '#cdc9a5': '#F4D424',
    '#cdc8b1': '#F4D424',
    '#cdc673': '#F4D424',
    '#eedc82': '#F4D424',
    '#cdbe70': '#F4D424',
    '#cdcdb4': '#F4D424',
    '#eec900': '#F4D424',
    '#cdad00': '#F4D424',
    '#ffd39b': '#F4D424',
    '#eec591': '#F4D424',
    '#cdaa7d': '#F4D424',
    '#ffe7ba': '#F4D424',
    '#eed8ae': '#F4D424',
    '#cdba96': '#F4D424',

    # lighting yellow - #F4AA24
    '#faf0e6': '#F4AA24',
    '#faebd7': '#F4AA24',
    '#ffefd5': '#F4AA24',
    '#ffebcd': '#F4AA24',
    '#daa520': '#F4AA24',
    '#cd853f': '#F4AA24',
    '#f4a460': '#F4AA24',
    '#d2691e': '#F4AA24',
    '#e9967a': '#F4AA24',
    '#ffa07a': '#F4AA24',
    '#ff8c00': '#F4AA24',
    '#ff7f50': '#F4AA24',
    '#ff6347': '#F4AA24',
    '#ffc125': '#F4AA24',
    '#eeb422': '#F4AA24',
    '#cd9b1d': '#F4AA24',
    '#ffb90f': '#F4AA24',
    '#eead0e': '#F4AA24',
    '#cd950c': '#F4AA24',
    '#ff8247': '#F4AA24',
    '#ee7942': '#F4AA24',
    '#cd6839': '#F4AA24',
    '#ffa54f': '#F4AA24',
    '#ee9a49': '#F4AA24',
    '#ff7f24': '#F4AA24',
    '#ee7621': '#F4AA24',
    '#cd661d': '#F4AA24',
    '#ff8c69': '#F4AA24',
    '#ee8262': '#F4AA24',
    '#ee9572': '#F4AA24',
    '#ffa500': '#F4AA24',
    '#ee9a00': '#F4AA24',
    '#cd8500': '#F4AA24',
    '#ff7f00': '#F4AA24',
    '#ee7600': '#F4AA24',
    '#cd6600': '#F4AA24',
    '#ff7256': '#F4AA24',
    '#ee6a50': '#F4AA24',

    # lemon - #F1F223
    '#fff8dc': '#F1F223',
    '#fffff0': '#F1F223',
    '#fffacd': '#F1F223',
    '#ffff00': '#F1F223',
    '#f0e68c': '#F1F223',
    '#eee8aa': '#F1F223',
    '#fafad2': '#F1F223',
    '#ffffe0': '#F1F223',
    '#ffd700': '#F1F223',
    '#f5f5dc': '#F1F223',
    '#eee9bf': '#F1F223',
    '#eee8cd': '#F1F223',
    '#eeeee0': '#F1F223',
    '#fff68f': '#F1F223',
    '#eee685': '#F1F223',
    '#ffec8b': '#F1F223',
    '#eeeed1': '#F1F223',
    '#eeee00': '#F1F223',
    '#cdcd00': '#F1F223',

    # scarlet - #EC1818
    '#cd5c5c': '#EC1818',
    '#b22222': '#EC1818',
    '#a52a2a': '#EC1818',
    '#fa8072': '#EC1818',
    '#ff4500': '#EC1818',
    '#ff0000': '#EC1818',
    '#ff6a6a': '#EC1818',
    '#ee6363': '#EC1818',
    '#cd5555': '#EC1818',
    '#ff3030': '#EC1818',
    '#ee2c2c': '#EC1818',
    '#cd2626': '#EC1818',
    '#ff4040': '#EC1818',
    '#ee3b3b': '#EC1818',
    '#cd3333': '#EC1818',
    '#cd3700': '#EC1818',
    '#ee0000': '#EC1818',
    '#cd0000': '#EC1818',
    '#d70751': '#EC1818',
    '#cd4f39': '#EC1818',
    '#ee4000': '#EC1818',
    '#ee5c42': '#EC1818',
    '#cd5b45': '#EC1818',
    '#8b2323': '#EC1818',
    '#c61b30': '#EC1818',
    '#b03060': '#EC1818',

    # silver - #C6C6C6
    '#bebebe': '#C6C6C6',
    '#d3d3d3': '#C6C6C6',
    '#cdc9c9': '#C6C6C6',
    '#cdc5bf': '#C6C6C6',
    '#cdcdc1': '#C6C6C6',
    '#a1a1a1': '#C6C6C6',
    '#a3a3a3': '#C6C6C6',
    '#a6a6a6': '#C6C6C6',
    '#a8a8a8': '#C6C6C6',
    '#ababab': '#C6C6C6',
    '#adadad': '#C6C6C6',
    '#b0b0b0': '#C6C6C6',
    '#b3b3b3': '#C6C6C6',
    '#b5b5b5': '#C6C6C6',
    '#b8b8b8': '#C6C6C6',
    '#bababa': '#C6C6C6',
    '#bdbdbd': '#C6C6C6',
    '#bfbfbf': '#C6C6C6',
    '#c2c2c2': '#C6C6C6',
    '#c4c4c4': '#C6C6C6',
    '#c7c7c7': '#C6C6C6',
    '#c9c9c9': '#C6C6C6',
    '#cccccc': '#C6C6C6',
    '#cfcfcf': '#C6C6C6',
    '#e8e8e8': '#C6C6C6',

    # violet - #AF1FA3
    '#c71585': '#AF1FA3',
    '#ee82ee': '#AF1FA3',
    '#d02090': '#AF1FA3',
    '#da70d6': '#AF1FA3',
    '#ee1289': '#AF1FA3',
    '#cd1076': '#AF1FA3',
    '#8b0a50': '#AF1FA3',
    '#8b3a62': '#AF1FA3',
    '#8b636c': '#AF1FA3',
    '#8b5f65': '#AF1FA3',
    '#cd6889': '#AF1FA3',
    '#8b475d': '#AF1FA3',
    '#ff34b3': '#AF1FA3',
    '#ee30a7': '#AF1FA3',
    '#cd2990': '#AF1FA3',
    '#8b1c62': '#AF1FA3',
    '#ff3e96': '#AF1FA3',
    '#ee3a8c': '#AF1FA3',
    '#cd3278': '#AF1FA3',
    '#8b2252': '#AF1FA3',
    '#cd00cd': '#AF1FA3',
    '#8b008b': '#AF1FA3',
    '#cd69c9': '#AF1FA3',
    '#8b4789': '#AF1FA3',
    '#e066ff': '#AF1FA3',
    '#d15fee': '#AF1FA3',
    '#a63669': '#AF1FA3',
    '#794764': '#AF1FA3',
    '#785e6b': '#AF1FA3',
    '#a793b9': '#AF1FA3',
    '#d5c6e9': '#AF1FA3',
    '#aeaee4': '#AF1FA3',
    '#bfa7b6': '#AF1FA3',

    # inchworm - #A5DD0C
    '#f0fff0': '#A5DD0C',
    '#f5fffa': '#A5DD0C',
    '#90ee90': '#A5DD0C',
    '#66cdaa': '#A5DD0C',
    '#7fffd4': '#A5DD0C',
    '#98fb98': '#A5DD0C',
    '#00ff7f': '#A5DD0C',
    '#7cfc00': '#A5DD0C',
    '#adff2f': '#A5DD0C',
    '#7fff00': '#A5DD0C',
    '#00fa9a': '#A5DD0C',
    '#9acd32': '#A5DD0C',
    '#e0eee0': '#A5DD0C',
    '#c1cdc1': '#A5DD0C',
    '#76eec6': '#A5DD0C',
    '#c1ffc1': '#A5DD0C',
    '#b4eeb4': '#A5DD0C',
    '#9bcd9b': '#A5DD0C',
    '#54ff9f': '#A5DD0C',
    '#4eee94': '#A5DD0C',
    '#9aff9a': '#A5DD0C',
    '#7ccd7c': '#A5DD0C',
    '#00ee76': '#A5DD0C',
    '#00cd66': '#A5DD0C',
    '#00ff00': '#A5DD0C',
    '#00ee00': '#A5DD0C',
    '#00cd00': '#A5DD0C',
    '#76ee00': '#A5DD0C',
    '#66cd00': '#A5DD0C',
    '#c0ff3e': '#A5DD0C',
    '#b3ee3a': '#A5DD0C',
    '#caff70': '#A5DD0C',
    '#bcee68': '#A5DD0C',
    '#a2cd5a': '#A5DD0C',

    # cornflower - #99D1EA
    '#00bfff': '#99D1EA',
    '#87ceeb': '#99D1EA',
    '#87cefa': '#99D1EA',
    '#b0c4de': '#99D1EA',
    '#add8e6': '#99D1EA',
    '#b0e0e6': '#99D1EA',
    '#afeeee': '#99D1EA',
    '#00ced1': '#99D1EA',
    '#48d1cc': '#99D1EA',
    '#40e0d0': '#99D1EA',
    '#00ffff': '#99D1EA',
    '#c1cdcd': '#99D1EA',
    '#63b8ff': '#99D1EA',
    '#5cacee': '#99D1EA',
    '#00b2ee': '#99D1EA',
    '#009acd': '#99D1EA',
    '#87ceff': '#99D1EA',
    '#7ec0ee': '#99D1EA',
    '#6ca6cd': '#99D1EA',
    '#b0e2ff': '#99D1EA',
    '#a4d3ee': '#99D1EA',
    '#8db6cd': '#99D1EA',
    '#c6e2ff': '#99D1EA',
    '#b9d3ee': '#99D1EA',
    '#9fb6cd': '#99D1EA',
    '#cae1ff': '#99D1EA',
    '#bcd2ee': '#99D1EA',
    '#bfefff': '#99D1EA',
    '#b2dfee': '#99D1EA',
    '#9ac0cd': '#99D1EA',
    '#d1eeee': '#99D1EA',
    '#b4cdcd': '#99D1EA',
    '#bbffff': '#99D1EA',
    '#aeeeee': '#99D1EA',
    '#96cdcd': '#99D1EA',
    '#98f5ff': '#99D1EA',
    '#8ee5ee': '#99D1EA',
    '#7ac5cd': '#99D1EA',
    '#00f5ff': '#99D1EA',
    '#00e5ee': '#99D1EA',
    '#00c5cd': '#99D1EA',
    '#00eeee': '#99D1EA',
    '#00cdcd': '#99D1EA',
    '#008b8b': '#99D1EA',
    '#97ffff': '#99D1EA',
    '#8deeee': '#99D1EA',
    '#79cdcd': '#99D1EA',
    '#8799a6': '#99D1EA',
    '#b7c5ca': '#99D1EA',
    '#84abd4': '#99D1EA',
    '#c7eae5': '#99D1EA',
    '#afd5cf': '#99D1EA',
    '#bcc5d0': '#99D1EA',
    '#b2bbcd': '#99D1EA',
    '#858b9b': '#99D1EA',
    '#ced2e2': '#99D1EA',
    '#99aab0': '#99D1EA',
    '#d9e1f0': '#99D1EA',
    '#bdc7dc': '#99D1EA',

    # chelsea gem - #90572F
    '#8b0000': '#90572F',
    '#b8860b': '#90572F',
    '#bc8f8f': '#90572F',
    '#8b4513': '#90572F',
    '#a0522d': '#90572F',
    '#8b8378': '#90572F',
    '#8b7d6b': '#90572F',
    '#cdaf95': '#90572F',
    '#8b7765': '#90572F',
    '#cdb38b': '#90572F',
    '#8b795e': '#90572F',
    '#8b8970': '#90572F',
    '#8b8878': '#90572F',
    '#8b814c': '#90572F',
    '#8b7500': '#90572F',
    '#8b6914': '#90572F',
    '#8b6508': '#90572F',
    '#8b6969': '#90572F',
    '#8b3a3a': '#90572F',
    '#8b4726': '#90572F',
    '#8b7355': '#90572F',
    '#8b7e66': '#90572F',
    '#8b5a2b': '#90572F',
    '#8b1a1a': '#90572F',
    '#8b4c39': '#90572F',
    '#cd8162': '#90572F',
    '#8b5742': '#90572F',
    '#8b5a00': '#90572F',
    '#8b4500': '#90572F',
    '#8b3e2f': '#90572F',
    '#8b3626': '#90572F',
    '#8b2500': '#90572F',
    '#925d44': '#90572F',
    '#926167': '#90572F',
    '#690631': '#90572F',
    '#744426': '#90572F',
    '#542c13': '#90572F',
    '#594435': '#90572F',
    '#946f56': '#90572F',
    '#965f60': '#90572F',
    '#988275': '#90572F',
    '#aa9994': '#90572F',
    '#afa386': '#90572F',
    '#c6b1a6': '#90572F',
    '#9a8b7c': '#90572F',
    '#c9a69d': '#90572F',
    '#cd7054': '#90572F',
    '#b4867e': '#90572F',

    # grey - #8B8B8B
    '#696969': '#8B8B8B',
    '#8b8989': '#8B8B8B',
    '#8b8682': '#8B8B8B',
    '#8b8b83': '#8B8B8B',
    '#838b83': '#8B8B8B',
    '#8b8386': '#8B8B8B',
    '#8b7d7b': '#8B8B8B',
    '#838b8b': '#8B8B8B',
    '#8b8b7a': '#8B8B8B',
    '#8b7b8b': '#8B8B8B',
    '#4d4d4d': '#8B8B8B',
    '#4f4f4f': '#8B8B8B',
    '#525252': '#8B8B8B',
    '#545454': '#8B8B8B',
    '#575757': '#8B8B8B',
    '#595959': '#8B8B8B',
    '#5c5c5c': '#8B8B8B',
    '#5e5e5e': '#8B8B8B',
    '#616161': '#8B8B8B',
    '#636363': '#8B8B8B',
    '#666666': '#8B8B8B',
    '#6b6b6b': '#8B8B8B',
    '#6e6e6e': '#8B8B8B',
    '#707070': '#8B8B8B',
    '#737373': '#8B8B8B',
    '#757575': '#8B8B8B',
    '#787878': '#8B8B8B',
    '#7a7a7a': '#8B8B8B',
    '#7d7d7d': '#8B8B8B',
    '#7f7f7f': '#8B8B8B',
    '#828282': '#8B8B8B',
    '#858585': '#8B8B8B',
    '#878787': '#8B8B8B',
    '#8a8a8a': '#8B8B8B',
    '#8c8c8c': '#8B8B8B',
    '#8f8f8f': '#8B8B8B',
    '#919191': '#8B8B8B',
    '#949494': '#8B8B8B',
    '#969696': '#8B8B8B',
    '#999999': '#8B8B8B',
    '#9c9c9c': '#8B8B8B',
    '#9e9e9e': '#8B8B8B',
    '#a9a9a9': '#8B8B8B',

    # dark violet - #8316C0
    '#6a5acd': '#8316C0',
    '#9370db': '#8316C0',
    '#7b68ee': '#8316C0',
    '#8470ff': '#8316C0',
    '#8a2be2': '#8316C0',
    '#ba55d3': '#8316C0',
    '#9932cc': '#8316C0',
    '#9400d3': '#8316C0',
    '#a020f0': '#8316C0',
    '#836fff': '#8316C0',
    '#7a67ee': '#8316C0',
    '#6959cd': '#8316C0',
    '#cd96cd': '#8316C0',
    '#8b668b': '#8316C0',
    '#b452cd': '#8316C0',
    '#7a378b': '#8316C0',
    '#bf3eff': '#8316C0',
    '#b23aee': '#8316C0',
    '#9a32cd': '#8316C0',
    '#68228b': '#8316C0',
    '#9b30ff': '#8316C0',
    '#912cee': '#8316C0',
    '#7d26cd': '#8316C0',
    '#551a8b': '#8316C0',
    '#ab82ff': '#8316C0',
    '#9f79ee': '#8316C0',
    '#8968cd': '#8316C0',
    '#5d478b': '#8316C0',
    '#c9ccf5': '#8316C0',
    '#512a42': '#8316C0',
    '#8b83af': '#8316C0',
    '#7d6785': '#8316C0',
    '#9a8b9a': '#8316C0',

    # olive - #71842F
    '#808000': '#71842F',
    '#556b2f': '#71842F',
    '#8fbc8f': '#71842F',
    '#6b8e23': '#71842F',
    '#698b69': '#71842F',
    '#698b22': '#71842F',
    '#6e8b3d': '#71842F',
    '#8b864e': '#71842F',
    '#8b8b00': '#71842F',
    '#89825c': '#71842F',
    '#7f8564': '#71842F',
    '#90a099': '#71842F',
    '#57635d': '#71842F',
    '#373e39': '#71842F',
    '#718079': '#71842F',
    '#5d5a4c': '#71842F',
    '#92958f': '#71842F',
    '#667a5b': '#71842F',
    '#969993': '#71842F',
    '#35432b': '#71842F',

    # green - #37B400
    '#006400': '#37B400',
    '#2e8b57': '#37B400',
    '#3cb371': '#37B400',
    '#20b2aa': '#37B400',
    '#32cd32': '#37B400',
    '#228b22': '#37B400',
    '#668b8b': '#37B400',
    '#00868b': '#37B400',
    '#458b74': '#37B400',
    '#43cd80': '#37B400',
    '#548b54': '#37B400',
    '#008b45': '#37B400',
    '#008b00': '#37B400',
    '#458b00': '#37B400',
    '#80aa7b': '#37B400',
    '#306134': '#37B400',
    '#2f4f4f': '#37B400',
    '#48a092': '#37B400',

    # blue - #3131FD
    '#778899': '#3131FD',
    '#6495ed': '#3131FD',
    '#0000cd': '#3131FD',
    '#4169e1': '#3131FD',
    '#1e90ff': '#3131FD',
    '#4682b4': '#3131FD',
    '#5f9ea0': '#3131FD',
    '#4876ff': '#3131FD',
    '#436eee': '#3131FD',
    '#3a5fcd': '#3131FD',
    '#0000ff': '#3131FD',
    '#0000ee': '#3131FD',
    '#1c86ee': '#3131FD',
    '#1874cd': '#3131FD',
    '#4f94cd': '#3131FD',
    '#53868b': '#3131FD',
    '#528b8b': '#3131FD',
    '#5373ae': '#3131FD',

    # nero - #202020
    '#000000': '#202020',
    '#030303': '#202020',
    '#050505': '#202020',
    '#080808': '#202020',
    '#0a0a0a': '#202020',
    '#0d0d0d': '#202020',
    '#0f0f0f': '#202020',
    '#121212': '#202020',
    '#141414': '#202020',
    '#171717': '#202020',
    '#1a1a1a': '#202020',
    '#1c1c1c': '#202020',
    '#1f1f1f': '#202020',
    '#212121': '#202020',
    '#242424': '#202020',
    '#262626': '#202020',
    '#292929': '#202020',
    '#2b2b2b': '#202020',
    '#2e2e2e': '#202020',
    '#303030': '#202020',
    '#333333': '#202020',
    '#363636': '#202020',
    '#383838': '#202020',
    '#3b3b3b': '#202020',
    '#3d3d3d': '#202020',
    '#404040': '#202020',
    '#424242': '#202020',
    '#454545': '#202020',
    '#474747': '#202020',
    '#4a4a4a': '#202020',

    # midnight blue - #1C2C85
    '#708090': '#1C2C85',
    '#191970': '#1C2C85',
    '#000080': '#1C2C85',
    '#483d8b': '#1C2C85',
    '#473c8b': '#1C2C85',
    '#27408b': '#1C2C85',
    '#00008b': '#1C2C85',
    '#104e8b': '#1C2C85',
    '#36648b': '#1C2C85',
    '#00688b': '#1C2C85',
    '#4a708b': '#1C2C85',
    '#607b8b': '#1C2C85',
    '#6c7b8b': '#1C2C85',
    '#6e7b8b': '#1C2C85',
    '#68838b': '#1C2C85',
    '#7a8b8b': '#1C2C85',
    '#303463': '#1C2C85',
    '#3f7099': '#1C2C85',
    '#354b74': '#1C2C85',
    '#4b4b65': '#1C2C85',
    '#1d2b48': '#1C2C85',
    '#171a27': '#1C2C85',
    '#5c6186': '#1C2C85',
    '#2b3c4f': '#1C2C85',
    '#6e7a8b': '#1C2C85',
    '#828ba2': '#1C2C85',
    '#3a4e60': '#1C2C85',
    '#5a677a': '#1C2C85',
    '#88939e': '#1C2C85',
    '#3e516a': '#1C2C85',
    '#7c8796': '#1C2C85',
    '#545d6b': '#1C2C85',
    '#6e7c8e': '#1C2C85',
    '#3e4554': '#1C2C85',
    '#426291': '#1C2C85',
}
