class Cuenta_Bancaria():
    def __init__(self,id, nombre, fecha, numerocuenta, saldo):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.numerocuenta = numerocuenta
        self.saldo = saldo


    #creamos la funcion para retirar dinero
    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            print("No tiene suficiente dinero en su cuenta")
        else:
            self.saldo -= cantidad
            print("Se ha retirado {cantidad} euros de tu cuenta.")

    #creamos la funcion para ingresar dinero
    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        print("Se ha ingresado {cantidad} euros en tu cuenta.")

    #creamos la funcion para transferir dinero
    def transferir_dinero(self, cantidad, cuenta_destino):
        if cantidad > self.saldo:
            print("No tiene suficiente dinero en su cuenta")
        else:
            self.saldo -= cantidad
            cuenta_destino.saldo += cantidad
            print("Se ha transferido {cantidad} euros de tu cuenta a la cuenta de {cuenta.numero_cuenta}")

