from flask import render_template
from monyy import app

@app.route("/")
def hello():
    return render_template("index.html") 

