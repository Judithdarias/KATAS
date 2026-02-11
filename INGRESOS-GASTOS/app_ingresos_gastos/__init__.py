from flask import Flask

app = Flask(__name__)

MOVIMIENTOS_FILE = 'app_ingresos_gastos/data/movimientos.csv'
LAST_ID_FILE = 'app_ingresos_gastos/data/last_id.csv'

from app_ingresos_gastos.routes import *

