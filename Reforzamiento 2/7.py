lista_cursos = ["Macroeconomia", "Microeconomia", "Economia", "Calculo", "Estadistica", "Finanzas"]
print("Los cursos que lleve a lo largo de la universidad son: {}".format(lista_cursos))
lista_cursos.append("Matematica")
lista_cursos.append("Redaccion")
lista_cursos.append("Algebra Lineal")
lista_cursos.append("Macro Dinamica")
lista_cursos.append("Econometria")
lista_cursos.append("Control optimo")
print("la nueva lista de cursos es: {}".format(lista_cursos))
lista_cursos.remove("Redaccion")
lista_cursos.remove("Algebra Lineal")
print("La nueva lista con valores removidos es: {}".format(lista_cursos))
lista_cursos.append("Macroeconomia")
lista_cursos.append("Macroeconomia")
print("Nueva lista con cursos repetidos: {}".format(lista_cursos))
print("La cantidad de veces que se repide macreconomia es: {}".format(lista_cursos.count("Macroeconomia")))

del lista_cursos[0]
print("Lista actualizada con el primer elemento eliminado: {}".format(lista_cursos))