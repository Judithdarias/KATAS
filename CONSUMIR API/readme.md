## Aplicación de consulta de api de valores de monedas internacionales

Programa hecho en python para recuperar el valor en monedas de euros y dolares

# Instalación
-Obtener el apikey en http://api.exchangeratesapi.io/
-Renombrear el fichero config_template.py a config.py
-Agregar dentro de config.py el apikey de esta manera
```
APIKEY="AQUI VA TU APIKEY"
```
## Instalacion de dependencias(librerias)
-Crear un entorno virtual de python con una de estas opciones

```
py -m venv entorno
python -n venv entorno
python3 -m venv entorno
```

-Activar el entorno e instalar los requerimientos
```
windows - .\entorno\Scripts\activate
mac o linux - source entorno/bin/activate

pip install -r requirements.txt
```