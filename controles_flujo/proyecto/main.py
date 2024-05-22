# sisitema de control de grass sintetico
# el usuario tiene un gras el cual administra de manera manual, 
#el usuario necesita que se automatize el proceso de la reserva y pago del alquiler, para lo cual solicita los siguientes casos de usos.
# - el usuario podra ver la lista de horarios disponibles.
# - el usuario podra reservar uno de los horarios disponibles.
# - el usuario podra pagar por el alquiler de la reserva realizada.
# - el usuario podra verificar su alquiler el cual le mostrara los detalles como la fecha, hora y costo del alquiler que realizo.
dias_reservados=[]
costo_alquiler=40
fecha_reserva=[]
while True:
    print("\t GRASS SINTETICO")
    print(f""" :::HORARIOS DISPONIBLES:::
1. LUNES     ----PRECIO:: 40$
2. MARTES     ---PRECIO:: 40$
3. MIERCOLES ----PRECIO:: 40$
4. VERIFICACION DE RESERVAS""")
    opcion=int(input("ELIJA DIA EJEMPLO: ELIJA 1 PARA EL DIA LUNES->> "))
    if opcion == 1:
        nombre_uno=input("ingrese su nombre->> ")
        pago=int(input("ingrese pago->> "))
        hora_reserva=input("ingrese hora reserva ejemplo: 1:00am a 2:00am-> ")
        if pago == 40:
             print("realizo su reserva con exito")
             dias_reservados.append("lunes")
             fecha_reserva.append(hora_reserva)
             print(f"\n{nombre_uno} reservo el dia {dias_reservados} a horas de 4:00pm hasta 6:00pm\n ")
        else:
             print("\nel pago es insuficiente page completo para reservar\n")
    if opcion == 2:
        nombre_dos=input("ingrese su nombre->> ")
        pago=int(input("ingrese pago->> "))
        hora_reserva=input("ingrese hora reserva ejemplo: 1:00am a 2:00am-> ")
        if pago == 40:
             print("realizo su reserva con exito")
             dias_reservados.append("martes")
             fecha_reserva.append(hora_reserva)
             print(f"\n{nombre_dos} reservo el dia {dias_reservados} a horas de 1:00pm hasta 3:00pm\n ")
        else:
             print("\nel pago es insuficiente page completo para reservar\n")
    if opcion == 3:
        nombre_tres=input("ingrese su nombre->> ")
        pago=int(input("ingrese pago->> "))
        hora_reserva=input("ingrese hora reserva ejemplo: 1:00am a 2:00am-> ")
        if pago == 40:
             print("realizo su reserva con exito")
             dias_reservados.append("miercoles")
             fecha_reserva.append(hora_reserva)
             print(f"\n{nombre_tres} reservo el dia {dias_reservados} a horas de 8:00am hasta 10:00am\n ")
        else:
             print("\nel pago es insuficiente page completo para reservar\n")
    if opcion == 4:
         print(f"\nel horario que reservo fue el dia {dias_reservados} la hora de reserva fue de {fecha_reserva} el costo que pago fue de {costo_alquiler}s/\n")