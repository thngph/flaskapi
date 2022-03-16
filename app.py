from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pandas as pd
import pickle as p
import json


app = Flask(__name__)
modelfile = 'models/final_prediction.sav'
model = p.load(open(modelfile, 'rb'))

@app.route("/", methods=["GET"])
def hello():
    return jsonify("hello from ML API of Red Wine data!")

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json(force=True)
    data = np.array(data)
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')