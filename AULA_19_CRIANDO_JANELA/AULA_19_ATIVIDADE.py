# **Exercício 1: Janela Simples**

# Crie uma janela simples com o Tkinter que exiba o texto "Olá, Tkinter!" no centro da janela.


# import tkinter as tk

# def texto():
#     novo_texto = "Olá, Tkinter!"
#     label.config(text=novo_texto)
 
# janela = tk.Tk()

# label = tk.Label(janela, font=('arial', 80, 'bold'))
# label.pack()

# texto() 

# janela.mainloop()


# **Exercício 2: Janela Simples**

# Crie uma janela simples com o Tkinter que exiba o texto seu nome no centro da janela

from tkinter import *

janela = Tk()
janela.title('Janela')
janela.geometry('400x200+750+450')
lb  = Label(janela, text = 'Nome', )
lb.place(x = 180, y=90)

janela.mainloop()
