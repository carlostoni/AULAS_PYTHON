##procurar

# cidade = 'São Carlos'
# endereco = 'Rua Cândido Padim, 25 - Vila Prado'
# completo = cidade + endereco
# print(cidade.startswith('São'))
# print(cidade.endswith('los'))

# print('Rua' in completo)
# print('Padim' not in completo)


## adicionar

# texto = 'Python é uma linguagem de programação. Python é simples. Python é organizado. Python é uma excelente linguagem.'
# print(texto.count('é'))
# print(texto.find('Python', 25,50))

# print(texto.rfind('lingua'))
# print(texto.index('é'))
# print(texto.rindex('é'))

# texto = 'Olá Mundo!'
# print(texto)
# texto_centro = texto.center(150)
# texto_centro_2 = texto.center(20,'.')
# texto_esquerda = texto.ljust(10)
# texto_direita = texto.rjust(150)
# print(texto_direita)
# print(f'**{texto_esquerda}*{texto_direita}**')


## separar
# nomes = "João Paulo/Maria Paula/Ana Beatriz/José Pedro"
# print(nomes.split('/'))
# #resultado: ['João Paulo', 'Maria Paula', 'Ana Beatriz', 'José Pedro']

frase = "Olá, mundo!"
if frase.startswith("Olá"):
    print("A frase começa com 'Olá'.")
else:
    print("A frase não começa com 'Olá'.")