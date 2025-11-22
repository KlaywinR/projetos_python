#class funcionario
class Employee:
#name - cpf - salario
    def __init__(self, name, cpf, wage):
        self._name = name 
        self._cpf = cpf
        self._wage  = wage 
    
    @property
    def name(self):
        return self._name
    @property
    def social_number_security(self):
        return self._cpf
    
    @property
    def wage(self):
        return self._wage
    

    def get_bonificacao(self):
        return self._wage * 0.10
    
    def __str__(self):
        return f'Funcionario: {self._name} - CPF: {self._cpf} - SALARIO: {self._wage}'
 
class Manager(Employee):
    
    def __init__(self, name, cpf, salario, password, qtd_gerenciados):
        super().__init__(name, cpf, salario)
        self._password = password
        self._qtd_gerenciados = qtd_gerenciados
    
    def password_authentication(self, password):
        if self._password == password:
            print("Access Allowed.")
            return True
        else:
            print("Access Denied.")
            return False
        
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.0
    
    
    def __str__(self):
        return f'Manager: {self._name} - CPF: {self._cpf} - Wage: {self._wage} - Employees: {self._qtd_gerenciados}'
   
class Client:
    def __init__(self, name, cpf, password):
         self._name = name
         self._cpf = cpf
         self._password = password

    def __str__(self):
        return f"Client: {self._name} - CPF {self._cpf} - Password: {self._password}"
        return f"Client: {self._nome} - CPF {self._cpf} - The Password: {self._password}"
    
class Count:
    def __init__(self, number, holder, balance=0.0, limit=1000.0):
        self._number = number
        self._holder = holder
        self._balance = balance
        self._limit = limit

    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        self._balance += value

    def sacar(self, value):
        if value <= self._balance + self._limit:
            self._balance -= value
        else:
            print("Your Balance is insufficient")

    def update(self, rate):
        self._balance += self._balance * rate
        return self._balance

    def __str__(self):
        return (
            "Account Details:\n"
            f"Number: {self._number}\n"
            f"Holder: {self._holder}\n"
            f"Balance: {self._balance}\n"
            f"Limit: {self._limit}\n"
        )     
        
class CurrentAccount(Count):
    def update(self, rate):
        self._balance += self._balance * rate * 2
        return self._balance

    def deposit(self, value):
        self._balance += value - 0.10  #tx fixa

    def __str__(self):
        return f"CurrentAccount - Holder: {self._holder} | General Balance : {self._balance}"
        return f"CurrentAccount - Holder: {self._titular} | General Balance : {self._saldo}"
    
##c. poupança
class SavingsAccount(Count):

    def update(self, rate):
        self._balance += self._balance * rate * 3
        return self._balance

    def __str__(self):
        return f"SavingsAccount - Holder: {self._holder} | General Balance: {self._balance}"
        return f"SavingsAccount - Holder: {self._titular} | General Balance: {self._saldo}"
        
class AtualizadorDeContas:
    def __init__(self, selic, total_balance=0):
        self._selic = selic
        self._total_balance = total_balance

    @property
    def total_balance(self):
        return self._total_balance

    def roda(self, count):
        try:
            print(f"Saldo anterior: {count.balance}")
            self._total_balance += count.update(self._selic)
            print(f"Saldo atualizado: {count.balance}\n")
        except AttributeError:
            print(f"Erro: {count.__class__.__name__} não é uma conta válida!")
            print(f"Erro: {Count.__class__.__name__} não é uma conta válida!")


class Bank:
    def __init__(self, name):
        self._name = name
        self._contas = []

    def adicionar(self, count):
        self._contas.append(count)

    def pegaConta(self, position):
        return self._contas[position]

    def pegaTotalDeContas(self):
        return len(self._contas)

    def __str__(self):
        return f"Banco {self._name} possui {self.pegaTotalDeContas()} contas."

class ControleDeBonificacoes:
    def __init__(self):
        self._total_bonificacoes = 0.0
if __name__ == '__main__':
    print("--- Testando a Classe de Funcionarios e Gerentes ---\n")
    
    f1 = Employee("Paulinia Moreira", "111111111-11", 2000.0)
    g1 = Manager("Chiquinha Miuda", "222222222-22", 5000.0, "1234", 5)

    print(f1)
    print(g1)
    print(f"Bonificação Funcionário: {f1.get_bonificacao()}\n")
    print(f"Bonificação Gerente: {g1.get_bonificacao()}\n")

    print("\n --- Testando as Contas dos Usuários ---")

    c1 = Count("132-6", "Paulo Lima", 100.00, 1000.00)
    c2 = CurrentAccount("342-9", "Maiza Silva", 200.00, 2000.00)
    c3 = SavingsAccount("763-8", "Ricardo Moreira", 300.00, 3000.00)

    c1.update(0.1) 
    c2.update(0.1)
    c3.update(0.1)

    print("\n--- +10% percent on everyone`s salary ---")
    print(c1) 
    print(c2)
    print(c3)
    print("\n=========================================")


    print("\n --- Testando o Atualizador de Contas ----")
    adc = AtualizadorDeContas(0.01) 
    adc.roda(c1)
    adc.roda(c2) 
    adc.roda(c3) 
    print(f"Saldo total: {adc._total_balance}\n")
    print("--------------------------------------------")


    print("--- TESTE DE BANCO ---")
    banco = Bank("Meu Banco") 
    banco.adicionar(c1) 
    banco.adicionar(c2) 
    banco.adicionar(c3)

    print(banco)
    for conta in banco._contas:
        adc.roda(conta)
    print(f"Total final Balance: {adc._total_balance}\n")

    print("=== TESTE DE POLIMORFISMO ===")
    controle = ControleDeBonificacoes() 
    controle.registra(f1) 
    controle.registra(g1)
    print(f"Total de bonificações: {controle.total_bonificacoes}\n")

    print("=== TESTE DUCK TYPING COM CLIENTE ===")
    cliente = Client("Maria", "333333333-33", "4321")
    controle.registra(cliente)  # Deve disparar erro de atributo
    print("=== FIM DOS TESTES ===")
print("--------------------------------------------")


print("--- TESTE DE BANCO ---")
banco = Bank() 
banco.adicionar(c1) 
banco.adicionar(c2) 
banco.adicionar(c3)

print(banco)
for conta in banco._contas: adc.roda(conta)
print(f"Totaal final Balance: {adc._total_balance}\n")

print("=== TESTE DE POLIMORFISMO ===")
controle = ControleDeBonificacoes() 
controle.registra(f1) 
controle.registra(g1) 
print(f"Total de bonificações: {controle.total_bonificacoes}\n") 

print("=== TESTE DUCK TYPING COM CLIENTE ===")
cliente = Client("Maria", "333333333-33", "4321")
controle.registra(cliente) # Deve disparar erro de atributo print("=== FIM DOS TESTES ===")