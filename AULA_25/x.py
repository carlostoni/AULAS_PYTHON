import tkinter as tk

janela = tk.Tk()
janela.geometry('600x500')

def add():
    item = f"{name_label.cget('text')}: {entrada.get()}"
    item1 = f"{name_label1.cget('text')}: {entrada1.get()}"
    item2 = f"{name_label2.cget('text')}: {entrada2.get()}"
    lista.insert(tk.END, item, item1, item2)
    entrada.delete(0, tk.END)
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)

name_label = tk.Label(janela, text='Username', font=('calibre', 10, 'bold'))
entrada = tk.Entry(janela)

name_label1 = tk.Label(janela, text='Email', font=('calibre', 10, 'bold'))
entrada1 = tk.Entry(janela)

name_label2 = tk.Label(janela, text='Phone', font=('calibre', 10, 'bold'))
entrada2 = tk.Entry(janela)

lista = tk.Listbox(janela)
btn = tk.Button(janela, text='Clique', command=add)

name_label.grid(row=0, column=0)
entrada.grid(row=0, column=1)
name_label1.grid(row=1, column=0)
entrada1.grid(row=1, column=1)
name_label2.grid(row=2, column=0)
entrada2.grid(row=2, column=1)
btn.grid(row=3, column=1)
lista.grid(row=4, column=1)

janela.mainloop()

import tkinter as tk
from tkinter import messagebox

def  create():
    item = name.entry.get()
    if item:
        items_listbox.insert(tk.END, item)
        name_entry.delete(0, tk.END)

def read():
    selecte_item = items_listbox.cursorselect()
    if selecte_item:
        item = items_listbox.get()
        massagebox.showinfo('selecionado', f' dados- {item}')
            if new_item:
                items_listbox(tk.END, selecte_item)



def upadate():
    pass

def delete():
    pass
root = tk.Tk()

root.mainloop()


import tkinter as tk
from tkinter import messagebox

def create():
    item = name_entry.get()
    if item:
        items_listbox.insert(tk.END, item)
        name_entry.delete(0, tk.END)

def read():
    selected_item = items_listbox.curselection()
    if selected_item:
        item = items_listbox.get(selected_item)
        messagebox.showinfo('Selecionado', f'Dados - {item}')

def update():
    selected_item = items_listbox.curselection()
    if selected_item:
        new_item = name_entry.get()
        if new_item:
            items_listbox.delete(selected_item)
            items_listbox.insert(selected_item, new_item)
            name_entry.delete(0, tk.END)

def delete():
    selected_item = items_listbox.curselection()
    if selected_item:
        items_listbox.delete(selected_item)

root = tk.Tk()

name_entry = tk.Entry(root)
name_entry.pack()

create_button = tk.Button(root, text="Create", command=create)
create_button.pack()

items_listbox = tk.Listbox(root)
items_listbox.pack()

read_button = tk.Button(root, text="Read", command=read)
read_button.pack()

update_button = tk.Button(root, text="Update", command=update)
update_button.pack()

delete_button = tk.Button(root, text="Delete", command=delete)
delete_button.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox

def  create():
    item = item_entry.get()
    if item:
        items_listbox.insert(tk.END, item)
        item_entry.delete(0, tk.END)

def read():
    selected_item = items_listbox.curselection()
    if selected_item:
        item = items_listbox.get(selected_item)
        messagebox.showinfo('Selecionado', f'Dados - {item}')
   


def update():
    selected_item = items_listbox.curselection()
    if selected_item:
        new_item = item_entry.get()
        if new_item:
            items_listbox.delete(selected_item)
            items_listbox.insert(selected_item, new_item)
            item_entry.delete(0, tk.END)

def delete():
    selected_item = items_listbox.curselection()
    if selected_item:
        items_listbox.delete(selected_item)

root = tk.Tk()
root.title('CRUD')
root.geometry('400x400')



item_label = tk.Label(root, text= 'Digite o seu E- mail', font=('arial',25, 'bold'))
item_label.pack()
item_entry = tk.Entry(root, width=50)
item_entry.pack()

btn_create = tk.Button(root, text='Salvar', command=create, width=15)
btn_create.pack()

items_listbox = tk.Listbox(root, width=50)
items_listbox.pack()

btn_read = tk.Button(root, text= 'Ler', command=read, width=15)
btn_read.pack()

btn_update = tk.Button(root, text ='Atualizar', command=update, width=15)
btn_update.pack()

btn_delete = tk.Button(root, text= 'Deletar', command=delete, width=15)
btn_delete.pack()



root.mainloop()
