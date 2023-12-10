import tkinter as tk

class ContaBancaria:
    def __init__(self):
        self.saldo = 50

    def saque(self, valor):
        self.saldo -= valor
        return f'Saque realizado. Saldo atual: {self.saldo}'

    def deposito(self, valor):
        self.saldo += valor
        return f'Depósito realizado. Saldo atual: {self.saldo}'

def realizar_operacao(tipo, valor, conta, resultado_var):
    if tipo == "saque":
        resultado_var.set(conta.saque(valor))
    elif tipo == "deposito":
        resultado_var.set(conta.deposito(valor))

def main():
    # Criar uma conta
    minha_conta = ContaBancaria()

    # Configurar a interface gráfica
    root = tk.Tk()
    root.title("Conta Bancária")

    resultado_var = tk.StringVar()

    label = tk.Label(root, text="Escolha a operação:")
    label.pack()

    saque_button = tk.Button(root, text="Saque", command=lambda: realizar_operacao("saque", float(entry.get()), minha_conta, resultado_var))
    saque_button.pack()

    deposito_button = tk.Button(root, text="Depósito", command=lambda: realizar_operacao("deposito", float(entry.get()), minha_conta, resultado_var))
    deposito_button.pack()

    entry = tk.Entry(root)
    entry.pack()

    resultado_label = tk.Label(root, textvariable=resultado_var)
    resultado_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
