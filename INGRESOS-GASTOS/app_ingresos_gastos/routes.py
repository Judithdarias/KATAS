from app_ingresos_gastos import app 
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html")