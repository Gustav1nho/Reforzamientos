lista = [int(input("ingrese un valor numerico:")), int(input("ingrese un valor numerico:")),
         int(input("ingrese un valor numerico:")), int(input("ingrese un valor numerico:")),
         int(input("ingrese un valor numerico:")), int(input("ingrese un valor numerico:")),
         int(input("ingrese un valor numerico:")), int(input("ingrese un valor numerico:")),
         int(input("ingrese un valor numerico:")), int(input("ingrese un valor numerico:"))]
print(lista)
suma_lista = [sum(lista)]
media = suma_lista[0] / 10
print(f"La suma de los valores elegidos es {suma_lista} con una media de {media}")
