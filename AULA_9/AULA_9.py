# prato = ()
# copo = ()

# def pratos():
#     print('Digite- 1 (pizza) 2 (macaronada) 3 (Lanche)')
#     escolha = input('Digite sua opção: ')
#     if escolha == '1':
#         prato = 'voce escolheu pizza'
#         print(prato)
#         return prato
#     elif escolha == '2':
#         prato = 'voce escolheu macaronada'
#         print(prato)
#     else:
#         print('erro')


# def driks():
#     print('Digite- 1 (cerveja) 2 (vinho) 3 (gin)')
#     escolha = input('Digite sua opção: ')
#     if escolha == '1':
#         copo= 'voce escolheu cerveja'
#         print(copo)
#     elif escolha == '2':
#         copo = 'voce escolheu vinho'
#         print(copo)
#     else:
#         print('erro')


# def restaurante():
#     print('Seja bem vindo ao restaurante')
#     pratos()
#     driks()
#     print(f'Voce escolheu {prato} e {copo}')
# restaurante()

# x = isinstance(5, int)
# print(x)

# x = isinstance(5, float)
# print(x)

# x = isinstance(5, str)
# print(x)

# dict = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 3,
#     'key4': 233215,
# }

# print(dict['key1'] , dict ['key2'])

# x =  dict['key1']

# print(x)

# notas_declaradas ={
# "José": 9,
# "Maria": 10,
# "Felipe":7
# }

# c = 2

# while c <=21:
#     nome_que_vai_entrar = input("digite o nome do aluno >> ")
#     nota = float(input("Digite a nota do aluno >> "))


#     if notas_declaradas.get(nome_que_vai_entrar):
#         print("Já existe o aluno", nome_que_vai_entrar)
#     else: 
#         notas_declaradas[nome_que_vai_entrar] = nota
#         print(notas_declaradas)

my_dict ={
    'key': 2,
    'key2': 5,
    'key3': 6
}

for chave, valor in my_dict.items():
    print(f'{chave}: {valor}')
