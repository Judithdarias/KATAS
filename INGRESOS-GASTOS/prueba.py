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
import csv

mifichero = open('app_ingresos_gastos/data/movimientos.csv','r')
lectura = csv.reader(mifichero,delimiter=",",quotechar='"')
for items in lectura:
    print(items)