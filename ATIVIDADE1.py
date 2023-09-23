nome = input("\nDigite o seu nome:")
print("Olá", nome)
print("Digite o  número  da respectiva operação ")
print("1- Adição")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")

lang = input()
match lang:
    case "1":
        n = float(input("Digite primeiro número"))
        n2 = float(input("Digite segundo número"))
        n3 =  n + n2
        print(nome,"Parabéns o resultado é:", n3)

    case "2":
        n = int(input("Digite primeiro número"))
        n2 = int(input("Digite segundo número"))
        n3 =  n - n2
        print(nome,"Parabéns o resultado é:", n3)

    case "3":
        n = int(input("Digite primeiro número"))
        n2 = int(input("Digite segundo número"))
        n3 =  n * n2
        print(nome,"Parabéns o resultado é:", n3)
    
    case "4":
        n = int(input("Digite primeiro número"))
        n2 = int(input("Digite segundo número"))
        n3 =  n / n2
        print(nome,"Parabéns o resultado é:", n3)

    case _:
        print("ERRO")
