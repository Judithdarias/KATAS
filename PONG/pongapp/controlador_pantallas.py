from pantallas import *


class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.record = Record()
       

    def iniciar(self):
        valor  = self.menu.bucle_pantalla()
        if valor =="partida":
            self.partida.bucle_fotograma()
            resultado_partida = self.partida.finalizacion_juego()
            if resultado_partida:
                resultado = Resultado(resultado_partida)
                resultado.bucle_pantalla()
        elif valor =="record":
            record = Record()
            record.bucle_pantalla()