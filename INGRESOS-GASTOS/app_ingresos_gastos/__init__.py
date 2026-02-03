from flask import Flask

app = Flask(__name__)

from app_ingresos_gastos.routes import *

