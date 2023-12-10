class Deposito():
    def __init__(self, valor):
        self.valor = valor
    
    def executar2(self, saldo):
        if self.valor:
            saldo += self.valor
            return saldo
        else:
            return None