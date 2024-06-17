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