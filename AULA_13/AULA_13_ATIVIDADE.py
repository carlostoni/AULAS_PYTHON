#atividade 1
# Exercício 1: Escreva um programa que verifique se a palavra "python" 
# está presente na string "Estou aprendendo Python".

# def busca():
#     palavra = ('Estou aprendendo Python')
#     if "Python" in palavra:
#         print(f'foi encontrada a palavra Python')
#     else:
#         print('nao foi encontrda a palavra')
# busca()

#atividade 2
# exercício 2: Escreva um programa que peça ao usuário para digitar 
# seu nome e verifique se o nome começa com a letra "A" (maiúscula ou minúscula).

# nome = input('Digite o seu nome: ')

# if nome.startswith("A"):
#     print('o nome começa com A')
# else:
#     print('o nome nao começa com A')

#atividade 3
# Exercício 3: Escreva um programa que peça ao usuário para digitar uma 
# senha e verifique se a senha contém pelo menos 8 caracteres.

# def verificar_senha():
#     nome = input('Digite o seu nome: ')
#     senha = input('Digite uma senha: ')
#     if len(senha) >= 8:
#      print('a senha tem 8 ou mais caracteres')
#     else :
#       print('a senha contem menos de 8 caracteres')
# verificar_senha()

#atividade 4
# Exercício 4: Escreva um programa que peça ao usuário para digitar 
# um número e verifique se o número é uma representação numérica (não contém 
# letras ou símbolos).

# def verificar_numero():
#     numero = input('Digite um numero: ')
#     if numero.isnumeric():
#         print("a string contém apenas numeros")
#     else:
#         print('a string contem algo mais que numeros')

    

# verificar_numero()

#atividade 5
# Exercício 5: Escreva um programa que peça ao usuário para digitar uma frase 
# e conte quantas vezes a letra "a" (maiúscula ou minúscula) aparece na frase.

nome = input('Digite o sua frase: ')
contador =nome.count('a')
print(contador)
