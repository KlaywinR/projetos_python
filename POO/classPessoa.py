class Pessoa:
    def __init__(self, nome, idade, altura, cor, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cor = cor 
        self.peso = peso
    
    def falar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}"

# Criando objetos passando todos os atributos
p1 = Pessoa("Ana", 23, 1.65, "Branca", 60)
p2 = Pessoa("Paulo", 33, 1.80, "Pardo", 75)

# Chamando o método
print(p1.falar())
print(p2.falar())
