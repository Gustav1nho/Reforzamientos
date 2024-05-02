def leer_numero(ini, fin):
    numeros = list(range(ini, fin + 1))
    return numeros

def generador():
    ini = int(input("Ingresa el límite inferior: "))
    fin = int(input("Ingresa el límite superior: "))
    numeros = leer_numero(ini, fin)
    cuadrados = [num ** 2 for num in numeros]
    return cuadrados