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

