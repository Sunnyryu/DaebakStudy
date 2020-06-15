import os
from flask import render_template, url_for, redirect, request
from editor import app
from editor.db.createtable import Createtable
from editor.db.create import Create
#from editor.db.insert import insert


@app.route("/")
def index():
    #create_table = Createtable()
    insert_row = Create()
    return render_template('index.html')
