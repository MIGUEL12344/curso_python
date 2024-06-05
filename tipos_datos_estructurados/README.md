# TIPOS DE DATOS ESTRUCTURADOS (TDA- tipos de datos abstractos)
# listas
```python
lista= ["abel",20,5.2,.5,False,["texto",.2]]
```
# tupla 
```python
tupla=("fers",20,5.2,False,[])
```
# diccionarios o objetos
## los diccionarios almacenan los datos clave:valor
```python
diccionario={
    "azul":12,
    "rojo":13,
    "blanco":11
    "nombre":"filemon",
    "sexo":False
    }
```
- [!TIP]
- **observaciones:** que los tipos de datos estructurados pueden almacenar en su interior otros tipos de datos estructurdos
```python
lista_alumno=[
    {
        "nombre":"filemon"
        "edad":13
        "amigos":["no tiene"]
    },{
        "nombre":"cervantes"
        "edad":11 
        "amigos":["film","zzz"]
    },{
        "nombre":"carlos"
        "edad":15 
    }
] 
```
## metodos
### 1. convertir texto a lista
```python
# metodo list
texto="hola"
list(texto) #["h","o","l","a"]

#metodo split
texto="hola como estan"
texto.split(" o ,")
```
# agregar elementos de una lista
```python
#append - es el metodo que me permite agregar elemento al final de mi lista
lista=["hola"]
lista.append("mundo")
print(lista)
# metodo insert - es el metosd que me permite agregar elementos en cualquier ubicacion  de mi lista
lista_nombre=["carlos","geronimo","zrt"]
lista.insert(1,"ppp")
print(lista)
```

### eliminar elementos de una lista 
```python
#metodo pop() - es el metodo que elimina el ultimo elemento de una lista es el contrario de una lista
lista_nombre=["carlos","geronimo","zrt"]
lista.pop()
print(lista)
#primera manera - metod remove() - este metodo elimina el por nombre el elemento que coincida dentro de mi lista
lista_nombre=["carlos","geronimo","zrt"]
lista.remove("carlos")
print(lista)
#segunda opcion - metodo pop - al pasarle por parametro un indice este lo elimina de la lista
lista_nombre=["carlos","geronimo","zrt"]
lista.pop(0)
print(lista)
```

### 4. buscar un elemento en una lista
```python
lista_nombre=["carlos","geronimo","zrt"]
indice=lista.index("carlos")
print(lista[indice])

pertenencia="gert" in lista 
```
### 5. COMPARACION DE LISTAS
podemos hacer uso de los operadores de comparacion para comprar listas 
**Ejm:**
```python
compara=[1,2,3]>[1,2,4]
print(compara)
# salida:

```
## 6. cuidado con las copias

### 7. fe de erratas(actualizar listas)
```python
lista=[1,3,4,5,6]
lista[0]=2
print(lista)
alumnos=[
    {"nombre":"abel"
    "edad":15
    },
    {"nombre":"anthoni"
    "edad":29}
]
alumnos[0]["edad"]=10
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por definir"
print(alumnos)
```
### los metodos son herramientas son herramientas que sirven para manipular tipos de datos estructurados y tips de datos string
## 8. listas y diccionarios por comprencion
es una tecnica pythonica que nos permite crear listas y dicccionarios en una listas y diccionarios en una sola linea combinando.
bucles y deciciones.
>[!NOTE]
>**VLC** value loop condicion - valor, bucle, condicion
```python
#listas por comprencion
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",") if int(n)%2==0]
print(nueva_lista)
#diccionarios por conprencion sin vlc
lista_amigos=["abel","anthony","edith","ruth"]
diccionario_a={}
for _,v in enumerate(lista_amigos):
    diccionario_a[v]=len(v)
print(diccionario_a)
#aplicando el vlc
dicci={amigo:len(amigo) for amigo in lista_amigos}
print(dicci)
```