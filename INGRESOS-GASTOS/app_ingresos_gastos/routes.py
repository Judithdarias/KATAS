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
        #fecha_actual = str(date.today())

        #if request.form['dfecha'] > fecha_actual:
        #    return render_template("new.html",title="Registro", titulo="Registro",boton="Guardar")
        comprobar_errores =  validar_formulario(request.form)
        if comprobar_errores:
            return render_template("new.html",title="Registro", titulo="Registro",boton="Guardar",error=comprobar_errores,dataform = request.form)
        else:
            ################Generar el nuevo id para registro###############################    
            lista_id=[]
            last_id=""
            new_id=0
            fichero = open('app_ingresos_gastos/data/movimientos.csv','r')
            lectura = csv.reader(fichero,delimiter=",",quotechar='"')
            for item in lectura:
                lista_id.append(item[0]) #guardo solo los ids eje:[1,2,3]
            last_id = lista_id[-1]#obtenemos el ultimo id registrado
            new_id = int(last_id) +1 #creo el nuevo id para luego registrarlo
            fichero.close()

            #################################Guardar el id anterior en last_id.csv###############################################
            fichero_new_id=open('app_ingresos_gastos/data/last_id.csv','w')
            fichero_new_id.write(str(new_id))
            fichero_new_id.close()

            #acceder al archivo y configurar la carga del nuevo registro
            mifichero = open('app_ingresos_gastos/data/movimientos.csv','a',newline="")
            #llamar al metodo writer de escritura y configuramos el formato
            lectura = csv.writer(mifichero,delimiter=",",quotechar='"')
            #registramos los datos recibidos desde el formulario al archivo csv
            lectura.writerow( [ new_id, request.form['dfecha'],request.form['dconcepto'],request.form['dmonto'] ] )
            #cierre del archivo moviemientos.csv
            mifichero.close()

            return redirect("/")#esto es para redirigir a la ruta home
        
    else:#esto seria GET
        return render_template("new.html",title="Registro", titulo="Registro",boton="Guardar",dataform={}) 

#http://127.0.0.1:5000/delete
@app.route("/delete/<int:id>")
def delete(id):
    return f"El registro para borrar es el de id:{id}"
    #return render_template("delete.html",title="Borrar")


#http://127.0.0.1:5000/update
@app.route("/update/<int:id>")
def update(id):
    return f"El registro para actualizar es el de id:{id}"
    #return render_template("update.html",title="Actualizar",titulo="Actualización",boton="Actualizar")


"""
    que la fecha ingresada no sea mayor que la actual
    que el concepto no vaya vació
    que el monto sea distinto de 0(cero) y de vacio
"""

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