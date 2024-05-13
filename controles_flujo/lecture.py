#if estructurado
edad:int=int(input("ingrese su edad_> "))
if edad >= 18:
    print("eres mayor")
else:
    print("eres menor de edad")

#if almacenado en variable
edad_dos:int=int(input("ingrese su edad_> "))
resupesta="eres mayor" if edad_dos >= 18 else "eres menor"
print(resupesta)


#controles de flujo que repiten codigo
#bucle for
vocales=["a","e","i","o","u"]
for i in range(0,5):
    print(vocales[i])

#segundo ejercicio
contador=0
for z in range(1,17):
    if z%2==0:
        contador+=1
        print(f"{z} es par numero {contador}")
#tercer ejercicio
oracion=input("ingresa una oracion-> ")
contador=0
for x in range(0,len(oracion)):
    if oracion[x] == "a":
        contador+=1
print(f"la contidad de vocales a que tengo es {contador}")
#otra manera
for n in "aeiou":
    print(n)
#otra manera
for i,j in enumerate("aeiou"):
#enumerate divide el string en dos partes una parte indice otra paRTE LETRA sin eso no funciona poner dos variables en el bucle for
    print(f"el idice es {i} la vocal es {j}")

#otro ejercicio
pida=input("ingrese dos o mas oraciones separados por comas-> ")
contador=0
for i,indice in range(0,len(pida)):
    if pida[i] == ",":
        contador+=1
print(f"la cantidad de comas es {contador}")