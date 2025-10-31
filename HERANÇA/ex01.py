from tabulate import tabulate
class Funcionario:

    def __init__(self, name, cpf, salario):
        self.__name = name 
        self.__cpf = cpf
        self.__salario  = salario 
    
    def aumentarSalario(self, percent):
        self.__salario *= (1 + percent/100)
        
    def mudarCargo(self, novoCargo):
        self.cargo = novoCargo
        
    def apresentar(self):
        return f'{self.__name} {self.__cpf} {self.__salario}'
 
class Gerente(Funcionario):
    
    def __init__(self, name, cpf, salario, password, setor  , cargo):
        super().__init__(name, cpf, salario, password, cargo)
        ##pq sse coloca self.setor sozinho?
        self.setor = setor 
    
    def AutenticacaoPorSenha(self, __password):
        if self.__password == __password:
            print("Acesso Permitido.!")
        else:
            print("Acesso Negado.")
            return False
        
    def aumentarSalario(self, percent):
        self.__salario *= (1 + percent/100)
        
    def calcularBonus(self):
        return self.__salario * 0.2
        
    

##displaying a table fucionarios
list_of_data = [
    ["Noangela", 46652800, 46, "aquino"],
    ["Cicero", 76537800, 84, "Dias"],
    ["Joao", 46652800, 46, "Dias"],
    ["Klaywin", 76537800, 84, "Felix"]
]
        
header_list_of_fata = ['Name', 'Social Security Number', 'Age', 'Last Name']

print(tabulate(list_of_data, headers=header_list_of_fata, tablefmt="grid" ))

