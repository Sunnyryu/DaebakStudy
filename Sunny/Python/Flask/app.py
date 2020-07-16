from flask import Flask, render_template, request, redirect
#from scrapper import get_jobs

app = Flask("SuperScrapper")

@app.route("/1")
def home():
    return render_template("home.html")

app.run(port="2222")