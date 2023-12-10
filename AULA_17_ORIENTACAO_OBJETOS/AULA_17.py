class House:
    def __init__(self, length, color):
        self.length= length
        self.color = color
        
    def display(self):
        print(self.length, self.color)
# instancia
house = House(100, 'green')
house.display

house2 = House(200, 'red')
house2.display()


# class Aluno:
#     def __init__(self,nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     def display(self):
#         print(self.nome, self.idade)

# class Fundamental(Aluno):
#     def acrescentar(self):
#         print('Olá alunos')
#         print("1"+ 2)

# class Medio(Aluno):
#     pass

# aluno = Fundamental('Carlos', 19)

# aluno.display()
# aluno.acrescentar()
