# Desenvolva um jogo em Python onde o computador escolhe aleatoriamente um número e desafia o usuário a adivinhá-lo de acordo com o nível de dificuldade. Utilize a estrutura try-except para lidar com possíveis erros quando o usuário inserir uma entrada que não seja um número. Passos necessários:

# O jogo solicita o nome do jogador, que deve ser do tipo string.
# O jogo solicita a idade do jogador, que deve ser um número inteiro.
# Idade menor que 10 anos: nível de dificuldade fácil;
# Idade entre 11 e 18 anos: nível de dificuldade intermediário;
# Idade maior que 19 anos: nível de dificuldade difícil.
# O programa deve gerar aleatoriamente um número inteiro dentro de um intervalo definido, dependendo do nível de dificuldade selecionado:
# Nível fácil: sortear números de 0 a 10
# Nível intermediário: sortear números de 0 a 50
# Nível difícil: sortear números de 0 a 100
# Solicite ao jogador que insira um número como tentativa de adivinhar o número gerado pelo programa.
# Utilize try-except para garantir que o programa consiga lidar com possíveis erros quando o jogador inserir uma entrada que não seja um número válido (tanto para idade quanto para o número que está adivinhando).
# Verifique se o número inserido pelo jogador corresponde ao número gerado pelo programa.
# Caso o jogador adivinhe corretamente, exiba uma mensagem de parabéns e encerre o jogo. Caso contrário, informe se o número é maior ou menor do que a tentativa do jogador e dê outra chance para adivinhar.
# Repita o processo até que o usuário adivinhe o número correto ou atinja um limite máximo de tentativas.



import random
class Jogo:
    
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

    def nivel_facil(self):
        for contador in range(5,0,-1):
            numero = int(input("digite um numero entre 0 e 10 \n"))
            numero2 = random.randint(0, 10)
        
            if numero == numero2:
                print(f'o {numero} e igual {numero2} \nparabéns {jogador}')
                break
            else:
                print(f'O {numero} e diferente de {numero2}')
                print(f'voce tem {contador}')
                

    def nivel_intermediario(self):
        for contador in range(5,0,-1):
            numero = int(input("digite um numero entre 0 e 50 \n"))
            numero2 = random.randint(0, 50)

            if numero == numero2:
                print(f'o {numero} e igual {numero2} \n parabéns {jogador}')
                break
            else:
                print(f'O {numero} e diferente de {numero2}')
                print(f'voce tem {contador}')

    def nivel_dificil(self):
        for contador in range(5,0,-1):
            numero = int(input("digite um numero entre 0 e 100 \n"))
            numero2 = random.randint(0, 100)

            if numero == numero2:
                print(f' o {numero} e igual {numero2} \n parabéns {jogador}')
                break
            else:
                print(f'O {numero} e diferente de {numero2}')
                print(f'voce tem  {contador}')


jogador = input("digite um nome ")
idade = float(input("digite sua idade "))


facil = Jogo(jogador, idade)
intermediario= Jogo(jogador, idade)
dificil = Jogo(jogador, idade)


if idade > 0 and idade < 10:
    print('nivel facil')
    facil.nivel_facil()

elif idade > 10 and idade <= 18:
    print('nivel intermediariointermediario')
    intermediario.nivel_intermediario()
elif idade >= 19:
    print('nivel dificil')
    dificil.nivel_dificil()
elif(idade < 0):
        raise ValueError("idade nao pode ser negativa")
else:
        raise ValueError("idade nao pode ser zero")

try:   
    if idade.is_integer():
        Jogo(idade)
    else:
        raise ValueError("idade nao pode ser numero quebrado")
    Jogo(idade)
except ValueError as e:
    print(f"erro de execucao {e} ")