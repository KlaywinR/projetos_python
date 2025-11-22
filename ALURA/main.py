class Employee:
    """Representa um funcionário genérico da empresa.
        _name (str): Nome do funcionário.
        _cpf (str): CPF do funcionário.
        _wage (float): Salário do funcionário.
    """
    def __init__(self, name, cpf, wage):
        """Inicializa um funcionário com nome, CPF e salário."""
        self._name = name
        self._cpf = cpf
        self._wage = wage

    @property
    def name(self):
        """str: retorna o nome do funcionário."""
        return self._name
    
    @property
    def social_number_security(self):
        """str: retorna o CPF do funcionário."""
        return self._cpf

    @property
    def wage(self):
        """float: retorna o salário do funcionário."""
        return self._wage

    def get_bonificacao(self):
     """
        calcula o bônus do funcionário.
        float: Valor do bônus (10% do salário).
    """
     return self._wage * 0.10

    def __str__(self):
        """""
        Retorna uma representação em string do funcionário
        """
        return f"Employee: {self._name} - CPF: {self._cpf} - Wage: {self._wage}"

class Manager(Employee):
    """Representa um gerente que herda de Employee.
        str -> _password: senha de acesso do gerente.
        int -> _qtd_gerenciados: número de funcionários gerenciados.
    """
    def __init__(self, name, cpf, wage, password, qtd_gerenciados):
        """inicializa um gerente com name, CPF, salário, senha e número de gerenciados"""
        super().__init__(name, cpf, wage)
        self._password = password
        self._qtd_gerenciados = qtd_gerenciados

    def password_authentication(self, password):
        """
            Vê se a senha fornecida está correta.
            str -> password: senha a ser vista.
            bool: True se a senha for correta; caso contrário False.
        """
        if self._password == password:
            print("Access Allowed.")
            return True
        else:
            print("Access Denied.")
            return False

    def get_bonificacao(self):
        """ calcula o bônus que gerente recebe.
            float: Valor do bônus = bônus do funcionário + 1000.0 fixo.
        """
        return super().get_bonificacao() + 1000.0

    def __str__(self):
        """""
        representação de string do gerente.
        """
        return f"Manager: {self._name} - CPF: {self._cpf} - Wage: {self._wage} - Employees: {self._qtd_gerenciados}"
    
class Client:
    """
        Representa um cliente do banco.
        str -> _name: nome do cliente.
        str -> _cpf: cpf do cliente.
        str -> _password: senha do cliente.
    """
    def __init__(self, name, cpf, password):
        """""
        Inicializa-se uma pessoa X, a mesma possui: name, cpf e password.
        """
        self._name = name
        self._cpf = cpf
        self._password = password

    def __str__(self):
        """
        Representação de string de determinado cliente:
        """
        
        return f"Client: {self._name} - CPF: {self._cpf} - Password: {self._password}"

class Count:
    """
        Representa uma conta de banco genérica, a qual possui:
        int -> number: Número da conta.
        str -> holder: Titular da conta bancária.
        float -> balance: Saldo da determinada conta bancária.
        float -> limit: Limite da determinda conta bancária.
    """
    def __init__(self, number, holder, balance=0.0, limit=1000.0):
        """
       Inicia-se um conta com numero, titular, saldo e limite em reais.
        Args:
            number (int): numero da conta bancaria.
            holder (str): nome do titular da conta.
            balance (float): saldo da conta bancária.
            limit (float): limite da conta bancaria.
        """
        self._number = number
        self._holder = holder
        self._balance = balance
        self._limit = limit
    
    @property
    def balance(self):
        """
        Retorna o saldo da conta bancária X.
        """
        return self._balance

    def deposit(self, value):
        """Realiza um depósito na conta.

        Args:
            value (float): Valor a ser depositado.
        """
        self._balance += value

    def withdraw(self, value):
        """faz um saque na conta; cons. o limite.

        Args:
            value (float): valor a ser sacado.
        """
        if value <= self._balance + self._limit:
            self._balance -= value
        else:
            print("Your balance is insufficient!")

    def update(self, rate):
        """
        Args:
            rate (float): taxa de atualização do valor monetário
        Returns:
            float: NewBalance
        """
        self._balance += self._balance * rate
        return self._balance

    def __str__(self):
        """
        Representação de string de determinado cliente:
        """
        return (
            f"Account Details:\n"
            f"Number: {self._number}\n"
            f"Holder: {self._holder}\n"
            f"Balance: {self._balance}\n"
            f"Limit: {self._limit}\n"
        )
