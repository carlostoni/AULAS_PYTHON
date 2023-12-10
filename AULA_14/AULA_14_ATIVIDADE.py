#atividade 1
# Exercício 1: Remova o último elemento de uma lista e imprima a lista resultante.
# lista = [1, 2, 3, 4, 5]
# itens = len(lista)
# print(itens)
# n = lista.pop(itens-1)

# print(list)

#atividade 2
# Exercício 2: Remova o elemento de índice 2 de uma lista e imprima a lista resultante
# lista = [10, 20, 30, 40, 50]

# n = lista.pop(1)
# print(lista)

#atividade 3
# Exercício 3: Crie uma lista e implemente as operações pop().

# print('digite 5 numeros')
# lista = []
# for i in range(5):
#     numeros = int(input('digite 5 numeros'))
          
#     if i in range(5) :
#         lista.append(numeros)
#     print(lista)       
# else:
    
#  numeros1 = int(input('digite o numero do deseja remover'))
#  n = lista.pop(numeros1-1)  
#  print(lista)    
   
#atividade 4
# Exercício 4: Remova o primeiro elemento de uma lista e o último elemento usando pop() e imprima a lista resultante.
# lista = [1, 2, 3, 4, 5]
# print(lista)
# n = lista.pop(0)  
# n = lista.pop(3)  
# print(lista)

#atividade 5
# Exercício 5: Acesse os três primeiros caracteres de uma string.
# text = 'ola bom dia como vai?'
# char = text[:3]
# print(char)

#atividade 6
# Exercício 6: Acesse todos os elementos de uma lista, exceto o primeiro e o último.

# text = 'ola bom dia como vai?'
# itens = len(text)
# char = text[1:itens-1]
# print(char)

# <Desafio: Calculadora de Média >

#atividade 7
print('digite 3 notas')
lista = []

for i in range(3):
    numeros = float(input('digite as notas '))
          
    if i in range(3) :
        lista.append(numeros)
    
    print(lista) 
          
soma = sum(lista) /3
print(soma)
if soma >= 7:
    print('Aprovado')
elif soma >= 5:
    print('recuperacao')
else :
    print('reprovado')