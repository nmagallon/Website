__author__ = 'nadia'

import os
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('homepage.html', name=name)

@app.route('/artPortfolio/')
@app.route('/artPortfolio/<name>')
def artPortfolio(name=None):
    return render_template('artPortfolio.html', name=name)

if __name__ == "__main__":
    app.run(debug = True)
