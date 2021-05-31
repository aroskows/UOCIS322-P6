from flask import Flask, render_template, request
import requests
import flask
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
   return render_template('index.html')


@app.route('/listeverything')
def listeverything():
    ''' these ports might be wrong ?'''
    dtype = request.args.get("dtype")
    r = requests.get('http://restapi:5000/listAll/' + dtype)
    return flask.jsonify({"result": r.text})

@app.route('/listopentimes')
def listopentimes():
    dtype = request.args.get("dtype")
    r = requests.get('http://restapi:5000/listOpen/' + dtype)
    return flask.jsonify({"result": r.text})

@app.route('/listclosetimes')
def listclosetimes():
    dtype = request.args.get("dtype")
    topk = request.args.get("topk")
    r = requests.get('http://restapi:5000/listClose/' + dtype) 
    app.logger.debug(r)
    
    return flask.jsonify({"result": r.text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
