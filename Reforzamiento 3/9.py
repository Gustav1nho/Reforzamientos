#Crear una clase llamada círculo que contenga radio en su constructory
#que contenga un método área que devuelva el área de un círculo.
#Aplicar excepciones en caso no se ingrese un dato tipo numérico.

#Crear adicionalmente un método que devuelva el perímetro del círculo.
#Instanciar la clase respectivamente para dos diferentes radios.
#Habrá un método donde pedirá el radio del círculo.
#Instanciar mínimo 2 veces la clase y mostrar resultados por consola.

class Circulo:
    def __init__(self):
        self.pi = 3.14159
        try:
            self.r = int(input("Ingrese un radio: "))
        except ValueError:
            print("Solo puede insertar una variable numerica!!")

    def Area(self):
         self.area = self.pi * self.r ** 2
    def Perimetro(self):
        self.perimetro = self.pi * self.r*2
        print(f"Tu area es {self.area} y tu perimetro {self.perimetro}")
class Circulo2(Circulo):
    pass


circulovic = Circulo()
circulovic2 = Circulo2()
try:
    circulovic.Area()
    circulovic2.Area()
    circulovic.Perimetro()
    circulovic2.Perimetro()
except AttributeError:
    print(f"Su valor no puede ser atribuido, inserte otra variable!")





