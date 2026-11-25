class Tarea:
    def __init__(self, titulo, prioridad="baja", completada=False):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = completada

    def marcar_completada(self):
        self.completada = True


class ListaTareas:
    def __init__(self, nombre):
        self.nombre = nombre
        self._tareas = []

    def agregar_tarea(self, tarea):
        self._tareas.append(tarea)

    def listar_pendientes(self):
        return [t.titulo for t in self._tareas if not t.completada]

    def contar_por_prioridad(self, prioridad):
        return len([t for t in self._tareas if t.prioridad == prioridad])


t1 = Tarea("Tomar agua", "alta")
t2 = Tarea("Llamar a Octavio")
t3 = Tarea("Investigar PC", "media", True)
t1.marcar_completada()

lt = ListaTareas("Planificación del día")
lt.agregar_tarea(t1)
print(lt.listar_pendientes())
lt.agregar_tarea(t3)
lt.agregar_tarea(t2)
print(lt.contar_por_prioridad("baja"))
