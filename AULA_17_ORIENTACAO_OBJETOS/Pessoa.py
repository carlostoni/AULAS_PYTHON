class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Alicee", 300)


# Chamando o método saudacao do objeto
pessoa1.saudacao()
pessoa2.saudacao()