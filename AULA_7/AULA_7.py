# def saudacao():
#     print("Olá,")
#     print("Mundo!")

# for i in range(5):
#     if i < 3:
#         print("Menor que 3")
#     else:
#         print("Igual ou maior que 3")

## ESTRUTURA WHILE

# n= 1
# while n <= 10:
#     print(f'numero :{n} ')
#     n = n+ 1

# senha = int(input())
# while senha == 123456:
#     print("ok")
#     if senha == 123456:
#         print('liberado')
#     else:
#         print('negado')

# contador = 10
# while contador > 0:
#     print(contador)
#     contador -= 1
#     print("Contagem")

# import random
# x = random.random()
# print(x)

# import random

# chute = int(input('digite um numero '))
# numero = random.randint(0,1)

# while  chute == numero:
#     print('Digite um numero ente  0 e 10')
#     print(f'Voce acertou {numero}')
#     break
# if chute != numero:
#     print(f'vc perdeu! o numero é {numero}')


import random

aleatorio = random.randint(0,100)
print(f'Esse é o numero {aleatorio}')
multiplicacao = aleatorio * 10
print(f'Esse é o numero aleatório multiplicado {multiplicacao}')
