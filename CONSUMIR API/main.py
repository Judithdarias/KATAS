import requests as consulta

#https://api.exchangeratesapi.io/v1/latest?access_key=10935d34bd5fc02589b3a47913728eb1&base=EUR&symbols=USD,MXN,BTC

response = consulta.get('https://api.exchangeratesapi.io/v1/latest?access_key=10935d34bd5fc02589b3a47913728eb1&base=EUR&symbols=USD,MXN,BTC')

print('codigo http de respuesta: ',response.status_code)
print("cabecera: ",response.headers['content-type'])
print("encoding:",response.encoding)
print("respuesta en string",response.text)
print("respuesta en json",response.json())

#ejercicio 1, como capturamos en la consulta los rates
respuesta = response.json()#obtener la respuesta en formato de diccionario
print("rates: ",respuesta['rates'])
print("USD: ",respuesta['rates']['USD'])
print("MXN: ",respuesta['rates']['MXN'])
print("BTC: ",respuesta['rates']['BTC'])

