from flask import Flask, render_template, url_for
from sunnygg import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')
