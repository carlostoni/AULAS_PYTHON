# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:

    x = int(input('digite um numero ')) 
    print(x)

except:
    print('isso nao e um numero inteiro')