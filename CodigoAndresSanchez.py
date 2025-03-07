class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.cursos = []

    def inscribirse(self, curso):
        self.cursos.append(curso)
        print(f"{self.nombre} se ha inscrito en el curso {curso}.")

    def listar_cursos(self):
        print(f"Cursos de {self.nombre}: {', '.join(self.cursos)}")

class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def dictar_clase(self):
        print(f"{self.nombre} está dictando una clase de {self.especialidad}.")

# Lógica principal
# Crear objetos
estudiante1 = Estudiante("Juan", 20, "A12345")
profesor1 = Profesor("María", 40, "Matemáticas")

# Interacciones
estudiante1.presentarse()
profesor1.presentarse()

estudiante1.inscribirse("Álgebra")
estudiante1.inscribirse("Programación")

estudiante1.listar_cursos()

profesor1.dictar_clase()
