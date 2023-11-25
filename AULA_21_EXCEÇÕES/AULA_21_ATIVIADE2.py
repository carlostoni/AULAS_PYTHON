# Exercício 1
# Faça um programa que leia um número inteiro do usuário e imprima o seu quadrado.
#  Se o usuário digitar um valor não inteiro ou valor negativo, imprima uma mensagem de erro.

# def exercico1(a):
#     if(a >= 1):
#         print(a ** 2)
        
#     elif(a < 0):
#         raise ValueError("a nao pode ser negativa")
#     else:
#         raise ValueError("a nao pode ser zero")

# try:   
#     a = float(input("digite um a "))
#     if a.is_integer():
#        print("Esse eo resultado ao quadrado:")
#     else:
#         raise ValueError("a nao pode ser a quebrado")
#     exercico1(a)
# except ValueError as e:
#      print(f"erro de execucao {e} ")

# Exercício 2
# Faça um programa que leia dois números inteiros do usuário e imprima a sua soma. 
# Se o usuário digitar um número não inteiro, imprima uma mensagem de erro.

# try:
#     a = int(input('digite o primeiro numero ')) 
    
#     b = int(input('digite o segundo numero ')) 
#     print(a+b)
# except:
#     print('isso nao e um numero inteiro')

# Exercício 3
# Faça um programa que leia um número inteiro do usuário e imprima o seu fatorial. 
# Se o usuário digitar um número não inteiro ou menor que zero, imprima uma mensagem de erro.
# import math 

# try:
#     numero = int(input('digite um numero inteiro'))
#     if (numero<0):
#         raise ValueError('nao pode ser negativo')




# fatorial = 1

# for i in range(1, numero+ 1):
#     fatorial = fatorial * i 

# print('valor',fatorial)

# Exercício 4
# Faça um programa que leia um número inteiro do usuário e imprima o seu próximo primo. 
# Se o usuário digitar um número menor que 2, imprima uma mensagem de erro.

# def exercico4(a):
#     if a> 1:
#         for i in range(2, a):
#             if a % i == 0:
#                 print(a, 'não é primo')
#                 break
#         else:
#             print(a, 'é primo')
#             print(a/ a)
#     elif a == 0:
#         raise ValueError("nao pode ser zero")
#     elif a == 1:
#         print(a, 'é um')
        
#     else:
#         raise ValueError("nao pode ser negativa")
    


# try:   
#     a = int(input("digite um numero "))
    
#     exercico4(a)
# except ValueError as e:
#      print(f"erro de execucao {e} ")

# def eh_primo(numero):
#     if (numero<=1):
#         return False
    
#     for i in range(2,numero // 2 + 1):
#         if numero % i == 0:
#             return False # nao e primo
#         return True # e primo
    
# def proximo_primo(numero):
#     while True:
#         numero = numero + 1
#         if eh_primo(numero): # se for primo retorna o numero
#             return numero
# numero = int(input('digite um numero inteiro '))
# proximo = proximo_primo(numero)
# print('o proximo primo', proximo)

# Exercício 5
# Faça um programa que leia uma string do usuário e imprima o seu comprimento. 
# Se o usuário digitar uma string vazia, imprima uma mensagem de erro.



try:
    palavra = input("digite um palvra")
    x = len(palavra)
    if x <= 0:
        raise ValueError('a string esta vazia')
       
except:
    print(x) 
    print("VAZIA")