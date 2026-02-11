from app_ingresos_gastos import MOVIMIENTOS_FILE,LAST_ID_FILE
import csv

def select_all():
    datos=[]
    fichero = open(MOVIMIENTOS_FILE,'r')
    lectura = csv.reader(fichero,delimiter=",",quotechar='"')
    for item in lectura:
        datos.append(item) 

    fichero.close()

    return datos


def select_by(id,condicion):
    registro_buscado=[]
    fichero_delete = open(MOVIMIENTOS_FILE,'r')
    lectura_delete = csv.reader(fichero_delete,delimiter=",",quotechar='"')
    for item in lectura_delete: 
        if condicion == "igual":
             if item[0] == str(id):
                #encuentro el id buscado en mi lista de registros
                registro_buscado = item
        elif condicion =="distinto":
            if item[0] != str(id):
                registro_buscado.append(item)
        elif condicion == "dic":
            if item[0] == str(id):
                #encuentro el id buscado en mi lista de registros
                registro_buscado={}
                registro_buscado['id'] = item[0]
                registro_buscado['dfecha'] = item[1]
                registro_buscado['dconcepto'] = item[2]
                registro_buscado['dmonto'] = item[3]

    
    fichero_delete.close()

    return registro_buscado

def delete_by(lista):
    fichero_guardar = open(MOVIMIENTOS_FILE,'w',newline='')
    csv_writer = csv.writer(fichero_guardar, delimiter=',',quotechar='"')
    #registramos los datos recibidos en el archivo csv
    for datos in lista:
        csv_writer.writerow(datos)

    fichero_guardar.close()    

def insert(request_form):
    ################Generar el nuevo id para registro###############################    
    lista_id=[]
    last_id=""
    new_id=0
    fichero = open(LAST_ID_FILE,'r')
    lectura = csv.reader(fichero,delimiter=",",quotechar='"')
    for item in lectura:
        lista_id.append(item[0]) #guardo solo los ids eje:[1,2,3]
    last_id = lista_id[-1]#obtenemos el ultimo id registrado
    new_id = int(last_id) +1 #creo el nuevo id para luego registrarlo
    fichero.close()

    #################################Guardar el id anterior en last_id.csv###############################################
    fichero_new_id=open(LAST_ID_FILE,'w')
    fichero_new_id.write(str(new_id))
    fichero_new_id.close()

    #acceder al archivo y configurar la carga del nuevo registro
    mifichero = open(MOVIMIENTOS_FILE,'a',newline="")
    #llamar al metodo writer de escritura y configuramos el formato
    lectura = csv.writer(mifichero,delimiter=",",quotechar='"')
    #registramos los datos recibidos desde el formulario al archivo csv
    lectura.writerow( [ new_id, request_form['dfecha'],request_form['dconcepto'],request_form['dmonto'] ] )
    #cierre del archivo moviemientos.csv
    mifichero.close()


def update_by(id):
    pass