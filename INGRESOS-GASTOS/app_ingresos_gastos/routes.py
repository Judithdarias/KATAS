from app_ingresos_gastos import app,MOVIMIENTOS_FILE,LAST_ID_FILE
from flask import render_template,request,redirect
import csv
from datetime import date
from app_ingresos_gastos.models import *

#http://127.0.0.1:5000/
@app.route("/")
def index():
    datos = select_all()
    return render_template("index.html",title="Lista",lista = datos) 


#http://127.0.0.1:5000/new
@app.route("/new",methods=["GET","POST"])
def new():
    if request.method == "POST":
       
        comprobar_errores =  validar_formulario(request.form)
        if comprobar_errores:
            return render_template("new.html",title="Registro", titulo="Registro",boton="Guardar",error=comprobar_errores,dataform = request.form,ruta="/new")
        else:
            insert(request.form)
            return redirect("/")#esto es para redirigir a la ruta home
        
    else:#esto seria GET
        return render_template("new.html",title="Registro", titulo="Registro",boton="Guardar",dataform={}, ruta="/new") 

#http://127.0.0.1:5000/delete/{id}
@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):

    if request.method == 'GET':
        registro_buscado = select_by(id,"igual")
        return render_template("delete.html",title="Borrar", dato = registro_buscado)
    
    else:#POST
        #################Lectura de archivo csv para quitar todos los registros excepto el del id dado##############
        registros = select_by(id,"distinto")
        ##########Guardar el registro de datos obtenidos##########################
        delete_by(registros)

        return redirect("/")

#http://127.0.0.1:5000/update/{id}
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    if request.method == 'GET':
        registro_buscado_update = select_by(id,"dic")
        
        return render_template("update.html",title="Actualizar",titulo="Actualización",boton="Actualizar", dataform =registro_buscado_update, ruta=f"/update/{id}")
    else:#POST

        comprobar_error = validar_formulario(request.form)

        if comprobar_error:
            return render_template("update.html",title="Actualizar",titulo="Actualización",boton="Actualizar", dataform =request.form, ruta=f"/update/{id}",error = comprobar_error)

        todos_registros=select_all()
        update_by(id,todos_registros,request.form)

        return redirect("/")


def validar_formulario(datos_formulario):
    hoy = str( date.today() )
    if datos_formulario['dmonto'] != "":
        monto_int = float( datos_formulario['dmonto'] )
    errores = []
    if datos_formulario['dfecha'] > hoy:
        errores.append("La fecha no puede ser mayor que la actual")
    if datos_formulario['dconcepto'] == "":
        errores.append("El concepto no puede ir vacio")
    if datos_formulario['dmonto'] == "" or  monto_int == 0:
        errores.append("El monto deber ser distinto de 0 y de vacio")

    return errores    
    hoy = str( date.today() )
    if datos_formulario['dmonto'] != "":
        monto_int = float( datos_formulario['dmonto'] )
    errores = []
    if datos_formulario['dfecha'] > hoy:
        errores.append("La fecha no puede ser mayor que la actual")
    if datos_formulario['dconcepto'] == "":
        errores.append("El concepto no puede ir vacio")
    if datos_formulario['dmonto'] == "" or  monto_int == 0:
        errores.append("El monto deber ser distinto de 0 y de vacio")

    return errores    