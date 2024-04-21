a = int(input("Ingrese un primer numero : "))
b = int(input("Ingrese un segundo numero : "))
c = int(input("Ingrese un tercer numero : "))
lista = a, b, c
print("tus numeros asignados son {}".format(lista))

modulo_a_3 = a % 3
modulo_a_5 = a % 5
modulo_a_7 = a % 7
Suma_mod_a = modulo_a_3 + modulo_a_5 + modulo_a_7
print("Suma de modulos de a con: {}".format(Suma_mod_a))

modulo_b_3 = b % 3
modulo_b_5 = b % 5
modulo_b_7 = b % 7
Suma_mod_b = modulo_b_3 + modulo_b_5 + modulo_b_7
print("Suma de modulos de b: {}".format(Suma_mod_b))

modulo_c_3 = c % 3
modulo_c_5 = c % 5
modulo_c_7 = c % 7
suma_mod_c = modulo_c_3 + modulo_c_5 + modulo_c_7
print("Suma de modulos de c: {}".format(suma_mod_c))

all_mod_plus = suma_mod_c + Suma_mod_a + Suma_mod_b

print("La suma de todos los modulos de todas las variables es {}".format(all_mod_plus))
