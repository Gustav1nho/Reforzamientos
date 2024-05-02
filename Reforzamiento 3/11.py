"""11. Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas."""
class Persona():
    Nombre = ""
    Edad = 0
    Sueldo= 0
    def __init__(self,nombre,edad,sueldo):
        self.Nombre = nombre
        self.Edad = edad
        self.Sueldo = sueldo
    def Datos(self):
        print(f"{self.Nombre} con edad de {self.Edad}, tiene un sueldo de {self.Sueldo}")
        if self.Edad <= 18:
            print(f"--{self.Nombre}, es menor de edad")
        else:
            print(f"--{self.Nombre}, es mayor de edad")
    def Sueldo_rar(self):
        if self.Edad <= 18:
            self.Sueldo = self.Sueldo + self.Sueldo*0.2
            print(f"--A {self.Nombre} Se le bonificará un 20% adicional por ser menor de edad y su sueldo es ahora {self.Sueldo} ")
        else:
            pass
            print(f"A {self.Nombre} se le mantendrá el sueldo de {self.Sueldo} ")


persona1 = Persona("Juan",17,2000)
persona2 = Persona("Alfonso",35,9850)

persona1.Datos()
persona1.Sueldo_rar()
persona2.Datos()
persona2.Sueldo_rar()