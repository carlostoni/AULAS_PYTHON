# Exercício 1: Lidando com NameError
# O código a seguir tenta calcular a média de uma lista de números, mas há um erro de NameError.
# Sua tarefa é corrigir o código utilizando try-except para lidar com o erro.
# Certifique-se de definir a lista de números corretamente dentro do bloco try.


# contador = 5
# lista = []

# while contador > 0:
#     numeros = int(input('Digite numeros inteiros: '))
#     contador -= 1
#     lista.append(numeros)
#     if numeros % 2 == 0:
#        lista.append(numeros)
#        print(lista)

#     else:
#         print()
          
    
# if contador <5 :
#     try:
#         soma = sum(lista)
#         media = soma / len(lista)
#         print("A média é:", media)
#     except NameError:
#            print('lista vazia')


# Exercício 2: Lidando com ValueError

# Exercício 2: Lidando com ValueError
# O código a seguir solicita ao usuário um número inteiro, mas pode gerar um ValueError se o usuário inserir uma string.
# Sua tarefa é corrigir o código utilizando try-except para lidar com o erro de ValueError.
# Informe ao usuário sobre o erro e peça para digitar um número inteiro válido.

# def exercico2(numero):
#     if(numero != False):
#         print('numero valido')
#     else:
#         raise ValueError("nao pode numero quebrado")

# try:
#     numero = float(input("Digite um número inteiro: "))
#     if numero.is_integer():
#         exercico2(numero)
#     else:
#          raise ValueError("isso e numero quebrado")
#     exercico2(numero)
    

# except ValueError as e:
#      print(f'isso nao e um numero inteiro {e}')

# Exercício 3: Lidando com AttributeError

# Exercício 3: Lidando com AttributeError
# O código abaixo tenta acessar um atributo 'comprimento' de uma string, o que causará um AttributeError.
# Sua tarefa é corrigir o código utilizando try-except para lidar com o erro.
# Informe ao usuário que o atributo não existe para essa string.


# try:
#     minha_string = "Olá, mundo!"
#     comprimento = minha_string.comprimento
#     print("O comprimento da string é:", comprimento)
# except:
#     print("erro")

# Exercício 4: Lidando com KeyError

# Exercício 4: Lidando com KeyError
# O código a seguir tenta acessar uma chave inexistente em um dicionário.
# Sua tarefa é corrigir o código utilizando try-except para lidar com o erro de KeyError.
# Informe ao usuário sobre a chave inexistente no dicionário.

# try:
#     meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
#     valor = meu_dicionario['d']
#     print("O valor é:", valor)
# except:
#     raise KeyError(valor)

# Exercício 5: Lidando com SyntaxError

# Exercício 5: Lidando com SyntaxError
# O código abaixo possui um erro de sintaxe que resultará em SyntaxError.
# Sua tarefa é corrigir o código utilizando try-except para capturar o erro de sintaxe.
# Informe ao usuário sobre o problema de sintaxe no código.

try:
    for i in range(5)
        print(i)
except:
    raise SyntaxError('erro')