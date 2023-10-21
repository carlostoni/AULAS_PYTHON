# import tkinter as tk

# root = tk.Tk()
# def calculadora ():
  
#     print('Digite a opção da operacao a baixo')
#     print('1 - Adição')
#     print('2 - Subtração')
#     print('3 - Multiplição')
#     print('4 - Divisão')

#     opcao = int(input())

#     x = float(input('Digite o primeiro numero: '))
#     y = float(input('Digite o segundo numero: '))

#     if opcao == 1:
#       print(f'{x} + {y} =',x+y) 

#     elif opcao == 2:
#      print(f'{x} - {y} =',x-y)

#     elif opcao == 3:
#      print(f'{x} * {y} =',x*y)

#     elif opcao == 4:
#      print(f'{x} / {y} =',x/y)
#     else:
#      print("Opção invalida")

# calculadora()


def soma ():

  x = float(input('Digite o primeiro numero: '))
  y = float(input('Digite o segundo numero: '))
  print(f'{x} + {y} =',x+y) 


def subtração(): 
  x = float(input('Digite o primeiro numero: '))
  y = float(input('Digite o segundo numero: '))
  print(f'{x} - {y} =',x-y)

def multiplcao(): 
  x = float(input('Digite o primeiro numero: '))
  y = float(input('Digite o segundo numero: '))
  print(f'{x} * {y} =',x*y)

def divisao(): 
  x = float(input('Digite o primeiro numero: '))
  y = float(input('Digite o segundo numero: '))
  print(f'{x} / {y} =',x/y)

def calculadora ():
 
  print('Digite a opção da operacao a baixo')
  print('1 - Adição')
  print('2 - Subtração')
  print('3 - Multiplição')
  print('4 - Divisão')

  opcao = int(input())

  if opcao == 1:
    soma()
  elif opcao == 2:
   subtração()

  elif opcao == 3:
   multiplcao()

  elif opcao == 4:
    divisao()
  else:
      print("Opção invalida")
 
calculadora()

# root.mainloop()