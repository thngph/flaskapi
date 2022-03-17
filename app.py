from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
import pandas as pd
import pickle as p
import json


app = Flask(__name__)
modelfile = 'models/final_prediction.sav'
model = p.load(open(modelfile, 'rb'))

@app.route("/", methods=["GET"])
def hello():
    return render_template('index.html')

@app.route('/api/', methods=['POST'])
def makecalc():
    data = []
    data.append(request.form['fa'])
    data.append(request.form['va'])
    data.append(request.form['ca'])
    data.append(request.form['rs'])
    data.append(request.form['ch'])
    data.append(request.form['fs'])
    data.append(request.form['ts'])
    data.append(request.form['ds'])
    data.append(request.form['ph'])
    data.append(request.form['su'])
    data.append(request.form['al'])
    #data = request.get_json(force=True)
    data = np.array(data).reshape(1, -1)
    prediction = np.array2string(model.predict(data))
    output = {"Quality":np.uint0(prediction[1])}
    return render_template('output.html', output=output)

@app.route('/api/raw', methods=['POST'])
def makeprediction():
    data = request.get_json(force=True)
    data = np.array(data)
    prediction = np.array2string(model.predict(data))
    return prediction

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')