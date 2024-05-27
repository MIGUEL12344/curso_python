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