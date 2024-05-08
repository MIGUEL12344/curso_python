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
    print("El número ingresado no es válido.")

