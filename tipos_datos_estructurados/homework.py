#1. crear una lista de 5 alumos alamacenados su nombre apellido y edad
#insertar al final de la lista los datos de geronimo
#eliminar de la lista si existe los datos de jose
#buscar y mostrar el alumno en la posicion 4 de la lista
# Lista inicial de alumnos
alumnos = [
    {'nombre': 'Jose', 'apellido': 'Perez', 'edad': 20},
    {'nombre': 'Ana', 'apellido': 'Garcia', 'edad': 22},
    {'nombre': 'Luis', 'apellido': 'Martinez', 'edad': 21},
    {'nombre': 'Maria', 'apellido': 'Lopez', 'edad': 23},
    {'nombre': 'Jose', 'apellido': 'Rodriguez', 'edad': 19}
]

# Insertar al final de la lista los datos de Geronimo
geronimo = {'nombre': 'Geronimo', 'apellido': 'Fernandez', 'edad': 24}
alumnos.append(geronimo)

# Eliminar de la lista si existe los datos de Jose
alumnos = [alumno for alumno in alumnos if alumno['nombre'] != 'Jose']

# Buscar y mostrar el alumno en la posición 4 de la lista
if len(alumnos) > 4:
    alumno_pos_4 = alumnos[4]
else:
    alumno_pos_4 = None

# Resultados
print("Lista de alumnos después de las operaciones:")
for i, alumno in enumerate(alumnos):
    print(f"{i+1}. {alumno}")

if alumno_pos_4:
    print("\nAlumno en la posición 4 de la lista:")
    print(alumno_pos_4)
else:
    print("\nNo hay alumno en la posición 4 de la lista.")
#2. crear una lista con los 4 diccionarios donde tendran los datos de sus mascotas (nombre,edad,sexo,raza)
#tareas
#mostrar lista con los 4 diccionarios
#editar el 3er registro y cambiarle la edad sin modificar la lista original 
#mostrar la listas original y luego 
dato_mascota=[
     {"nombre":"carlos",
      "edad":4,
      "sexo":"macho",
      "raza":"tsu shi"
     },{"nombre":"firulais",
      "edad":3,
      "sexo":"macho",
      "raza":"tsu shi"
     },{"nombre":"bryan",
      "edad":5,
      "sexo":"macho",
      "raza":"tsu shi"
     },{"nombre":"jose",
      "edad":7,
      "sexo":"macho",
      "raza":"tsu shi"
     }
 ]
def copia_datos_mascota():
     copia_datos=dato_mascota.copy()
     copia_datos[2]["edad"]=6
     print(copia_datos)
print(dato_mascota)
print()
copia_datos_mascota()
