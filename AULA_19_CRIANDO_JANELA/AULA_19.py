# import tkinter as tk
# from time import strftime

# def atualizar():

    
#     time =  strftime('%H:%M:%S')
#     label['text'] = time
#     janela.after(100, atualizar)


# janela = tk.Tk()
# janela.geometry('750x200')
# label = tk.Label(janela, text = 'Relogio')
# janela.configure(bg='blue')


# label = tk.Label(janela,font=('arial',80, 'bold'),bg= 'blue', fg= 'white')
# label.pack()


# time = tk.Label(janela, background='blue')
# time.pack(anchor='center')


# button= tk.Button(janela, text = 'clique aqui', command=atualizar)
# button.pack()

# janela.mainloop()

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()