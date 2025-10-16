#Crie uma classe que modele uma pessoa:

##• Atributos: nome, idade, peso e altura

##• Métodos: Envelhecer, engordar, emagrecer, crescer.

##• Obs: Por padrão, a cada ano que a pessoa envelhece, sendo a
### idade dela menor que 21 anos, ela deve crescer 0,5 cm.

##• O construtor pode possuir ou não parâmetros.

class Pessoa:
    def __init__(self,nome,idade=0,peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos=1):
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.crescer(0.005)
    
    def engordar(self,quilos):
        self.peso += quilos
    
    def emagrecer(self, quilos):
       self.peso -= quilos
       if self.peso < 0:
           self.peso = 0
       
    def crescer(self,metros):
        self.altura += metros
    
    def mostrar_dados(self):
        return(
        f'Idade:{self.idade}\n'
        f'Altura:{self.altura}\n'
        f'Peso:{self.peso}'
        
        )  
 ##Exibido  a primeira pessoa:
##########################################################################################      
p1 = Pessoa("Joao Silva", idade=19, peso=67, altura=1.98)
##########################################################################################

print(f"\n#### Dados Obtidos da Pessoa {p1.nome} ####")
print("Antes:")
print(p1.mostrar_dados())

p1.emagrecer(3.0)
p1.crescer(2.0)
p1.envelhecer(5)

##mostrando o depois da pessoa 01
print("\nDepois:")
print(p1.mostrar_dados())

             
        
           
    
    