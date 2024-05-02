"""tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)"""

def Nombres(nombre):
    Nombre = nombre
    print("Tu nombre es:  {}".format(Nombre))
    pass

def TipoSeguro(Seguro):
    seguro = Seguro
    print(f"El seguro que usted posse es {Seguro}")
    pass

def Edad():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Usted es mayor de edad")
    else:
        print("Usted es menor de edad")
    pass


