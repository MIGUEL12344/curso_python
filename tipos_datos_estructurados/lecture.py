# listas
lista_uno=["carlos","jeremi","cervantes"]
print(lista_uno[-1])
#diccionario
diccionario={"nombre":"cervantes","edad":12}
print(diccionario["nombre"])
#split trosear texto
texto="hola"
lista=list(texto)
lista2=[e for e in texto]
print(lista2)
#otro ejemplo
texto_largo="hola mundo"
nueva_lista=list(texto_largo)
print(nueva_lista)
#otro ejemplo del ejemplo
texto_largo="hola mundo"
nueva_lista=texto_largo.split(" ")
print(nueva_lista)
#otro ejemplo del ejemplo el ejemplo
texto_largo="hola mundo.mp4"
nueva_lista=texto_largo.split(".")
print(nueva_lista[-1])

#join metodo para unir elementos de una lista
texto_largo="hola .mundo"
nueva_lista=texto_largo.split(" ")
print(" ".join(nueva_lista))

#DATO PRIMITIVO
nombre="cesar"
print(id(nombre))
otro_nombre=nombre
print(id(otro_nombre))
#DATOS ESTRUCTURADOS
lista_original=[1,2,3,4]
copia_lista=lista_original

lista_original[-1]=15

#modificar lista sin afectar la original

lista=[1,7,2,4,3,6,5]
copia_lista=lista.copy()
copia_lista.sort()
print(lista,end="\n ordenada \n")
print(copia_lista)

#crear una lista de numeros enteros del siguiente texto

#listas por comprencion
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",") if int(n)%2==0]
print(nueva_lista)

#diccionarios por conprencion

lista_amigos=["abel","anthony","edith","ruth"]
diccionario_a={}
for _,v in enumerate(lista_amigos):
    diccionario_a[v]=len(v)
print(diccionario_a)

#aplicando vlc
dicci={amigo:len(amigo) for amigo in lista_amigos}
print(dicci)