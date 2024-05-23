# sisitema de control de grass sintetico
# el usuario tiene un gras el cual administra de manera manual, 
#el usuario necesita que se automatize el proceso de la reserva y pago del alquiler, para lo cual solicita los siguientes casos de usos.
# - el usuario podra ver la lista de horarios disponibles.
# - el usuario podra reservar uno de los horarios disponibles.
# - el usuario podra pagar por el alquiler de la reserva realizada.
# - el usuario podra verificar su alquiler el cual le mostrara los detalles como la fecha, hora y costo del alquiler que realizo.
# Lista de horarios disponibles y sus costos
horarios_disponibles = ["10:00 - 12:00", "12:00 - 14:00", "14:00 - 16:00"]
costos = {
    "10:00 - 12:00": 50,
    "12:00 - 14:00": 60,
    "14:00 - 16:00": 55
}
reservas = []

def mostrar_horarios():
    print("Horarios disponibles:")
    cont = 0
    while cont < len(horarios_disponibles):
        horario = horarios_disponibles[cont]
        print(f"{cont + 1}. {horario} - ${costos[horario]}")
        cont += 1

def reservar_horario():
    mostrar_horarios()
    horario_index = int(input("Ingrese el número del horario que desea reservar: "))
    if horario_index < 1 or horario_index > len(horarios_disponibles):
        print("Horario no válido")
    else:
        horario = horarios_disponibles.pop(horario_index - 1)
        reservas.append(horario)
        print(f"Horario {horario} reservado con éxito.")

def pagar_reserva():
    if not reservas:
        print("No tiene reservas para pagar.")
        return
    print("Reservas disponibles para pagar:")
    cont = 0
    while cont < len(reservas):
        print(f"{cont + 1}. {reservas[cont]}")
        cont += 1
    horario_index = int(input("Ingrese el número del horario que desea pagar: "))
    if horario_index < 1 or horario_index > len(reservas):
        print("Reserva no válida")
    else:
        horario = reservas[horario_index - 1]
        costo = costos[horario]
        pago = int(input(f"El costo es ${costo}. Ingrese el monto del pago: "))
        if pago == costo:
            print(f"Pago de ${costo} realizado por la reserva del horario {horario}.")
        else:
            print("Monto de pago incorrecto.")

def verificar_alquiler():
    if not reservas:
        print("No tiene reservas.")
    else:
        cont = 0
        while cont < len(reservas):
            reserva = reservas[cont]
            costo = costos[reserva]
            print(f"Reserva: {reserva} - Costo: ${costo}")
            cont += 1

while True:
    print("\nOpciones:")
    print("1. Ver horarios disponibles")
    print("2. Reservar un horario")
    print("3. Pagar una reserva")
    print("4. Verificar alquileres")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        mostrar_horarios()
    elif opcion == 2:
        reservar_horario()
    elif opcion == 3:
        pagar_reserva()
    elif opcion == 4:
        verificar_alquiler()
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")