import tkinter as tk

#input usuario
#botao mostar uma nova tela

def add():
    item = entrada.get()
    lista.insert(tk.END, item)
    entrada.delete(0,tk.END)
    pass

janela = tk.Tk()
janela.geometry('500x500')

entrada = tk.Entry(janela)
entrada.pack()

lista = tk.Listbox()
lista.pack()

btn = tk.Button(janela, text= 'Clique', command=add)
btn.pack()


janela.mainloop()