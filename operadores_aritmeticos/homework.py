
#area de un cuadrado
lado = float(input("Ingrese la longitud del lado del cuadrado: "))
area = lado * lado
print("El área del cuadrado es:", area)



#viaje de la tierra al sol

# Velocidad de la luz en metros por segundo
velocidad_luz = 299792458  

# Distancia promedio de la Tierra al Sol en metros
distancia_tierra_sol = 149.6e9  

# Calculando el tiempo de ida y vuelta
tiempo_ida_vuelta = (2 * distancia_tierra_sol) / velocidad_luz
tiempo_viaje=tiempo_ida_vuelta/60
# Imprimiendo el resultado
print("El tiempo de ida y vuelta al Sol a la velocidad de la luz es de aproximadamente", tiempo_viaje, "minutos.")

