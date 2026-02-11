# Aplicación web de Ingresos/Gastos con Flask

Programa hecho en python con el framework flask

# Instalación

- crear un entorno en python, activalo y ejecutar el comando

```
pip install -r requirements.txt
```

la libreria utilizada es https://flask.palletsprojects.com


# Ejecución del programa

-inicializar parametros para el servidor de flask
-en mac:
```
export FLASK_APP=main.py
```
-en windows:
```
set FLASK_APP=main.py
```
-comando para ejecutar el servidor
```
flask --app main run
```

-comando para ejecutar el servidor en otro puerto diferente al de default que es el 5000
```
flask --app main run -p 5002
```

-comando para activar el servidor de flask en modo debug, no parar el servidor para ver los cambios
```
flask --app main --debug run
```