class CurrentAccount(Count):
    """
    Representa uma conta corrente
    """
    def update(self, rate):
        """

        Args:
            rate (float): taxa de atualização 
            
        Returns:
         float: NewBalance
            
        """
        self._balance += self._balance * rate * 2
        return self._balance

    def deposit(self, value):
        """deposita um valor descontando uma taxa fixa de 10%"""
        self._balance += value - 0.10  

    def __str__(self):
        """Retorna a representação de uma string de uma conta corrente"""
        return f"CurrentAccount - Holder: {self._holder} | General Balance: {self._balance}"
class SavingsAccount(Count):
    """
    Representa uma conta poupança
    """
    def update(self, rate):
        """
        Atualiza o saldo com uma taxa triplicada:
        """
        self._balance += self._balance * rate * 3
        return self._balance

    def __str__(self):
        """Retorna a representação de uma string da conta poupança"""
        return f"SavingsAccount - Holder: {self._holder} | General Balance: {self._balance}"
class AccountUpdater:
    """Atualiza as contas com base na taxa Selic e mantém o total atualizado."""
    def __init__(self, selic, total_balance=0):
        """Inicializa o atualizador com a taxa Selic e o saldo total."""
        self._selic = selic
        self._total_balance = total_balance

    @property
    def total_balance(self):
        """
        Retorna o saldo total acumulado
        """
        return self._total_balance

    def run(self, count):
        """faz a atualização de uma conta Z.

        Args:
            count: conta a ser atualizada.
        """
        try:
            print(f"Previous Balance: {count.balance}")
            self._total_balance += count.update(self._selic)
            print(f"Updated Balance: {count.balance}\n")
        except AttributeError:
            print(f"Error: {count.__class__.__name__} is not a valid account!")
class Bank:
    """
        Representa um banco que contem varias contas
    """
    def __init__(self, name):
        """
        Inicializa com nome e uma lista vazia para adicionar as contas
        """
        self._name = name
        self._accounts = []

    def add(self, count):
        """
        Adiciona uma determinada conta ao banco
        """
        self._accounts.append(count)

    def get_account(self, position):
        """
        Retorna uma conta em uma determinada posição especificada.
        """
        return self._accounts[position]

    def total_accounts(self):
        """
        Retorna o numero total de contas presentes no banco
        """
        return len(self._accounts)

    def __str__(self):
        """Retorna uma representação em string do banco."""
        return f"Bank {self._name} has {self.total_accounts()} accounts."
class BonusControl:
    """Controla o total de bonificações de funcionários."""
    def __init__(self):
        """inicializa o controle com total de bônus igual a zero."""
        self._total_bonus = 0

    def register(self, obj):
        """faz o regitros de um objeto que possui método de bonificação.
            obj: objeto que implementa o método get_bonificacao().
        """
        try:
            self._total_bonus += obj.get_bonificacao()
        except AttributeError:
            print(f"Error: {obj.__class__.__name__} does not implement get_bonificacao().")

    @property
    def total_bonus(self):
        """
            float: retorna o total acumulado em bonificação
        """
        return self._total_bonus

#programa principal:
if __name__ == "__main__":
    print("--- Testando as classes de Empregados e Gerente ---\n")

    f1 = Employee("Paulinia Moreira", "111111111-11", 2000.0)
    m1 = Manager("Chiquinha Miuda", "222222222-22", 5000.0, "1234", 5)

    print(f1)
    print(m1)
    print(f"Employee Bonus: {f1.get_bonificacao()}")
    print(f"Manager Bonus: {m1.get_bonificacao()}\n")

    print("--- Testando as contas ---\n")
    c1 = Count("132-6", "Paulo Lima", 100.00, 1000.00)
    c2 = CurrentAccount("342-9", "Maiza Silva", 200.00, 2000.00)
    c3 = SavingsAccount("763-8", "Ricardo Moreira", 300.00, 3000.00)

    c1.update(0.1)
    c2.update(0.1)
    c3.update(0.1)

    print(c1)
    print(c2)
    print(c3)
    print("======================================\n")

    print("--- Testando as adicoes às contas ---\n")
    adc = AccountUpdater(0.01)
    adc.run(c1)
    adc.run(c2)
    adc.run(c3)
    print(f"Total balance after updates: {adc.total_balance}\n")

    print("--- Testando a Classe Banco ---\n")
    bank = Bank("Klawys Bank")
    bank.add(c1)
    bank.add(c2)
    bank.add(c3)

    print(bank)
    for account in bank._accounts:
        adc.run(account)
    print(f"Final Total Balance: {adc.total_balance}\n")

    print("---  Testando o Poliformismo ---\n")
    control = BonusControl()
    control.register(f1)
    control.register(m1)
    print(f"Total Bonuses: {control.total_bonus}\n")

    print("--- Testando o Ducking Typing---\n")
    client = Client("Maria", "333333333-33", "4321")
    control.register(client)

    print("0----------------0")
