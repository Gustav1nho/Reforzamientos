"""12. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto (Por DNI)"""


class Adminitracion():
    def __init__(self, nombre, telefono, email, dni):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.dni = dni
        self.contacto = {"Nombre": self.nombre, "Telefono": self.telefono, "Email": self.email, "DNI": self.dni}

    def MisContactos(self):
        self.contactos = [self.contacto]
        print(self.contactos)

    def AñadirContacto(self, nombrex, telefonox, emailx, dnix):
        self.nuevoContacto = {"Nombre": nombrex, "Telefono": telefonox, "Email": emailx, "DNI": dnix}
        self.añadir = self.contactos.append(self.nuevoContacto)
        print(f"Mi nueva lista de contactos actualizada es: {self.contactos}")
    def BuscarPorDni(self):
        self.buscar = int(input("Introduce el dni de la persona que quieres buscar: "))
        if self.buscar == self.dni:
            print(f"El dni que buscaste es de {self.nombre}")
        else:
            print("No existe ese contacto")



Mis_Contactos = Adminitracion("Julian", 9321, "@gmail", 7172)
Mis_Contactos.MisContactos()
Mis_Contactos.AñadirContacto("Jose", 213, "@gmaail", 3213)
Mis_Contactos.BuscarPorDni()
