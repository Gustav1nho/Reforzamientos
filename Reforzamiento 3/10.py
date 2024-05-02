#Crear una clase llamada Alumno que tenga como atributos el nombre,
#edad y la nota final del alumno. Crear los métodos para inicializar sus
#atributos, otro para imprimirlos y un método para mostrar un mensaje
#con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
#alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)
class Alumno():
    Nombre = ""
    Edad = 0
    Nota_Final = 0
    def __init__(self,Nombre,Edad,Nota_Final):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Nota_Final = Nota_Final
        print(f"El alumno de nombre {self.Nombre} con  {self.Edad} años tiene una nota final de {self.Nota_Final}")
        if self.Nota_Final >= 11:
            print("-El alumno ha aprobado")
        else:
            print("-El alumno ha desaprobado")
Alumnos1 = Alumno("Gustavo",18,14)
Alumno2 = Alumno("Sebastian",19,16)
Alumno3 = Alumno("Gabriel",20,8)
