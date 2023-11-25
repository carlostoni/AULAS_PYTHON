

# try:

#     n =10

#     x = int(input('digite um numero'))

#     s = n/x
#     print(s)

# except:
#     print('nao pode dividir por 0')

# def divisao2(a, b):
   
#     if(b==0):
#         raise ZeroDivisionError("nao pode dividir por zero")
#     else:
#         total = a/b
#         print(total)
# try:
#     divisao2(4,0)
# except ZeroDivisionError as e:
#     print(f"Calculo nao permitido {e}") 


#exemplo 4 - idade
#se idade =>18 maior de idade
#senao 1 e 17  nemor
#idade <0 -- except (raise)
#idade ==0 -- except (raise)

def validaIdade(idade):
    if(idade >= 18):
        print("maior de idade")
    elif(idade > 0 and idade <18):
        print("menor de idade")
    elif(idade < 0):
        raise ValueError("idade nao pode ser negativa")
    else:
        raise ValueError("idade nao pode ser zero")
try:   
    idade = float(input("digite sua idade "))
    if idade.is_integer():
        validaIdade(idade)
    else:
        raise ValueError("idade nao pode ser numero quebrado")
    validaIdade(idade)
except ValueError as e:
    print(f"erro de execucao {e} ")