from flask import Flask


#inicializar la varaible app con clask
app = Flask(__name__)

#inicializar parametros para el servidor de flask
#en mac:
#export FLASK_APP=main.py
#en windows:
#set FLASK_APP=main.py

#comando para ejecutar el servidor
#flask --app main run

#comando para ejecutar el servidor en otro puerto diferente al de default que es el 5000
#flask --app main run -p 5002

#comando para activar el servidor de flask en modo debug, no parar el servidor para ver los cambios
#flask --app main --debug run

@app.route('/hola')
def hola_mundo():
    return "Esto es una intro a flask, creo que mola, metira mola mucho"

@app.route('/frutas')
def list_frutas():
    list_fruta = ['platano','fresa','piña','uva','melon']
    return list_fruta

@app.route('/diccionario')
def list_dic():
    dic = [{'name':'Maria','email':'maria@email.com'},{'name':'Carlos','email':'carlos@email.com'}]
    return dic

#pasar parametro por ruta url
@app.route("/nombre/<name>")
def tu_nombre(name):
    print("valor: ",type(name))
    return f"hola {name} como estas"

@app.route("/num/<int:parametro>")
def cuadrado(parametro):
    #parametro = int(parametro)
    return f"El cuadrado de {parametro} es {parametro*parametro}"