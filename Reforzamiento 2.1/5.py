diccionario = {"Nombre" : "Gustavo", "Edad" : "20" , "Salario" : "2500"}
print(diccionario)
#Diccionario a lista
diccionario2 = list(diccionario)
print(diccionario2)
diccionario["Dni"] = "1234567"
print(diccionario)
del diccionario["Edad"]
print(diccionario)
#Convertimos a una lista el nuevo diccionario
diccionario3 = list(diccionario)
print(diccionario3)