#ejemplos de lectura de archivos csv con python

"""
with open('app_ingresos_gastos/data/movimientos.csv','r') as resultado:
    lectura = resultado.read()
    print(type(lectura))
"""
"""
resultado = open('app_ingresos_gastos/data/movimientos.csv','r')
lectura = resultado.readlines()
print(lectura)
"""
"""
import csv

mifichero = open('app_ingresos_gastos/data/movimientos.csv','r')
lectura = csv.reader(mifichero,delimiter=",",quotechar='"')
for items in lectura:
    print(items)

mifichero.close()    
"""
"""
import csv

mifichero = open('app_ingresos_gastos/data/movimientos.csv','a',newline="")
lectura = csv.writer(mifichero,delimiter=",",quotechar='"')
lectura.writerow(['05/02/2026','merienda','-16'])

mifichero.close()
"""
"""
from datetime import date

print(str(date.today()))

if str(date.today()) < '2026-02-06':
    print("es verdadero")
else:
    print("es falso")
"""
lista = ""
#comprobar si una lista esta vacia
#if len(lista) == 0:
#    print("lista esta vacia")

if lista:
    print("esta cargada")
else:
    print("lista esta vacia")
