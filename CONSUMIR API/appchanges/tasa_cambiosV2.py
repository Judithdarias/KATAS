import requests as consulta
from config import API_KEY

#http://api.exchangeratesapi.io/v1/latest?access_key=f457c5dbf867ac6c4dddfdfe388b206a
url = f'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}'
response = consulta.get(url)

if response.status_code != 200:
    raise Exception("Error en consulta http")

objeto_general = response.json()

valores_lista=[]

for k,v in objeto_general['rates'].items():
    valores_lista.append(k)

print("Lista completa: ",valores_lista)
print("Total de codigo de monedas: ",len(valores_lista))    
#######################################################################################

moneda = input("Ingrese un codigo de moneda: ").upper()

#controlar de que moneda  no sea vacio o numerico
while moneda == "" or not moneda.isalpha() or moneda not in valores_lista:
    moneda = input("Ingrese un codigo de moneda: ").upper()
                                                                                               
response = consulta.get(f'http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&base={moneda}&symbols=USD,MXN,BTC')
respuesta = response.json()#obtener la respuesta en formato de diccionario

if response.status_code == 200:
    print("rates: ",respuesta['rates'])
    print("USD: ",round(respuesta['rates']['USD'],2) )# 1.196001 - 1.19
    print("MXN: ",round(respuesta['rates']['MXN'],2) )# 20.603608 - 20.60
    print("BTC: ",round(respuesta['rates']['BTC'],2) )# 1.4266251e - 1.42
    #print(f"rates: {respuesta['rates']},\nUSD: {respuesta['rates']['USD']},\nMXN: {respuesta['rates']['MXN']},\nBTC: {respuesta['rates']['BTC']}" )
elif response.status_code >= 400:
    print("error: codigo:"+ respuesta['error']['code'] +" mensaje:"+ respuesta['error']['message'] )