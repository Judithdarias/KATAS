from flask import Flask,render_template


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

#realizar una ruta que dinamicamente pueda solicitar o realizar
#operaciones matematicas de suma,resta,multiplicacion y division
# debe ingresar dos parametros numericos y la operacion a realizar
@app.route("/calculador/<int:num1>/<int:num2>/<op>")
def operaciones_mates(num1,num2,op):#op suma,resta, multi,divi
    result=""
    if op == "suma":
        result = f"La suma es: {num1+num2}"
    elif op == "resta":
        result = f"La resta es: {num1-num2}"
    elif op == "multi":
        result = f"La multiplicación es: {num1*num2}"
    elif op == "divi":
        result = f"La división es: {num1/num2}"

    return result


@app.route("/html")
def mi_html():
    return render_template('hola.html',variable = "Hola esto es una variable desde metodo",nombre="Rolando",list_fruta = ['platano','fresa','piña','uva','melon'])

@app.route("/segunda")
def mi_html_segunda():
    return render_template('segunda.html')

#ejercicio
#al metodo operaciones_mates, agregamos una vista html y mostramos dentro de esta
#su resultado y los numeros y la operacion ejemplo: 10 + 5 = 15,
#si el usuario no pasa una operacion mostrar un mensaje 
#que diga debe ingresar la operacion : suma,resta,multi,divi

@app.route("/calculadora/<int:num1>/<int:num2>/<op>")
def operaciones_mates_tarea(num1,num2,op):#op suma,resta, multi,divi
    result=""
    if op == "suma":
        result = f"La suma es: {num1} + {num2} = {num1+num2}"
    elif op == "resta":
        result = f"La resta es: {num1} - {num2} ={num1-num2}"
    elif op == "multi":
        result = f"La multiplicación es: {num1} * {num2} = {num1*num2}"
    elif op == "divi":
        result = f"La división es: {num1} / {num2} = {num1/num2}"
    else:
        result = "debe ingresar la operacion : suma,resta,multi,divi"
    return render_template('tarea.html', resultado = result)