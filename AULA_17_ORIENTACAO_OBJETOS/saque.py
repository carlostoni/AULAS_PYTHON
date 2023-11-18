class Saque():
    def __init__(self,valor):
        self.valor = valor

    def executar(self, saldo):
        if self.valor:
            saldo -= self.valor
            return saldo
        else:
            return None
        