#crear una clase banco
class banco:
#sus atributos seran nombre. apellidos, dni, numero de cuenta y saldo inicial
    def __init__ (self,nombre,apellido,dni,numero_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo_inicial=saldo_inicial
#como metodo podremos hecer deposito retirar dinero y ver estado de cuenta.
#metodo de depositar
    def depositar(self,cantidad):
        if cantidad > 0:
            self.saldo_inicial = self.saldo_inicial+ cantidad
            resultado=f"Depósito realizado con éxito. Nuevo saldo: {self.saldo_inicial}"
            return resultado
        
    def retirar(self,cantidad):
        if cantidad > 0:
            self.saldo_inicial = self.saldo_inicial- cantidad
            resultado=f"retiro realizado con éxito. Nuevo saldo: {self.saldo_inicial}"
            return resultado
        
    def estado_cuenta(self):
        return (f"Nombre y apellidos: {self.nombre} {self.apellido}\n"
                f"DNI: {self.dni}\n"
                f"Número de cuenta: {self.numero_cuenta}\n"
                f"Saldo actual: {self.saldo_inicial}")
#instanciar
cliente_1=banco("paco","gerte",43578034,5555,20) 
print(cliente_1.estado_cuenta())


# segundo ejercicio

# crear una clase banco
# sus atributos seran nombres y apellidos del pasajero dni numero de asiento fecha de viaje 
# sus metodos seran ingresar origen, ingresar destino, cancelar viaje, ver estado de pasaje


class Pasajero:
    def __init__(self, nombre, apellido, dni, numero_asiento, fecha_viaje, origen="", destino=""):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_asiento = numero_asiento
        self.fecha_viaje = fecha_viaje
        self.origen = origen
        self.destino = destino
        self.viaje_confirmado = True

    # Método para ingresar el origen
    def ingresar_origen(self, origen):
        self.origen = origen
        return f"\nOrigen ingresado: {self.origen}"

    # Método para ingresar el destino
    def ingresar_destino(self, destino):
        self.destino = destino
        return f"\nDestino ingresado: {self.destino}"

    # Método para cancelar el viaje
    def cancelar_viaje(self):
        self.viaje_confirmado = False
        return "\nViaje cancelado con éxito."


    # Método para ver el estado del pasaje
    def estado_pasaje(self):
        return (f"\nPasajero: {self.nombre} {self.apellido}\n"
                f"DNI: {self.dni}\n"
                f"Número de asiento: {self.numero_asiento}\n"
                f"Fecha de viaje: {self.fecha_viaje}\n"
                f"Origen: {self.origen}\n"
                f"Destino: {self.destino}\n"
                f"Estado del viaje: {'Confirmado' if self.viaje_confirmado else 'Cancelado'}")

# Ejemplo de uso
pasajero = Pasajero("Juan", "Pérez",12345678, "12A", "2024-10-15")
print(pasajero.ingresar_origen("galeras"))
print(pasajero.ingresar_destino("nazca"))
print(pasajero.estado_pasaje())
print(pasajero.cancelar_viaje())
print(pasajero.estado_pasaje())
