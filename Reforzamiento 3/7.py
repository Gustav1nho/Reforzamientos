# PRegunta 7. Crear una clase en python que contenga un método que revierta una
#cadena de palabras:
#Input: "Hola Pythonista, seguimos adelante"
#Output: "adelante seguimos Pythonista Hola"
#Llamarlo mínimo 2 veces y mostrar el resultado por consola.

class Reverb():
    def __init__(self):
        self.ingresar = input("Ingrese un texto: ")
        self.reverse = ""
        self.decision = input("Deseas hacer reversa a tu palabras? Si o No: ")
        if self.decision == "Si":
            for letra in self.ingresar:
                self.reverse = letra + self.reverse
            print(self.reverse)
        else:
            print(f"Tus palabras son: {self.ingresar}")
Texto = Reverb()

