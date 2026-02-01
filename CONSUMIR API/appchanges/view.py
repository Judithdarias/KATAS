class ViewCoins():


    def insertCoin(self):
        moneda = input("Ingrese un codigo de moneda: ").upper()
        return moneda
    
    def viewListCoins(self,obj_modelo):
        print("Lista completa: ",obj_modelo.valores_lista)
        print("Total de codigo de monedas: ",len(obj_modelo.valores_lista)) 

    def viewRatesCoin(self,obj_modelo):
        print("rates: ",obj_modelo.respuesta['rates'])
        print("USD: ",round(obj_modelo.respuesta['rates']['USD'],2) )# 1.196001 - 1.19
        print("MXN: ",round(obj_modelo.respuesta['rates']['MXN'],2) )# 20.603608 - 20.60
        print("BTC: ",round(obj_modelo.respuesta['rates']['BTC'],2) )# 1.4266251e - 1.42
        print("Moneda Base: ",obj_modelo.respuesta['base'])
        print("Fecha de consulta: ",obj_modelo.respuesta['date'])

    def getError(self,err):
        print(err)