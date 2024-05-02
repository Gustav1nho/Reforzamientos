"""14. Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)"""


from Modulo import Mi_Modulo

var1 = input("Ingrese su nombre: ")
var2 = input("Ingrese su  tipo de seguro: ")
nombre = Mi_Modulo.Nombres(var1)
seguro = Mi_Modulo.TipoSeguro(var2)
Edad = Mi_Modulo.Edad()