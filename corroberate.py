from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1/')
def test_1():
    return render_template('1/index.html')

@app.route('/2/')
def test_2():
    return render_template('2/index.html')

@app.route('/3/')
def test_3():
    return render_template('3/index.html')

@app.route('/4/')
def test_4():
    return render_template('4/index.html')

@app.route('/5/')
def test_5():
    return render_template('5/index.html')

@app.route('/6/')
def test_6():
    return render_template('6/index.html')

@app.route('/7/')
def test_7():
    return render_template('7/index.html')

@app.route('/8/')
def test_8():
    return render_template('8/index.html')
