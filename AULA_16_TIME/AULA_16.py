# import datetime

# n = datetime.datetime.now()
# print(n)

from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (ano-mes-dia):")
nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
idade = datetime.now() - nascimento

# Extrair apenas a parte dos anos da diferença de datas
anos = idade.days // 365

print(anos)
