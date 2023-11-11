# 1 - Crie uma classe chamada Cachorro com um atributo nome e um método 
# latir que imprima "Woof!" quando chamado. 
# Em seguida, crie um objeto da 
# classe Cachorro e chame o método latir.

# class Cachorro:
#     def __init__(self, nome):
#         self.nome = nome
        
#     def latir(self):
#         print(f"Woof! {self.nome} ")
        
# cachorro =  Cachorro('Rubens')

# cachorro.latir()


# 2-Crie uma classe chamada Retangulo com atributos largura e 
# altura. Adicione um método chamado calcular_area que retorna a área do retângulo.

# class Retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura
    
#     def calculo(self):
#         print(f'area total é',self.largura * self.altura)
        
        
# largura2 = float(input())
# altura2 = float(input())
   
# area=Retangulo(largura2, altura2)

# minha_area = area.calculo()

# 3: Crie uma classe chamada Carro com um atributo chamado velocidade 
# (inicialmente 0). Em seguida, adicione um método chamado acelerar que aumenta a
# velocidade em 5 unidades a cada vez que é chamado.

class Carro:
    

        
    def __init__(self,velocidade = 0):
        self.velocidade = velocidade
            
    def acelerar(self):
        print(self.velocidade)
        
aceleracao = Carro(+5)
    
velo =  aceleracao.acelerar()
                
    