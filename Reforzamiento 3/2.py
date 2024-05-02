var1 = int(input("Ingrese un primer numero: "))
var2 = int(input("Ingrese un segundo numero: "))
def cuadrados(x,y):
    if x > y:
        x , y = y, x
    for i in range(x,y):
        print(i**2)
print(f"Los cuadrados entre {var1} y {var2} son:")
cuadrados(var1,var2)