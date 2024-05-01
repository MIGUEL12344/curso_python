#comparacion de año
# Pedir al usuario que ingrese un año
año_usuario = int(input("Por favor ingresa un año: "))

# Obtener el año actual
año_actual = 2024

# Comparar si el año ingresado por el usuario es anterior al año actual
if año_usuario < año_actual:
    print(f"{año_usuario} es anterior al año actual.")
else:
    print(f"{año_usuario} no es anterior al año actual.")
    
 

#comparacion de edades 
edad1 = int(input("Ingrese la primera edad: "))
edad2 = int(input("Ingrese la segunda edad: "))
if edad1 == edad2:
    print("Las edades son iguales.")
else:
    print("Las edades son diferentes.")