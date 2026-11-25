class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self._notas = []

    def agregar_nota(self, nota):
        self._notas.append(nota)

    def calcular_promedio(self):
        if len(self._notas) == 0:
            return 0
        return sum(self._notas) / len(self._notas)

    def mostrar_resumen(self):
        print(f"{self.nombre} ({self.carrera}) - Promedio: {self.calcular_promedio():.2f}")


e1 = Estudiante("Ana", "Ingeniería")
e1.agregar_nota(18)
e1.agregar_nota(16)
e1.agregar_nota(19)
print(e1.calcular_promedio())
e1.mostrar_resumen()

e2 = Estudiante("Luis", "Sistemas")
print(e2.calcular_promedio())
