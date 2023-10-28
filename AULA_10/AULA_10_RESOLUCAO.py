#atividade 1
# def soma(N):
#     soma = 0
#     for i in range(1,N+1):
#         soma = soma +i
#         print(soma)
# n = int(input('Digite o numero'))
# soma(n)

#atividade 2
# def contador_de_letra(palavra,letra):
#     contador = 0
#     for char in palavra:
#         if char == letra:
#             contador+=1
#             print(contador)
# achados = contador_de_letra('coisa', 'i')

#atividade 3
# N = int(input('fat: '))
# resultado = 1
# count = 1

# while count <=N:
#     resultado *= count
#     count += 1

# print(resultado)

#atividade 4
# dicionario = {}
# dicionario ['chave'] = 'valor'
# dicionario ['chave1'] = 'valor1'
# dicionario ['chave2'] = 'valor2'
# dicionario ['chave3'] = 'valor3'

# print(dicionario)
#atividade 5
# produtos = {}

# for i in range(3):
#     nome_produto = input('Digite o nome do produto: ')
#     preco_produto = float(input('Digite o peço do produto: '))
#     produtos[nome_produto] = preco_produto

# print('Leads: ')

# for produto, preco in produtos.items():
#     print(f'{produto}: R$ {preco: 2f}')
