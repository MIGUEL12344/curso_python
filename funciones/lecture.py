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

#ejemplo de lambda
saludo=lambda n:f"hola, {n}"
print(saludo("zz"))

# crear un programa anonimo que reciba como parametro una lista de 5 numeros y retorne dos listas una con los numero pares y otra con numeros impares
numeros=[2,4,8,3,1]
pares=lambda pares:[i for i in numeros if i%2==0]
impares=lambda impares:[i for i in numeros if i%2!=0]
print(pares(numeros))
print(impares(numeros)) 
#map()
lista=[4,7,8,5,2]
nueva_lista=list(map(lambda x:x+1,lista)) #por defecto retorna una lista
print(nueva_lista)
#tengo una lista de alumnos que todos ellos aprobaron y pasan al tercer semestre, en mi lista todos estan con el segundo semestrew por lo que tendremos
#que crear una solucion que cambie el campo semestre de 2 a 3
lista_alumnos=[
    {"nombre":"abel",
     "edad":36,
     "semestre":2
     },{"nombre":"anthony",
     "edad":40,
     "semestre":2
     },{"nombre":"edith",
     "edad":50,
     "semestre":2
     }
]
def objeto(e):
    if "semestre" in e:
        e["semestre"]=e["semestre"]+1
    return [
         e
     ]
alumnos_actualizados=list(map(objeto,lista_alumnos)) #por defecto retorna una lista
print(alumnos_actualizados)
def nombre(i):
    i["carrera"]="apsti"
    return [
        i]
alumnos_zz=list(map(nombre,lista_alumnos))
print(alumnos_zz)
 #filter()
 #devolver los numeros pares de una lista
listas=[4,6,5,8,7,10,3,20]
nueva_list=list(filter(lambda x:x%2==0,listas))
print(nueva_list)

nueva_listas=list(filter(lambda x:x["edad"]<50,lista_alumnos))
print(nueva_listas)