## ATIVIDADE 1
# contador = 10
# while contador > 0:
#     print(contador)
#     contador -= 1
#     if contador < 1:
#      print("fogo")

## ATIVIDADE 2
# contador = 5
# lista =[]
# lista1 =[]
# while contador > 0:
#     numeros = int(input('Digite numeros inteiros: '))
#     contador -= 1
#     lista.append(numeros)
#     if numeros % 2 == 0:
#        lista1.append(numeros)
#        soma = sum(lista1)
    
# if contador <5 :
#        print('A Soma total é: ' ,soma)
# else:
#          print('nenhum numeo e par ')

## ATIVIDADE 3
# contador = 1
# numeros = int(input('Digite numeros inteiros: '))
# while contador < 11:
     
#      print(f'{numeros} * {contador} = ',numeros * contador)
#      contador += 1

# ## ATIVIDADE 4
# contador = 100
# while contador > 0:
     
#      print(f'{contador}')
#      contador -= 1

# Teste o Random: 
# ## ATIVIDADE 1

# import random

# aleatorio = random.randint(5,10)
# print(f'Esse é o numero {aleatorio}')

# ## ATIVIDADE 2
# import random

# contador = 0
# while contador < 3:
#      aleatorio = random.randint(0,10)
#      print(f'{aleatorio}')
#      contador += 1

import random
aleatorio = random.randint(10,30)

for aleatorio in range(20):
    if aleatorio < 3:
        print(aleatorio)
    else:
        print("Igual ou maior que 3")