class People:
    def __init__(self, nome, idade, curso, area, cor):
        self.__nome = nome 
        self.__idade = idade
        self.__curso = curso 
        self.__area = area
        self.__cor = cor 
        
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, new_color):
     self.__cor = new_color
    
    @property 
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, new_area):
        self.__area = new_area
    
    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def curso(self, new_course):
        self.__curso = new_course
    
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, new_age):
        self.__idade = new_age
        
    @property
    def nome(self):
        return self.__nome
    
    @idade.setter
    def nome(self, new_name):
        self.__nome = new_name
    

    def __str__(self):
        return(
            f"Nome: {self.__nome}\n"
            f"Idade: {self.__idade}\n"
            f"Curso:{self.__curso}\n"
            f"AREA: {self.__area}\n"
            f"Cor: {self.__cor}\n"
        )

        
pessoa1 = People("ANA", 12, "Biomedicina", "SAUDE", "Parda")
print("\nMostrando a pessoa 1 antes das mudanças:")
print(pessoa1)

print("\nMudancas ocorridas:")
pessoa1.nome = "Klaywin"
pessoa1
pessoa1.cor = "Branca"
print(pessoa1)