#Escribir una clase en Python que contenga un método que convierta un
#número entero en su cubo y contenga otro método que obtenga el
#cuadrado de ese resultado. El valor inicial de resultado deberá estar
#creado en el constructor. Considerar un método en la cual le pedirá al
#usuario ingresar un valor numérico.

class Op:
    def __init__(self,x):      # def __init__(self) , podemos omitir el valor x y canmbiar el self dato por:
        self.dato = x          #int(input("Ingresa un numero: "))
        self.cubo = self.dato ** 3
        self.cubodecubos = self.cubo ** 3
        print("El cubo de tu variable asignada es {} y su cubo es {}".format(self.cubo,self.cubodecubos))

var1 = int(input("Ingrese un valor numerico: "))
operacion = Op(var1)
