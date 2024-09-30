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
#instanciar
cliente_1=banco("paco","gerte",43578034,5555,20) 
print(cliente_1.retirar(20))
print(cliente_1.saldo_inicial)
