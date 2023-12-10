<<<<<<< HEAD
class Saque():
    def __init__(self,valor):
        self.valor = valor

    def executar(self, saldo):
        if self.valor:
            saldo -= self.valor
            return saldo
        else:
            return None
=======
class Saque():
    def __init__(self,valor):
        self.valor = valor

    def executar(self, saldo):
        if self.valor:
            saldo -= self.valor
            return saldo
        else:
            return None
>>>>>>> 2dcac4952d542ed043f8b3e7cd3db907baa00a78
        