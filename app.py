from unittest import result
from flask import Flask, render_template, jsonify, request
import os

from flask_cors import cross_origin
from requests import request
from predict import model
from utils.utils import decodeImage


app = Flask(__name__)

class CnnApp:
    def __init__(self):
        self.filename = 'inputimage.jpg'
        self.classifier = model(self.filename)

@app.route('/', methods = ["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods = ['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, cnnapp.filename)
    result = cnnapp.classifier.model_prediction()
    return jsonify(result)

if __name__ == "__main__":
    cnnapp = CnnApp()

    app.run(host="0.0.0.0", port=5000)









print('Successfully Run')