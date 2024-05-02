#Crear una clase que contenga dos métodos, uno que pida ingresar un
#nombre y apellido, un método para pedir su edad y otro método que lo
#imprima ambos resultados, pero estarán contenidos en un diccionario.
#Comprobar ambos métodos instanciado la clase respectivamente.
#Considerar en el constructor los valores necesarios.
class Datos:
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ")
        self.apellido = input("Ingresa tu apellido: ")
    def edad(self):
        self.edad = int(input("Ingrese su edad: "))
    def dicionario(self):
        self.datos = {"nombre" : self.nombre, "Apellido" : self.apellido, "Edad" : self.edad}
        print(f"Sus datos son: {self.datos}")

var1 = Datos()
var1.edad()
var1.dicionario()
