
# Comenzamos creando una clase llamada Tarea, con ella lo que hacemos es poder darles un 
# nombre y despues marcar como completada ya que por defecto la marcamos como pendien
class Tarea:
    def __init__(self, descripcion, completada=False):
        
        self.descripcion = descripcion
        self.completada = completada

# Pasamos a crear el método que nos permite marcar la tarea como completada
    def marcar_completada(self):
        
        self.completada = True
# Devuelve una representación legible de la tarea, mostrando su descripción y estado.
    def __str__(self):
        
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.descripcion} - Estado: {estado}"

# Inicializa el gestor de tareas con una lista vacía para almacenar las tareas.
class GestorTareas:
    def __init__(self):
        self.tareas = []

#   Agrega una nueva tarea a la lista de tareas pendientes.
    def agregar_tarea(self, descripcion):

        tarea_nueva = Tarea(descripcion)
        self.tareas.append(tarea_nueva)

#Marca una tarea como completada, dada su posición en la lista.
    def marcar_completada(self, posicion):

        try:
            tarea = self.tareas[posicion]
        except IndexError:
            print("La tarea especificada no existe.")
            return
        tarea.marcar_completada()

# Muestra todas las tareas pendientes en pantalla, numeradas y con su estado.
    def mostrar_tareas(self):

        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i+1}. {tarea}")

# Elimina una tarea de la lista, dada su posición.
    def eliminar_tarea(self, posicion):

        try:
            del self.tareas[posicion]
        except IndexError:
            print("La tarea especificada no existe.")

# A continuacion se configura la interface de usuario que aparecera en la consola para ejecutar el gestor de tareas
if __name__ == "__main__":
    gestor = GestorTareas()

    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la nueva tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == "2":
            posicion = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
            gestor.marcar_completada(posicion)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            posicion = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
            gestor.eliminar_tarea(posicion)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
