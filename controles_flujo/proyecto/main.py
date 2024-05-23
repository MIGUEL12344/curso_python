horarios_disponibles = ["10:00 - 12:00", "12:00 - 14:00", "14:00 - 16:00"]
costos = {
    "10:00 - 12:00": 50,
    "12:00 - 14:00": 60,
    "14:00 - 16:00": 55
}
reservas = []

while True:
    print("\nOpciones:")
    print("1. Ver horarios disponibles")
    print("2. Reservar un horario")
    print("3. Pagar una reserva")
    print("4. Verificar alquileres")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        # Mostrar horarios disponibles
        print("Horarios disponibles:")
        idx = 0
        while idx < len(horarios_disponibles):
            horario = horarios_disponibles[idx]
            print(f"{idx + 1}. {horario} - ${costos[horario]}")
            idx += 1

    elif opcion == 2:
        # Reservar un horario
        print("Horarios disponibles:")
        idx = 0
        while idx < len(horarios_disponibles):
            horario = horarios_disponibles[idx]
            print(f"{idx + 1}. {horario} - ${costos[horario]}")
            idx += 1
        horario_index = int(input("Ingrese el número del horario que desea reservar: "))
        if horario_index < 1 or horario_index > len(horarios_disponibles):
            print("Horario no válido")
        else:
            horario = horarios_disponibles.pop(horario_index - 1)
            reservas.append(horario)
            print(f"Horario {horario} reservado con éxito.")

    elif opcion == 3:
        # Pagar una reserva
        if not reservas:
            print("No tiene reservas para pagar.")
        else:
            print("Reservas disponibles para pagar:")
            idx = 0
            while idx < len(reservas):
                print(f"{idx + 1}. {reservas[idx]}")
                idx += 1
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

    elif opcion == 4:
        # Verificar alquileres
        if not reservas:
            print("No tiene reservas.")
        else:
            idx = 0
            while idx < len(reservas):
                reserva = reservas[idx]
                costo = costos[reserva]
                print(f"Reserva: {reserva} - Costo: ${costo}")
                idx += 1

    elif opcion == 5:
        # Salir
        print("Saliendo...")
        break

    else:
        print("Opción no válida, por favor intente de nuevo.")