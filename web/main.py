# coding: utf-8

from flask import Flask, request, Response, url_for, render_template, request, redirect, session, make_response, json
from flask_cors import CORS

# import numpy as np
# import cv2

import requests
import json
from io import StringIO
import csv


# color
from procs.color_extract import ColorExtractor
from utils.utils import *

#-------------------------------------------------
# app 설정
app = Flask(__name__, static_url_path='/static')

cors = CORS(app)

jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    block_start_string='{%',
    block_end_string='%}',
    variable_start_string='[[',
    variable_end_string=']]',
    comment_start_string='{#',
    comment_end_string='#}'
))
app.jinja_options = jinja_options

extractor = ColorExtractor()


## request function
@app.route("/product/byCategory", methods=['GET'])
def product():
    # test
    # curl -X GET "http://127.0.0.1:8080/product/byCategory?lastProductId=251187412&lastTimestamp=1566831600&categoryId=10000000%20(%EC%97%AC%EC%84%B1)" -H "accept: application/json"
    # curl -X GET "http://34.84.27.156/product/byCategory?lastProductId=1107055443&lastTimestamp=1591161992&categoryId=10000000%20(%EC%97%AC%EC%84%B1)" -H "accept: application/json"

    headers = {'Content-Type': "application/json", 'accept': "application/json"}

    a = request.args.get('lastTimestamp')
    b = request.args.get('lastProductId')
    c = request.args.get('categoryId')

    # data json화 시켜줘야 함.
    data = {
        "list": [
                    {'a':a, 'b':b, 'c':c},
                    {'a': a, 'b': b, 'c': c}

                ]
        }

    data = json.dumps(data)
    print(data)
    requests.put('http://127.0.0.1:8080/product/beauty', data=data, headers=headers)
    # Response(json.dumps(data), mimetype="application/json")

    return '200'

@app.route("/product/beauty", methods=['PUT'])
def beauty_score():
    data = request.get_json()
    print(data)
    print('success score')
    # Response('success', status=201, mimetype='application/json')
    return '200', 200

# https://stackoverflow.com/questions/47515243/reading-image-file-file-storage-object-using-cv2
@app.route("/extract_color", methods=['GET','POST'])
def extract_color():
    if request.method == 'POST':

        deal_id = json.loads(request.data.decode('utf8'))['deal_id']
        #img_url = make_wmp_deal_img_url(deal_id)
        img_url = make_wmp_prod_img_url(deal_id)
        img, _ = load_img_from_url(img_url)

        # PIL로 읽었을 때는 img 차원 바꿔주어야함
        # Opencv로 읽었을 때는 pass
        img = img[:,:,::-1]
        color_result = eval(extractor.do(img))

        # color가 단일 컬러로 나올때를 대비해서..!
        if len(color_result) > 1:
            hex_code_1st, hex_code_2nd = color_result[0]['rgb'], color_result[1]['rgb']
        else:
            hex_code_1st, hex_code_2nd = color_result[0]['rgb'], None

        result = {
            'img_url': img_url,
            'color_1st' : hex_code_1st,
            'color_2nd': hex_code_2nd
        }

        # color_box img input 미리보기 코드...
        # image to numpy array
        # filestr = request.files['file'].read()
        # # DeprecationWarning: The binary mode of fromstring is deprecated, as it behaves surprisingly on unicode inputs. Use frombuffer instead
        # np_img = np.frombuffer(filestr, np.uint8)
        # img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        #
        # color_result = eval(extractor.do(img))
        # dominant_hex_code = color_result[0]['rgb']
        #
        # result = {
        #     'color' : dominant_hex_code
        # }

    return result, 200

@app.route("/upload", methods=['GET','POST'])
def upload_file():
    f = request.files['file']
    f.save('test.xlsb')

    #file = request.files['file']
    #file.save('test.xlsb')
    # print('>>>', request.files)
    # read_file = file.read()
    #
    # data = read_file.decode('utf-8').splitlines()
    # print('<<<', data)
    # filename = secure_filename(file.filename)
    # print('>>>', filename)

    return index()

@app.route("/main", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        test = request.data
        print(test)
    return 'success'

@app.route("/index", methods=['GET', 'POST'])
def index():
    combo_items = ['a', 'b', 'c']

    return render_template('index.html',combo_items=combo_items)

@app.route("/canvas")
def canvas():
    return render_template('canvas.html')

@app.route("/get_csv", methods=['POST', 'GET'])
def get_csv():
    file_name='test.csv'
    data = StringIO()
    # 한글 인코딩 위해 UTF-8 with BOM 설정해주기
    data.write(u'\ufeff')

    w = csv.writer(data)
    w.writerow(['test','test'])
    with open(file_name, 'w') as f:
        print(data.getvalue(), file=f)
    output_data = data.getvalue()

    cast_file_name = file_name

    output = make_response(output_data)
    output.headers["Content-Disposition"] = "attachment; filename={0}".format(cast_file_name)
    output.headers["Content-type"] = "text/csv"

    return output, 200

@app.route("/run_model", methods=['POST', 'GET'])
def run_model():

    # status 확인
    with open("saved_csv.json", "r") as json_file:
        meta_data = json.load(json_file)

    query_status = meta_data['query_status']
    print(query_status)

    if query_status == 1:
        return {'status': 1}
    else:
        return {'status': 0}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True)