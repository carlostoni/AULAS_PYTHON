import tkinter as tk
from PIL import Image, ImageTk

def calcular_imc():
    
    
    peso = float(entry_peso.get())
    altura = float(entry_altura.get()) / 100  # Convertendo altura de cm para metros
    imc = peso / (altura ** 2)
    nivel_imc = obter_nivel_imc(imc)
    mensagem = f"Seu IMC é: {imc:.2f}\nNível: {nivel_imc}"
    label_resultado.config(text=mensagem)

def obter_nivel_imc(imc):
    if imc < 18.5:
        return "Baixo (Abaixo do peso)"
    elif 18.5 <= imc < 25:
        return "Ideal (Peso normal)"
    elif 25 <= imc < 30:
        return "Alto (Sobrepeso)"
    else:
        return "Muito alto (Obesidade)"

root = tk.Tk()
root.title("Calculadora de IMC e Tabela de Valores de IMC")
root.geometry("800x640")  # Definindo o tamanho da janela

menubar = tk.Menu()

filemenu = tk.Menu(menubar)
filemenu.add_command(label="Cadastro")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

# Ícones
icon_peso = Image.open("weight_icon.png")
icon_peso = icon_peso.resize((100, 100))
icon_peso = ImageTk.PhotoImage(icon_peso)

icon_altura = Image.open("height_icon.png")
icon_altura = icon_altura.resize((100, 100))
icon_altura = ImageTk.PhotoImage(icon_altura)

# Título
label_titulo = tk.Label(root, text="Calculadora de IMC", font=("Arial", 36))
label_titulo.pack()

# Entrada de peso
frame_peso = tk.Frame(root)
frame_peso.pack()
label_icon_peso = tk.Label(frame_peso, image=icon_peso)
label_icon_peso.pack(side=tk.LEFT)
entry_peso = tk.Entry(frame_peso, font=("Arial", 24), width=10)
entry_peso.pack(side=tk.LEFT)

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

valores_imc = [
    ("Tabela", "IMC"),
    ("Abaixo do peso", "< 18.5"),
    ("Peso normal", "18.5 - 24.9"),
    ("Sobrepeso", "25 - 29.9"),
    ("Obesidade", ">= 30")
]

for i, (categoria, imc) in enumerate(valores_imc):
    label_categoria = tk.Label(tabela, text=categoria, font=("Calibra", 16, "bold"))
    label_categoria.grid(row=i, column=0, padx=5, pady=5)

    label_imc = tk.Label(tabela, text=imc, font=("Arial", 16, "bold"))
    label_imc.grid(row=i, column=1, padx=5, pady=5)

root.mainloop()
