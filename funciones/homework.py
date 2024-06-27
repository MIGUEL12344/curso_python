#crear una funcion que reciba por argumentos n numeros y retorne una lista con los numeros para.
#forma iperativa
def lista(*numeros):
        lista_pares=[]
        for i in numeros:
            if i %2 == 0:
                lista_pares.append(i)
        return lista_pares
print(lista(2,4,5,3,8,16,20))
#por compresion
def listas(*numeros):
     return[n for n in numeros if n%2==0]
print(lista(2,4,5,3,8,16,20))

#crear tres funciones para los siguientes caso 
#calcular el numero menor
#calcular el numero mayor
#calcular la suma de todos los numeros
#se le pasra por argumentos n numeros
def min(*args):
     menor=args[0]
     for n in args:
          if n<menor:
               menor=n
     return menor
def max(*args):
     mayor=args[0]
     for n in args:
          if n>mayor:
               mayor=n
     return mayor
def sum(*args):
     suma=0
     for n in args:
          suma+=n
     return suma
valores=4,5,6,7,8,2,1
print(min(*valores))
print(max(*valores))
print(sum(*valores))

#tarea
# Crear una lista de alumnos
alumnos = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 20, "celular": "1234567890", "email": "juan.perez@example.com"},
    {"nombre": "Ana", "apellido": "Gómez", "edad": 22, "celular": "0987654321", "email": "ana.gomez@example.com"},
    {"nombre": "Luis", "apellido": "Martínez", "edad": 24, "celular": "1122334455", "email": "luis.martinez@example.com"}
]

# Actualizar los registros con el campo "programa de estudios"
for alumno in alumnos:
    alumno["programa de estudios"] = "enfermería"

# Actualizar la edad del segundo registro a 50 años
if len(alumnos) > 1:
    alumnos[1]["edad"] = 50

# Imprimir la lista de alumnos actualizada
for alumno in alumnos:
    print(alumno)