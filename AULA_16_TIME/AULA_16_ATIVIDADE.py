# # 2 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora

# from datetime import datetime, timedelta

# data_atual = datetime.now()
# futuro = data_atual + timedelta(days=7)

# print(futuro)

# # 3 - Peça ao usuário para inserir um ano e, em seguida, exiba o ano atual.
# from datetime import datetime

# data  = input("Digite data atual aqui um ano (ano-mes-dia):")
# data_atual = datetime.now()

# print(data_atual)

# 4 - Calcule e exiba a data e hora atuais em um formato personalizado(utilize diretivas).
from datetime import datetime

data_atual = datetime.now()
formato_personalizado="%d-%B-%Y \n%p %H:%M:%S \n%j-%w"

formatado = data_atual.strftime(formato_personalizado)


print(formatado)  

