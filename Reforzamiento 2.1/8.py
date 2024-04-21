Departamentos_peru = {"Norte" : "Ica" , "Norte2" : "Tumbes", "Centro" : "Lima"  ,"Centro2" : "Anchash", "Sur" : "Arequipa", "Sur2" : "Tacna"}
print(Departamentos_peru)
#Borramos con del
del Departamentos_peru["Norte"]
print(Departamentos_peru)
#Con esto comprobamos que Ica ya no está presente
Departamentos_peru["Mi carrera universitaria"] = "Economia"
print(f"Mi nuevo diccionario actualizado es: {Departamentos_peru}")