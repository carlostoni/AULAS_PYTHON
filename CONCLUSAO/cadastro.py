import tkinter as tk
from PIL import Image, ImageTk

def calcular_imc():
    
    
    nome = (entry_nome.get())
    altura = float(entry_altura.get()) / 100  # Convertendo altura de cm para metros
    


root = tk.Tk()
root.title("Cadastro")
root.geometry("800x640")  # Definindo o tamanho da janela


# Ícones
icon_peso = Image.open("weight_icon.png")
icon_peso = icon_peso.resize((100, 100))
icon_peso = ImageTk.PhotoImage(icon_peso)

icon_altura = Image.open("height_icon.png")
icon_altura = icon_altura.resize((100, 100))
icon_altura = ImageTk.PhotoImage(icon_altura)

# Título
label_titulo = tk.Label(root, text="Cadastro", font=("Arial", 36))
label_titulo.pack()

# Entrada de nome
frame_peso = tk.Frame(root)
frame_peso.pack()
label_icon_peso = tk.Label(frame_peso, image=icon_peso)
label_titulo = tk.Label(root, text="Nome", font=("Arial", 36))
label_icon_peso.pack(side=tk.LEFT)
entry_nome = tk.Entry(frame_peso, font=("Arial", 24), width=10)
entry_nome.pack(side=tk.LEFT)

# Entrada de altura
frame_altura = tk.Frame(root)
frame_altura.pack()
label_icon_altura = tk.Label(frame_altura, image=icon_altura)
label_icon_altura.pack(side=tk.LEFT)
entry_altura = tk.Entry(frame_altura, font=("Arial", 24), width=10)
entry_altura.pack(side=tk.LEFT)

# Botão para calcular IMC
botao_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc, font=("Arial", 24))
botao_calcular.pack()

# Resultado do IMC
label_resultado = tk.Label(root, text="", font=("Arial", 24))
label_resultado.pack()

# Tabela de valores de IMC
tabela = tk.Frame(root)
tabela.pack()


root.mainloop()
