var1 = input("ingresa texto de minimo 3 palbras: ")
def contador_palabras(texto):
    texto_sin_comas = texto.replace(",","")
    texto_list = texto_sin_comas.split()
    cantidad_palbras = len(texto_list)
    if cantidad_palbras < 3:
        print("Ingrese mas palabras")
    else:
        return cantidad_palbras
print("La cantidad de palabras que ingresaste es de: {}".format(contador_palabras(var1)))

