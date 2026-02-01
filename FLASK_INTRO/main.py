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

@app.route('/hola')
def hola_mundo():
    return "Hola mundo flask"