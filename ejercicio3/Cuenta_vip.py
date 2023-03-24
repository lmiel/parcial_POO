from Cuenta_Bancaria import Cuenta_Bancaria

class Cuenta_vip(Cuenta_Bancaria):
    def __init__(self, id, nombre, fecha, numerocuenta, saldo, saldo_negativo_permitido):
        super()._init_(id, nombre, fecha, numerocuenta, saldo)
        self.saldo_negativo_permitido = saldo_negativo_permitido
        
    def transferir_dinero(self, cuenta_destino, cantidad):
        if cantidad > (self.saldo + self.saldo_negativo_permitido):
            print("No tienes suficiente saldo para transferir esa cantidad.")
        else:
            self.saldo -= cantidad
            cuenta_destino.saldo += cantidad
            print(f"Se ha transferido {cantidad} euros a la cuenta {cuenta_destino.numerocuenta}.")
