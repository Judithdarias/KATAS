import sqlite3


def select_all():
    conexion = sqlite3.connect("data/movimientos.sqlite")
    cur = conexion.cursor()
    res = cur.execute("SELECT * FROM movements;")
    filas = res.fetchall()#datos de filas
    columnas = res.description#las columnas

    lista_diccionario=[]
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion +=1
        lista_diccionario.append(diccionario)   

    conexion.close()

    return lista_diccionario