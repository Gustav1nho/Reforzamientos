lista = {"Nombre" : "Gustavo", "Apellido" : "Garcia" , "Residencia" : "Callao"}
print("la lista es: {}".format(lista))

#Se puede usar 2 metodos para los keys de la lista: with list and list(nombredeltrabajo.keys)
lista_keys = list(lista)
print("{}".format(lista_keys))

lista_key_2 = list(lista.keys())
print("{}".format(lista_key_2))

#Si deseamos los resultados de las keys de la lista usamos "list(lista.value)

lista_key_3 = list(lista.values())
print("{}".format(lista_key_3))

#Todos los items de la lista
lista_items = list(lista.items())
print("{}".format(lista_items))