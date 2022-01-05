from flask import Flask, json, render_template, url_for, request, redirect, jsonify, make_response, send_from_directory, safe_join, abort
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin
from requests.api import get
from Unipose.pose_model_inference import  inference_model
import torch


import service
# from preprocess import preprocess, predict
from pred import get_pred

app = Flask(__name__, template_folder='Template')
cors = CORS(app)
Bootstrap(app)

app.config['image'] = '/home/sonhos/Basement/VisionDemo/static/images/infered'
# model = torch.hub.load('JJ-HH/yolov5', 'yolov5x')
# 핸드폰 계단 샐러드 개 고양이 
total = torch.hub.load('JJ-HH/yolov5', 'custom', path='yolov5m_total.pt')
# 핸드폰 과일
fruit = torch.hub.load('JJ-HH/yolov5', 'custom', path='yolov5m_fruit.pt')


"""
Routes
"""
@app.route('/', methods=['GET'])
def index():
    # return render_template('webcam.html')
    return render_template('main_page.html')

@app.route('/image/<path:image_name>', methods=['GET'])
def send_infered_img(image_name):
    safe_path = safe_join(app.config['image'], image_name)
    print(safe_path)
    try:
        return send_from_directory(app.config['image'], image_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route('/capture_img', methods=['POST'])
def capture_img():
    pose = ['pullup', 'pushup', 'plank', 'squat']
    yolo = {'stairs': 'stairs', 'walk with pet': ('cat', 'dog'), 'salad': 'salad', 'fruit': 'fruit'}
    
    msg, im_path = service.save_img(request.form["img"])
    infered_path = im_path.replace("auth", "infered")

    ch = request.form["challenge"]
    challenge = ch.replace("-", "").lower()

    result = {}
    if challenge in pose:
        is_posture = inference_model(challenge, im_path, model_dir='Unipose/classifier')
        result['success'] = is_posture
    else:
        if challenge == 'fruit': 
            infered = fruit(im_path)
        else:
            infered = total(im_path)
        infered.save(save_dir="static/images/infered")
        detected = get_pred(infered)
        result['success'] = yolo.get(challenge, "") in detected
        print(detected)

    # url_filename = infered_path.replace("static/", "")
    filename = infered_path.split('/')[-1].strip(" ")
    # print(url_for('static', filename=filename))
    result['img'] = filename
    print(challenge,  result)

    return make_response(jsonify(result))


if __name__ == "__main__":
    app.run()
    # app.run(host="0.0.0.0", port=5000)
