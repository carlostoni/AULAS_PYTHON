import tkinter as tk

janela = tk.Tk()
janela.geometry('600x500')

def add():
    item = entrada.get()
    item1 = entrada1.get()
    item2 = entrada2.get()
    lista.insert(tk.END, (item, item1, item2))
    entrada.delete(0, tk.END)
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)

name_label = tk.Label(janela, text='Username', font=('calibre', 10, 'bold'))
entrada = tk.Entry(janela)

name_label1 = tk.Label(janela, text='Username', font=('calibre', 10, 'bold'))
entrada1 = tk.Entry(janela)

name_label2 = tk.Label(janela, text='Username', font=('calibre', 10, 'bold'))
entrada2 = tk.Entry(janela)

lista = tk.Listbox(janela)
btn = tk.Button(janela, text='Clique', command=add)

name_label.grid(row=0, column=0)
entrada.grid(row=0, column=1)
name_label1.grid(row=1, column=0)
entrada1.grid(row=1, column=1)
name_label2.grid(row=2, column=0)  # Adjusted the row index
entrada2.grid(row=2, column=1)  # Adjusted the row index
btn.grid(row=3, column=1)  # Adjusted the row index
lista.grid(row=4, column=1)  # Adjusted the row index

janela.mainloop()
