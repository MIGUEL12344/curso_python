#return devuelve valores que podre hacer uso
# crear una funcion que retorne el numero 10, muestra por terminal si es par
#siempre que el valor que retorne mi funcion se utilize en mas sentencias u operaciones hacer uso de return 
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es impar")
#print solo muestra por terminal

#crear una funcion que me muestre el producto de dos numero
def producto(a,b):
    return a*b
#crear una funcion por parametro reciba un nombre y retorne un mensaje de bienvenida con el nombre
def mensaje(nombre):
    print(f"hola, {nombre}, bienvenido")

#crear una funcuion que reciba por parametro una lista de numeros y me devuleva el numero menor, mostrar por terminal el valor retornado por la funcion
lista=[1,2,3,4]
def Min(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
print(Min(lista))
#crear una funcion que reciba como parametro un nombre y la edad de una persona mi funcion debera retornar un diccion con as datos, luego por terminal el valor de retorno de mi funcion.
diccionario={}
def datos(nombre,edad):
    return{
        "nombre":nombre,
        "edad":edad
    }
print(datos(nombre="jota",edad=13))
#empaquetado y desempaquetado de objetos nominales
def alumnos(**kwargs):
    print(kwargs)
alumnos(nombre="miguel", apellido="largo",edad=30)
