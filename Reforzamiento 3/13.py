"""Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo) (si sueldo es superior a 4000 soles)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto."""
class Persona():
    Nombre = ""
    Edad = 0
    def __init__(self,nombre,edad):
        self.Nombre = nombre
        self.Edad = edad
        print(f"Su nombre es {self.Nombre} y tiene {self.Edad}")
class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo
        if self.sueldo >= 4000:
            self.sueldo = self.sueldo - self.sueldo * 0.1
            print("Usted debe pagar impuestos y su nuevo sueldo es {}".format(self.sueldo))
        else:
            print("Usted no paga impuestos, su sueldo se mantiene")
var1 = str(input("Inserte su nombre: "))
var2 = int(input("Inserte su edad: "))
var3 = int(input("Inserte su sueldo: "))
Empleado = Empleado(var1,var2,var3)

