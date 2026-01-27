class Persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni

    def mostrar_datos(self):
        print(f"Nombre:{self.nombre},Apellido:{self.apellido},DNI:{self.dni}")


class Estudiante(Persona):  
    def __init__(self, nombre, apellido, dni,carrera,year):
        super().__init__(nombre, apellido, dni)
        self.carrera = carrera
        self.year = year


    def mostrar_datos33(self):
       super().mostrar_datos()    
       print(f"Carrera: {self.carrera},Año:{self.year}") 
       print(self.nombre)

class Empleado(Estudiante):
    def __init__(self, nombre, apellido, dni, carrera, year,empresa,area,sueldo):
        super().__init__(nombre, apellido, dni, carrera, year)
        self.empresa=empresa
        self.area = area
        self.sueldo = sueldo

    def mostrar_datos(self):
        super().mostrar_datos33()
        print(f"Empresa:{self.empresa},Area:{self.area},Sueldo:{self.sueldo}")

persona = Empleado("Maria","Diaz","B6546546","Ingenieria de Software","2022","Keepcoding","programacion","35000")
persona.mostrar_datos()