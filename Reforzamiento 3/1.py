var1 = int(input("Ingrese un numero: "))
var2 = int(input("Ingrese otro numero: "))
def suma_digitos(x):
    suma = 0
    while x > 0:
        suma = suma + (x%10)
        x = x//10
    return suma
print(suma_digitos(var1))
print(suma_digitos(var2))
if suma_digitos(var1) > suma_digitos(var2):
    print("Su primer numero es mayor ")
elif suma_digitos(var1) == suma_digitos(var2):
    print("La suma de sus digitos son iguales")
else:
    print("Su segundo numero es mayor")

if suma_digitos(var1) < 10:
    print("La suma de los digitos de su primer numero es menor a 10")
else:
    pass
if suma_digitos(var2) < 10:
    print("La suma de digitos de su segundo numero es menor a 10")
else:
    pass
