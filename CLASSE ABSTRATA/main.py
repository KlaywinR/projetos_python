import abc

class Account(abc.ABC):
    def __init__(self, number, holder, balance=0.0, limit=1000.0):
        self._number = number
        self._holder = holder 
        self._balance = float(balance)
        self._limit = limit 
        
    @abc.abstractmethod
    def update():
       pass
    
    @property
    def balance(self):
        return self._balance
    
    def __str__(self):
        return (
            f"\n== Account Details =="
            f"Number:{self._number}\n"
            f"Holder: {self._holder}\n"
            f"Balance: {self._balance}\n"
            f"Limit:{self._limit}\n"  
        )
    def type(self):
        """""
        Returns:
        retorna o tipo da classe 
        """
        return self.__class__.__name__    

class CurrentAccount(Account):
    """""
        CurrentAccount (Account): retorna a representação de uma conta conrrente
    """
    def __init__(self, number, holder, balance=0.0, limit=1000):
        """
        Cria uma conta do tipo corrente; possuindo nome, titular, saldo e limite
        Args:
            number (int): numero da determinada conta
            holder (str): nome do titular da determinada conta
            balance (float): saldo da conta
            limit (int): limite da conta
        """
        super().__init__(number, holder, balance, limit)
    
    def update(self, rate):
        """
        Args:
            rate (int): taxa de atualização do saldo da conta
        Returns:
        retorna o saldo da conta acrescido de uma taxa duplicada.
        
      """
        self._balance += self._balance * rate * 2
        return self._balance
    
    def deposit(self, value):
        """
        Return: deposita na conta um valor descontado de uma taxa fixa de 10%
        Args:
            value (int): _description_
        """
        self._balance += value - 0.10
    
    def __str__(self):
        """""
        Returns:
            string : Retorna a repesenção de uma conta corrente
        """
        return (
            f"Current Account Holder: {self._holder}\n"
            f"General Balance: {self._balance}"
        )
    def type(self):
        """""
        Returns:
        retorna o tipo da classe 
        """
        return self.__class__.__name__
    
class SavingsAccount(Account):
    """
        Representacao de uma conta poupanca
    """
    def __init__(self, number, holder, balance=0, limit=1000):
        """
        Args:
            number (int): numero da conta
            holder (str): titular da conta
            balance (int, optional): saldo da conta
            limit (int): limite da conta 
        """
        super().__init__(number, holder, balance, limit)
        
    def update(self, rate):
        """
        Retorna o valor do salario com uma taxa triplicada
        """
        self._balance += self._balance * rate * 3
        return self._balance
       
    def __str__(self):
        """
        retorna uma representação de uma string na conta poupança
        """
        return (
            f"SavingsAccount Holder:{self._holder}\n"
            f"General Balance: {self._balance}\n"
        )
    def type(self):
        """""
        Returns:
        retorna o tipo da classe 
        """
        return self.__class__.__name__

class AccountInvestiment(Account):
    def __init__(self, number, holder, balance=0, limit=1000):
        super().__init__(number, holder, balance, limit)
        
    def update(self, rate):
        self._balance += self._balance * rate * 5
        return self._balance
    
    def deposit(self, value):
        """
        Return: deposita na conta um valor descontado de uma taxa fixa de 10%
        Args:
            value (int): _description_
        """
        self._balance += value - 0.10
    
    def type(self):
        """""
        Returns:
        retorna o tipo da classe 
        """
        return self.__class__.__name__
    
    

if __name__ == '__main__':
    
    cc = CurrentAccount(231-0, "Aninha", 200.0, 400.0)
    cp = SavingsAccount(123-0, "Antonia", 450.0, 1000.0)
    
print("\n----- Current Account & Savings Account Balances -------------")
print(cc._balance)
print(cp.balance)


print("--------------- Testing AccountInvestiment -----------------")

CountInvestimentOne = AccountInvestiment(123-7, "Ana Marilia Silva", 1000.0)
CountInvestimentOne.deposit(1000.0)
CountInvestimentOne.update(0.01)
print(CountInvestimentOne._balance)


print("\n --- Data type of classes -----")
print(type(AccountInvestiment))
print(type(Account))
print(type(CurrentAccount))
print(type(SavingsAccount))
print("\n----------------------------------------------------------")




        