from Cuenta_Bancaria import Cuenta_Bancaria
from Cuenta_vip import Cuenta_vip
from Cuenta_plazo_fijo import Cuenta_plazo_fijo
import random

class CrearCuenta():
    def __init__(self, id, tipo_cuenta, titular,numerocuenta, fecha_apertura, fecha_vencimiento, saldo):
        self.id = id
        self.tipo_cuenta = tipo_cuenta
        self.titular = titular
        self.numerocuenta = numerocuenta
        self.fecha_apertura = fecha_apertura
        self.fecha_vencimiento = fecha_vencimiento
        self.saldo = saldo
