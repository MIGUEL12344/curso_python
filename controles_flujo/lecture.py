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
datos:str=input("ingrese dos o mas oraciones separados por comas-> ")
contador:int=0
for indice,letra in enumerate(datos):
    if letra == ",":
        print(f"""el numero de indices son:: {i}""")
        contador+=1
print(f"""la cantidad de comas es:: {contador}""")
#otro ejercicio
edad_usuario:int=int(input("ingrese su edad: "))
for edad in range(1,edad_usuario+1):
    print(edad)
#otro ejercicio
ultima_letra=""
for i in range(3):
    nombre:str=input("ingrese su nombre-> ")
    letras:str=nombre[-1]
    ultima_letra+=letras
print(ultima_letra)

#otro ejercicio
for i,letra in enumerate("aeiou"):
    print(letra * (i + 1))

#while 
#metodos de string
nombre="hola"
nombre.upper()#todo mayuscula
nombre="hola"
nombre.lower()#todo minuscula
nombre="hola"
nombre.capitalize()#primera letra mayuscula

#ejercicio while
notas=int(input("ingrese la cantidad de notas-> "))
cant=0
promedio_final=0
while cant < notas:
    print(f"ingrese nota {cant+1}")
    promedio=int(input(""))
    promedio_final+=promedio
    cant+=1
print(f"el promedio es {promedio_final//cant}")