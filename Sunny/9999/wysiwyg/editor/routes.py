import os
from flask import render_template, url_for, Flask, redirect, request
from editor import app

@app.route("/")
def index():
    return render_template('index.html')

