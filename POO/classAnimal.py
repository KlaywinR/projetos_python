class Animal:
    def __init__(self,cor, pelagem, tamanho, peso, altura, etnia ):
        self.cor = cor
        self.pelagem = pelagem
        self.tamanho = tamanho
        self.peso = peso 
        self.altura = altura
        self.etnia = etnia
      
    def apresentar(self):
            return (
        f"Cor: {self.cor} \n"
        f"Possui: {self.peso} quilos\n"
        f"Pelagem:{self.pelagem}\n"
        f"Tamanho:{self.tamanho}\n"
        f"Etnia:{self.etnia}\n"
        f"Altura:{self.altura }\n"
        )
          
         
animal01 = Animal("Preto",'ESCURA', 1.67, 66,99,'brasileira',)
animal02 = Animal("Branco",'ESCURA', 1.67, 25,56,'brasileira',)
animal03 = Animal("Marrom",'ESCURA', 1.67, 88,87,'brasileira',)

print(animal01.apresentar())
print(animal02.apresentar())
print(animal03.apresentar())

         