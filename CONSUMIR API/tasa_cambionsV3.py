from appchanges.model import ModelCoins
from appchanges.config import * 

def test_allcoints():
    objetoMoneda = ModelCoins()# creando un objeto de la clase o instanciando la clase
    objetoMoneda.getAllCoins(API_KEY)
    lista = objetoMoneda.valores_lista
    assert lista != None

def test_exchange():
    cambio = ModelCoins()
    cambio.updateExchanges(API_KEY,"EUR")
    assert cambio.respuesta != None