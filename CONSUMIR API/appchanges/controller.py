import requests as consulta
from appchanges.config import API_KEY
from appchanges.model import *
from appchanges.view import *


class ControllerCoins:

    def __init__(self):
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