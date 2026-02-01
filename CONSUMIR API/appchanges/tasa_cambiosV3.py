import requests as consulta
from config import API_KEY
from model import *

modelo = ModelCoins()
try:
    modelo.getAllCoins(API_KEY)
except Exception as error:
    print(error)

print("Lista completa: ",modelo.valores_lista)
print("Total de codigo de monedas: ",len(modelo.valores_lista))    
#######################################################################################

moneda = input("Ingrese un codigo de moneda: ").upper()

#controlar de que moneda  no sea vacio o numerico
while moneda == "" or not moneda.isalpha() or moneda not in modelo.valores_lista:
    moneda = input("Ingrese un codigo de moneda: ").upper()


try:
    modelo.updateExchanges(API_KEY,moneda)
    print("rates: ",modelo.respuesta['rates'])
    print("USD: ",round(modelo.respuesta['rates']['USD'],2) )# 1.196001 - 1.19
    print("MXN: ",round(modelo.respuesta['rates']['MXN'],2) )# 20.603608 - 20.60
    print("BTC: ",round(modelo.respuesta['rates']['BTC'],2) )# 1.4266251e - 1.42
except Exception as error:
    #aqui va si falla
    print(error)