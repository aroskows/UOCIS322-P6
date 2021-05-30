from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
   return render_template('index.html')


@app.route('/listeverything')
def listeverything():
    ''' these ports might be wrong ?'''
    r = requests.get('http://restapi:5000/listAll')
    return r.text

@app.route('/listopentimes')
def listopentimes():
    r = requests.get('http://restapi:5000/listOpen')
    return r.text

@app.route('/listclosetimes')
def listclosetimes():
    app.logger.debug("website")
    r = requests.get('http://128.223.8.30:5974/listClose')
    app.logger.debug(r)
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
