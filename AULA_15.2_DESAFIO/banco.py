from saque import saque
from deposito import deposito

saldo = (float(1000.00))
a = saldo

contador = 0
while contador < 100:


    print('''
      Bem vindo
      qual operacao voce deseja fazer
      1 - saque
      2 - deposito 
      ''')

    lang = input()
    

    match lang:
        case "1":      
            valor = int(input('digite o valor que deseja sacar:'))
            b = valor
            
          
            saque(a,b)
            saldo -= saque
        case "2":
            valor = int(input('digite o valor que deseja depositar:'))
            b = valor
            
            deposito(a,b)
            
contador += 1 