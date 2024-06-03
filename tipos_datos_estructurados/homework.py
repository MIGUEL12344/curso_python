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
#un empresario de alquiler de autos desea guardar en una base 
#de datos la informacion de sus veiculos,procesos que desea automatizar con sus sistema informatico
#las acciones que puede realizar el empresario son ver las listas de autos que tiene, podra tambien 
#actualizar la lista y agregar un nuevo veiculo
###
#casos de uso

###1
#yo como empresario
#quiero ver la lista de autos disponibles en mi inventario
#para ver el estado actual de mi stock

###2
#yo como empresario 
#quiero agregar un nuevo veiculo a la lista de autos
#para ampliar mi inventario y ofrecer mas opciones a mis clientes

###3
#yo como empresario
#quiero actualizar la informacion de un veiculo existente en mi liata 
#para asegurarme que los datos esten correctos y actualizados.

#programacion
##ver las lista de los autos
autos =[
    {'1.marca': 'Toyota', 'modelo': 'Corolla', 'año': 2020, 'matricula': 'XYZ123'},
    {'2.marca': 'Honda', 'modelo': 'Civic', 'año': 2019, 'matricula': 'ABC456'}]
def mostrar_autos():
    for ordenado in autos:
             print(ordenado)
while True:
    print("\nOpciones:")
    print("1. Ver lista de autos")
    print("2. Agregar un nuevo vehículo")
    print("3. Actualizar información de un vehículo")
    print("4. Salir")
    opcion=int(input("ingrese una opcion"))
    if opcion == 1:
         mostrar_autos()
#agregar nuevo dato a lista
    if opcion == 2:
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        año = int(input("Ingrese el año del auto: "))
        matricula = input("Ingrese la matrícula del auto: ")
        nuevo_auto = {'marca': marca, 'modelo': modelo, 'año': año, 'matricula': matricula}
        autos.append(nuevo_auto)
        print("\nAuto agregado exitosamente.")
#actualizar lista de autos
    if opcion == 3:
             mostrar_autos()
             opcion=int(input("\nIngrese el número del auto que desea actualizar\n"))
             if opcion == 1:
                 marca = input("Ingrese la nueva marca del auto->> ")
                 modelo = input("Ingrese el nuevo modelo del auto->> ")
                 año = input("Ingrese el nuevo año del auto->> ")
                 matricula = input("Ingrese la nueva matrícula del auto->> ")
                 if marca:
                     autos[0]['1.marca'] = marca
                 if modelo:
                     autos[0]['modelo'] = modelo
                 if año:
                     autos[0]['año'] = int(año)
                 if matricula:
                     autos[0]['matricula'] = matricula
    if opcion == 4:
         print("saliendo....")
         break