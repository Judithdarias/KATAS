import requests as consulta
from config import API_KEY
from model import *
from view import *

modelo = ModelCoins()
vista = ViewCoins()

try:
    modelo.getAllCoins(API_KEY)
except Exception as error:
    vista.getError(error)

vista.viewListCoins(modelo)  
#######################################################################################
moneda = vista.insertCoin()

while moneda == "" or not moneda.isalpha() or moneda not in modelo.valores_lista:
    moneda = vista.insertCoin()

try:
    modelo.updateExchanges(API_KEY,moneda)
    vista.viewRatesCoin(modelo)
except Exception as error:
    vista.getError(error)