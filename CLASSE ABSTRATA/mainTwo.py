import abc

#------------------------------------------------------------------------------------------------------
class Account(abc.ABC):
    """
    Classe abstrata que exige o metodo "update" em todas as classes que herdam da mesma.
    """
    def __init__(self,number,holder, balance=0.0, limit=0.0):
        """""
        Args:
            number (int): numero da determinada conta
            holder (str): nome do tituar da determinada conta
            balance (float): saldo da determinada conta
            limit (float): limite da conta.
        """
        self._number = number 
        self._holder =  holder
        self._balance = balance 
        self._limit = limit 
    
    @abc.abstractmethod
    def update(self, rate):
        pass
    
    def deposit(self, value):
        """
        Deposita no saldo um determinado valor acrescido de uma taxa de 10%
        """
        self._balance += value + 0.10
         
    def __str__(self):
        """
        Retorna em formato de string a representação da conta X
        """
        return(
            f"\n--- Account Details ---"
            f"Number of Account: {self._number}\n"
            f"Holder:{self._holder}\n"
            f"Balance: {self._balance}\n"
            f"Limit: {self._limit}\n"
            f"Type of Account: {type(self).__name__}\n"
        )     
class CurrentAccount(Account):
    """
    Classe responsável por simular uma conta corrente
    """
    def __init__(self, number, holder, type="Current Account",balance=0, limit=0):
        """""
        Args:
            number (int): numero da conta
            holder (str): titular da conta
            type (str): tipo da conta, neste caso "Current Account"
            balance (int): saldo da conta
            limit (int): limite da conta
        """
        super().__init__(number, holder, balance, limit)
        self._type = type
        
    def update(self, rate):
        """""
        Args:
            rate (float): taxa de atualização do valor monetário

        Returns:
            float: Balance
        """
        self._balance *= (1 + rate * 2)
        return self._balance

    def deposit(self, value):
        """""
        Realiza um deposito na conta juntamente com um desconto de 10% no valor
        """
        self._balance += value - 0.10   
class SavingsAccount(Account):
    """
    Representa uma conta poupança
    """
    def __init__(self, number, holder,type="Savings Account", balance=0, limit=0):
        """
        Inicializa uma conta com nome, titular, limit,saldo e tipo
        Args:
            number (int): numero da conta
            holder (str): titular da conta
            type (str): "Savings Account".
            balance (int): saldo da conta
            limit (int): limite da conta
        """
        super().__init__(number, holder, balance, limit)
        self._type = type
        
    def update(self, rate):
        """""
        Args:
            rate (taxa): taxa de atualização do vallor monetário

        Returns:
            _type_: Savings Account
        """
        self._balance *= (1 + rate * 3)
        return self._balance 
class InvestimentAccount(Account):
    """
    Cria uma classe de investimentos
    """
    def __init__(self, number, holder, type="Investiment Account",balance=0, limit=0):
        """""
        Args:
            number (int): numero da conta
            holder (str): titular da conta
            type (str): tipo da conta, neste caso "Investiment Account"
            balance (int): saldo da conta
            limit (int): limite da conta
        """
        super().__init__(number, holder, balance, limit)
        self._type = type 
        
    def update(self, rate):
        """
        Atualiza o saldo da conta com uma taxa multiplicada por 5
        """
        self._balance *= (1 + rate * 5)
        return self._balance
class UpdaterAccounts():
    """
    Simula uma atualização de contas do banco 
    """
    
    def __init__(self, rate_selic, total_balance=0.0):
        """
        Inicializa o construtor com a taxa selic atual e o saldo atual da conta
        """
        self._rate_selic = rate_selic
        self._total_balance = total_balance
        
    def run(self, account):
        """
    faz uma atualização do saldo de uma conta com base na taxa Selic.

    esse método exibe o saldo anterior da conta, aplica a taxa de atualização 
    e, em seguida, soma o novo saldo  ao total de saldos gerenciados pela instancia total.
    
    Efeitos :
        - modifica o saldo da conta fornecida.
        - atualiza o atributo `_total_balance` da instância com o novo saldo.
        - exibe o saldo anterior no console.
    """
        print(f"Previous Balance: {account._balance}\n")
        account.update(self._rate_selic)
        self._total_balance += account._balance
    
    @property
    def total_balance(self):
        """
        Retorna o saldo total da conta
        """
        return self._total_balance   
class Bank:
    """
    Classe que simula um banco:
    """
    def __init__(self):
        """
        É criada uma lista vazia para armazenar todas as contas presentes dentro do banco
        """
        self.accounts = []
        
    def add(self, account):
        """"
        Este método vai percon
        """
        self.accounts.append(account)
        
    def collect_accounts(self, indice):
        """
        Retorna a conta no índice informado, se existir.

        Retorna None se o índice for inválido.
        """
        if 0 <= indice < len(self.accounts):
            return self.accounts[indice]
        else:
            return None
        
    def total_accounts(self):
        """
        Lê as contas presentes na lista de contas e me retorna
        """
        return len(self.accounts)
    
#-------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    current_account_test = CurrentAccount('1342-8', "Joao Lucas", 1000.0)
    savings_account_test = SavingsAccount('24453-3', "Maria Antonia Silva de Medeiros", 500.0)
    investiment_account_test = InvestimentAccount('753098-9',"Joao Moreira Silvestre", 2000.0)

    print("\nDepositing money into accounts")
    current_account_test.deposit(500.0)
    savings_account_test.deposit(1000.0)
    investiment_account_test.deposit(1500.0)


    accounts_updates = UpdaterAccounts(0.01)

    accounts_updates.run(current_account_test)
    accounts_updates.run(savings_account_test)
    accounts_updates.run(investiment_account_test)
        
    print(f"The Final Balance: {accounts_updates._total_balance}")

    print("\n Testing the Bank Class")
    b1 = Bank()
    b1.add(current_account_test)
    b1.add(savings_account_test)
    b1.add(investiment_account_test)
    print(f"Total number of accounts at the bank: {b1.total_accounts()}")

    b1.update_accounts(accounts_updates)            
    print(f"Updated total balance at the bank: {accounts_updates.total_balance:.2f}")
    
    
    
      
        
        
        
    
     
    
        
 


    
    
        
