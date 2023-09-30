# #Atividade 1
# n = int(input("Digite primeiro número "))
# print("Parabéns o resultado é:", n*n)

# #Atividade 2
# nome = "Betriz"
# sobrenome = "Alves"
# print(nome, sobrenome)

# #Atividade 3
# n1 = input("Digite primeiro número ")
# n2 = input("Digite o segundo número ")
# print ("Numeros", n1 + n2)

# #Atividade 4
# palavra = "Python"
# n3 = int(input("Digite primeiro número"))
# print(palavra, n3)

# #Atividade 5
# word_1 = "Dell i5"
# word_2 = input("Digite uma palavra ")
# print (f"O computador {word_1} é {word_2}")

# #Atividade 6
# h =10
# m= 10 
# s = 0
# print (f"{h}:{m}:{s}")

# #Atividade 7
# tel = "99999-9999"
# codigo = "11"
# print(f"{codigo} {tel}")

# #Atividade 8
# ingr_1 = "Farinha"
# ingr_2 = "Ovo"
# ingr_3 = "Leite"
# print (f"{ingr_1}, {ingr_2}, {ingr_3}")

# #Atividade 9 
# word_3 = input("Digite a primeira palavra ")
# word_4 = input("Digite a segunda palavra ")
# word_5 = input("Digite a terceira palavra ")
# print(f"{word_3} {word_4} {word_5}")

#Atividades Condicionais

#Atividade 1
idade = int(18)
idade2 = int(45)

#Atividade 2
idade = int(input("Digite sua idade "))
if idade >=18:
    print("Pode Entrar")
else:
    print("Menor de idade, acesso proibido")

#Atividade 3
n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))
n3 = float(input("Digite a terceira nota "))

resultado = (n1+n2+n3)/3

if resultado >= 7:
    print("Aprovado")
else:
    print(f"Reprovado", resultado)