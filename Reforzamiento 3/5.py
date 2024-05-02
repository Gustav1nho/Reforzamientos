var1 = int(input("Cuantos elementos quieres ingresar?: "))


def parametros(x):
    lista = []
    num_elementos = x
    for i in range(num_elementos):
        elementos = input("ingresa tu elemento {}: ".format(i + 1))
        lista.append(elementos)
    return lista
resultado_lista = parametros(var1)
print(resultado_lista)

var2 = int(input("Cuantos elementos quieres quitar?: "))

def quitar_lista(y):
    nueva_lista = resultado_lista
    quitar_elementos = y
    for i in range(quitar_elementos):
        num_elementos_quitar = int(input("Ingresa que elemento quieres quitar por index: "))
        del nueva_lista[num_elementos_quitar]
    print(nueva_lista)
    return nueva_lista

resultado_lista2 = quitar_lista(var2)
print(f"mi nueva lista es {resultado_lista2}")


