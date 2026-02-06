from app_ingresos_gastos import app
from flask import render_template,request,redirect
import csv
from datetime import date

#http://127.0.0.1:5000/
@app.route("/")
def index():
    
    datos=[]
    fichero = open('app_ingresos_gastos/data/movimientos.csv','r')
    lectura = csv.reader(fichero,delimiter=",",quotechar='"')
    for item in lectura:
        datos.append(item) 

    fichero.close()
    """
    datos = [
        {'fecha':'01/09/2025','concepto':'Salario','monto':1800},
        {'fecha':'15/09/2025','concepto':'Compras de Alimentos','monto':-250},
        {'fecha':'30/09/2025','concepto':'Compra de Ropa','monto':-150},
    ]
    """
    return render_template("index.html",title="Lista",lista = datos) 


#http://127.0.0.1:5000/new
@app.route("/new",methods=["GET","POST"])
def new():
    if request.method == "POST":
        fecha_actual = str(date.today())

        if request.form['dfecha'] > fecha_actual:
            return render_template("new.html",title="Registro", titulo="Registro",boton="Guardar")
        else:
            #acceder al archivo y configurar la carga del nuevo registro
            mifichero = open('app_ingresos_gastos/data/movimientos.csv','a',newline="")
            #llamar al metodo writer de escritura y configuramos el formato
            lectura = csv.writer(mifichero,delimiter=",",quotechar='"')
            #registramos los datos recibidos desde el formulario al archivo csv
            lectura.writerow( [request.form['dfecha'],request.form['dconcepto'],request.form['dmonto']] )
            #cierre del archivo moviemientos.csv
            mifichero.close()

            return redirect("/")#esto es para redirigir a la ruta home
        
    else:#esto seria GET
        return render_template("new.html",title="Registro", titulo="Registro",boton="Guardar") 

#http://127.0.0.1:5000/delete
@app.route("/delete")
def delete():
    return render_template("delete.html",title="Borrar")

#http://127.0.0.1:5000/update
@app.route("/update")
def update():
    return render_template("update.html",title="Actualizar",titulo="Actualización",boton="Actualizar")