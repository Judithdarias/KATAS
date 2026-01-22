from pantallas import *


"""
menu = Menu()
opcion = menu.bucle_pantalla()

if opcion =="partida":
    juego = Partida()
    juego.bucle_fotograma()
"""   
menu = Menu()
opcion = menu.bucle_pantalla()
if opcion =="partida":
    juego = Partida()
    juego.bucle_fotograma()
    resultado_partida = juego.finalizacion_juego()
    if resultado_partida:
        resultado = Resultado(resultado_partida)
        resultado.bucle_pantalla()