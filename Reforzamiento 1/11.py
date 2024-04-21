var1 = float(input("Elige un numero: "))
print("Tu numero elegido es: {}".format(var1))
var2 = float(pow(var1, 5) / 10)
print("El nuevo valor convertido es: {}".format(var2))
if type(var2) is float:
    print("Tu numero es de tipo flotante")
else:
    print("Tu numero es entero")
