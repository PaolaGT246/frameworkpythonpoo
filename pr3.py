class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def retirarDinero(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Has retirado {cantidad}$. Ahora tienes {self.cantidad}$ en la cuenta.")
        else:
            print("No hay suficiente saldo para realizar la retirada.")

    def mostrar(self):
        print(f"Titular: {self.titular}\nSaldo: {self.cantidad}€")

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def setBonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def getBonificacion(self):
        return self.bonificacion

    def esTitularValido(self):
        edad = self.titular['edad']  
        return 18 <= edad < 25

    def retirarDinero(self, cantidad):
        if self.esTitularValido():
            super().retirarDinero(cantidad)
        else:
            print("No puedes retirar dinero porque el titular no es válido para esta cuenta joven.")

    def mostrar(self):
        print(f"Cuenta Joven\nTitular: {self.titular['nombre']} {self.titular['apellido']}\nBonificación: {self.bonificacion}%")
        super().mostrar()

titular = {'nombre': 'Paola', 'apellido': 'Gutierrez', 'edad': 22}

cuenta_joven = CuentaJoven(titular, 500, 5)

cuenta_joven.mostrar()

cuenta_joven.retirarDinero(100)

cuenta_joven.setBonificacion(10)
print(f"Bonificación actual: {cuenta_joven.getBonificacion()}%")
