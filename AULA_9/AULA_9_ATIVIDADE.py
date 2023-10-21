# prato1 = []
# bebida1 = []

# def pratos():
#     print('Digite: 1 (pizza) 2 (macaronada) 3 (Lanche)')
#     prato = ('pizza', 'macarrao', 'lanche')

#     escolha = input('Digite sua opção: ')
#     if escolha == '1':
#         prato1.append(prato[0])
#         print('Voce escolheu',prato1)
#     elif escolha == '2':
#         prato1.append(prato[1])
#         print('Voce escolheu',prato1)
#     elif escolha == '3':
#         prato1.append(prato[2])
#         print('Voce escolheu',prato1)
#     else:
#         print('erro')


# def bebidas():
#     print('Digite: 1 (cerveja) 2 (vinho) 3 (gin)')
#     bebida = ('cerveja', 'vinho', 'gin')

#     escolha = input('Digite sua opção: ')
#     if escolha == '1':
#         bebida1.append(bebida[0])
#         print('Voce escolheu',bebida1)
#     elif escolha == '2':
#         bebida1.append(bebida[1])
#         print('Voce escolheu',bebida1)
#     elif escolha == '3':
#         bebida1.append(bebida[2])
#         print('Voce escolheu',bebida1)
#     else:
#         print('erro')
        
# def restaurante():
#     print('Seja bem vindo ao restaurante')
#     print('Escolha entre as opcoes abaixo')
#     pratos()
#     bebidas()
#     print(f'\nVoce escolheu {prato1} e {bebida1}')
# restaurante()

#atividade 2

dict = {
    '@': 'pizza',
    '#': 'macarrao',
    '$': 'lanche',
    '&': 'batata',
}
print('digite uma comida')
opcao = input()

for chave, valor in dict.items():
    if opcao == valor:
      print(f'o simbolo correspondente é: {chave}')
else:
   print("")

#atividade 3

# dict = {
#     'key': 'pizza',
#     'key1': 'macarrao',
#     'Key2': 'lanche',
#     'key3': 'batata',
#     'key4': 'arroz',
# }
# for chave, valor in dict.items():
#     if valor == valor:
#       print(f'o simbolo correspondente é: {dict.values}')
# else:
#    print("")
    