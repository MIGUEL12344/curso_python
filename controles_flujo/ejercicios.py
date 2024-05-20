#primer ejercicio
#escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
#CREO MI VARIABLE DONDE PIDO EDAD
edad = int(input("Por favor, ingresa tu edad: "))
#SENTENCIO SI LA EDAD INGRESADA ES MAYOR O NO
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#segundo ejercicio 
#CREO UNA VARIABLE DONDE ALMACENO UNA CONTRASEÑA
contraseña_guardada = "contraseña"
#PIDO AL USUARIO QUE INGRESE UNA CONTRASEÑA
contraseña_ingresada = input("Por favor, ingresa la contraseña: ")
#SENTENCIO SI LA VARIABLE ES CORRECTA O NO 
if contraseña_guardada.upper() == contraseña_ingresada.upper():
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")

#TERCER EJERCICIO
#creo una variable donde pido que ingrese un numero
numero = int(input("Por favor, ingresa un número entero positivo: "))
#sentencio que solo trabaje con numeros positivos 
if numero > 0:
    print(*range(numero, -1, -1), sep=", ")
else:
    print("El número ingresado no es válido")

#tabla de multiplicar
for i in range(1,6):
    print(f"""\nla tabla del {i}\n""")
    for m in range(1,13):
        print(f"""{i}x{m}={i*m}""")
    
#tabla especifica
numero=int(input("ingrese numero de tabla->  "))
for i in range(numero,numero+1):
    print(f"""\n \tla tabla del {i}\n""")
    for m in range(1,13):
        print(f"""{i}x{m}={i*m}""")
#ejercicio while
condicion=True
while condicion:
    eval=input("desea continuar [s7n]:")
    if eval == "s":
        print("continuas en el bucle")
        continue
    else:
        print("se termino el programa")
        condicion=False
        break
#otro ejemplo de while
num=int(input("ingrese numero-> "))
cont=0
while cont < num :
    print("hola")
    cont+=1

