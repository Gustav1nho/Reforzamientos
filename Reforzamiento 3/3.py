def suma_cuadrados(x):
    suma = 0
    while x > 0:
        suma = suma + (x%10)
        x = x//10
    return suma
x = int(input("Ingrese un numero: "))
print("La suma de los digitos del numero ingresado es: {}".format(suma_cuadrados(x)))

