from Cuenta_Bancaria import Cuenta_Bancaria

class Cuenta_plazo_fijo(Cuenta_Bancaria):
    def __init__(self, id, nombre, fecha, numerocuenta, saldo, vencimiento):
        super()._init_(id, nombre, fecha, numerocuenta, saldo)
        self.vencimiento = vencimiento
        self.penalizacion = 0.05
    
    def retirar_dinero(self, cantidad, fecha_actual):
        if fecha_actual > self.fecha_vencimiento:
            self.saldo -= cantidad
            print("Se ha retirado {cantidad} euros de tu cuenta.")
        else:
            penalizacion = cantidad * self.penalizacion
            cantidad_total = cantidad + penalizacion
            print("Vas a retirar dinero antes de la fecha de vencimiento del plazo fijo")
            if cantidad_total > self.saldo:
                print("No tienes suficiente saldo para retirar esa cantidad.")
            else:
                self.saldo -= cantidad_total
                print("Se ha retirado {cantidad_total} euros de tu cuenta.")

