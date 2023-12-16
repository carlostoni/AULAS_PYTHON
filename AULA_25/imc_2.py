import tkinter as tk

def calculadora_imc():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get()) / 100
    imc = peso / (altura ** 2)
    nivel_imc = obter_nivel_imc(imc)
    mensagem = f'Seu Imc é: {imc:.2f}\n Nivel: {nivel_imc}'
    label_resultado.config(text=mensagem)

    item = f"{name_label.cget('text')}: {entrada.get()}"
    item1 = f"{name_label1.cget('text')}: {entrada1.get()}"
    item2 = f"{name_label2.cget('text')}: {entry_altura.get()}"
    item3 = f"{name_label3.cget('text')}: {entry_peso.get()}"
    lista.insert(tk.END, item, item1, item2, item3)
    entrada.delete(0,tk.END)
    entrada1.delete(0,tk.END)
    entry_altura.delete(0,tk.END)
    entry_peso.delete(0,tk.END)

def obter_nivel_imc(imc):
    if imc < 18.5:
        return "Baixo (Abaixo do peso)"
    elif 18.5 <= imc < 25:
        return "Ideal (Peso normal)"
    elif 25 <= imc < 30:
        return "Alto (Sobrepeso)"
    else:
        return "Muito alto (Obesidade)"

janela = tk.Tk()
janela.title("Calculadora de IMC e Tabela de Valores de IMC")
janela.geometry("800x600")

name_label = tk.Label(janela, text = 'Nome ', font=('calibre',24, 'bold'))
entrada = tk.Entry(janela, font=('calibre',18, 'bold'), width=24)

name_label1 = tk.Label(janela, text = 'Idade ', font=('calibre',24, 'bold'))
entrada1 = tk.Entry(janela, font=('calibre',18, 'bold'), width=24)

name_label2 = tk.Label(janela, text = 'Altura ', font=('calibre',24, 'bold'))
entry_altura = tk.Entry(janela, font=('calibre',18, 'bold'), width=24)

name_label3 = tk.Label(janela, text = 'Peso ', font=('calibre',24, 'bold'))
entry_peso = tk.Entry(janela, font=('calibre',18, 'bold'), width=24)

lista = tk.Listbox(janela, font=('calibre',18, 'bold'), width=24)
btn = tk.Button(janela, text= 'SALVAR', command=calculadora_imc, font=("Arial", 24))

label_resultado = tk.Label(janela, text="", font=("Arial", 24))


name_label.grid(row=1,column=0)
entrada.grid(row=1,column=1)

name_label1.grid(row=2,column=0)
entrada1.grid(row=2,column=1)

name_label2.grid(row=3,column=0)
entry_altura.grid(row=3,column=1)

name_label3.grid(row=4,column=0)
entry_peso.grid(row=4,column=1) 

btn.grid(row=4,column=2)
lista.grid(row=7,column=1)

label_resultado.grid(row=7,column=2)
janela.mainloop()
