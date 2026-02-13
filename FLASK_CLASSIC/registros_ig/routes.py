from registros_ig import app
from flask import render_template,request
from registros_ig.models import *

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html",datos = registros)


@app.route("/new",methods=['GET','POST'])
def create():
    if request.method == "GET":
        return render_template("create.html")
    else:
        return f"aqui debo guardar en base de datos el registro: {request.form}"

