import random

class Jogo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def jogar(self, limite_superior):
        for contador in range(5, 0, -1):
            try:
                numero = int(input(f"Digite um número entre 0 e {limite_superior}\n"))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
            
            numero2 = random.randint(0, limite_superior)

            if numero == numero2:
                print(f'O {numero} é igual a {numero2}\nParabéns {self.nome}!')
                break
            else:
                print(f'O {numero} é diferente de {numero2}')
                print(f'Você tem {contador} tentativas restantes.')

jogador = input("Digite um nome: ")
idade = 0

try:
    idade = float(input("Digite sua idade: "))
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
except ValueError as e:
    print(f"Erro de execução: {e}")
    exit()

if idade <= 10:
    print('Nível fácil')
    Jogo(jogador, idade).jogar(10)
elif idade <= 18:
    print('Nível intermediário')
    Jogo(jogador, idade).jogar(50)
else:
    print('Nível difícil')
    Jogo(jogador, idade).jogar(100)

