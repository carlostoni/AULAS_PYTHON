#atividade 1
#4: Crie um conjunto chamado "frutas" com as seguintes frutas: maçã, banana, 
#laranja, pêra e abacaxi. Em seguida, imprima o número de 
#elementos no conjunto

# def elementos():
#     frutas= {'maçã', 'banana', 'laranja', 'pêra', 'abacaxi'}
#     numero = len(frutas)
#     print(numero)
# elementos()

#atividade 2
# 5: Crie dois conjuntos, "conjunto1" e "conjunto2", 
# com alguns números inteiros. 
# Imprima a união desses dois conjuntos

# def uniao():
#     conjunto1 = {1, 3, 5, 7, 9}
#     conjunto2 = {2, 4, 6, 8, 10}

#     uniao1 = conjunto1.union(conjunto2)
#     print(uniao1)
# uniao()

#atividade 3
#6: Dado o conjunto "cores" com cores diferentes, remova a cor 
#"vermelho" do conjunto.s
# def remover():
#     cor = {'azul', 'laranja', 'verde', 'vermelho'}
#     cor1 = {'roxo', 'preto', 'branco', 'cinza'}
#     uniao1 = cor.union(cor1)
#     print(uniao1)
   
#     uniao1.remove('vermelho')
#     print(uniao1)
# remover()

#atividade 4
# 7: Crie um conjunto chamado "numeros" com os números de 1 a 10. 
# Em seguida, crie um novo conjunto chamado "pares" 
# contendo os números pares do conjunto "numeros".

# def par_impar():
     
#      conjunto1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#      conjuntopar =[]
#      conjuntoimpar =[]
    
#      for conjunto1 in conjunto1:
#         if conjunto1 % 2 == 0:
#          conjuntopar.append(conjunto1)
#         else :
#          conjuntoimpar.append(conjunto1)
         
#      print(conjuntopar)
#      print(conjuntoimpar)
# par_impar()

#atividade 5
# 8: Verifique se o conjunto "alunos_aprovados" contém todos os 
# alunos do conjunto "todos_alunos". Os conjuntos devem ser 
# definidos com nomes apropriados.

# def aprovados():
#     alunos_aprovados ={'carlos', 'andre', 'maria'}
#     todos_alunos = {'carlos', 'andre', 'maria', 'ana'}
    
#     aprovados1= []
#     reprovados = []
    
#     for nome in todos_alunos:
        
#         if nome in alunos_aprovados :
#            aprovados1.append(nome)
#         else :
#             reprovados.append(nome)
       
#     for i in range(1):
#         print('aprovados', aprovados1)
#         print('reprovados', reprovados)

# aprovados()

#atividade 5 resolucao
# alunos_aprovados ={'carlos', 'andre', 'maria'}
# todos_alunos = {'carlos', 'andre', 'maria', 'ana'}

# print(todos_alunos.difference(alunos_aprovados))

    
    