import sqlite3 

def select_all():
    """
    diccionario=[
        {"fecha":"2026-02-01","concepto":"Nomina","monto":2800},
        {"fecha":"2026-02-02","concepto":"mercado","monto":-100},
        {"fecha":"2026-02-05","concepto":"Desayuno","monto":-12},
        {"fecha":"2026-02-06","concepto":"Almuerzo","monto":-25},
    ]
"""
    conexion = sqlite3.connect("data/movimientos.sqlite")
    cur = conexion.cursor()
    res = cur.execute("SELECT * FROM movements;")
    filas = res.fetchall()#datos de columnas 
    columnas = res.description#las columnas

    lista_diccionario=[]
    for f in filas:
        posicion = 0 
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion += 1
        
        lista_diccionario.append(diccionario)

    return lista_diccionario