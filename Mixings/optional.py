import abc

class Tax(abc.ABC):
    
    @abc.abstractmethod
    def get_value_imposto(s):
        pass
    
class Account:
    def __init__(self, number,holder, balance):
        self._number = number 
        self._holder = holder
        self._balance = balance
        
    def deposit (self, value):
        self._balance  += value
        
    def saca(self, value):
        if value <= self._balance:
            self._saldo += value
            return True
        return False
    
    def __repr__(self):
        return f"Conta:{self._number}, Holder of Account: {self._holder}."
         
class CurrentAccount(Account):
    def get_valor_imposto(self):
        return self._balance * 0.01

class SavingsAccount(Account):
    pass

class InvestimentAccount(Account):
    def update(self, rate):
        self._balance += self._balance * rate * 5
        
    def get_valor_imposto(self):
        return self._balance * 0.03
    
class LifeInsurance:

    def __init__(self, valor, titular, policy_number):
        self._valor = valor
        self._titular = titular
        self._policy_number = policy_number

    def get_valor_imposto(self):
        return 50 + (self._valor * 0.05)

    def __repr__(self):
        return f"Life Insurance: {self._policy_number}, Holder of Life Insurance: {self._titular})"
    
class TaxRandller:

    def calculate_taxes(self, lista):
        total = 0
        for item in lista:
            if isinstance(item, TaxRandller):
                total += item.get_valor_imposto()
            else:
                print(item, "this is a not taxable amount")
        return total
  

if __name__ == "__main__":

#classes tributaveis
    Tax.register(CurrentAccount)
    Tax.register(LifeInsurance)
    Tax.register(InvestimentAccount)

    
    cc = CurrentAccount("123-4", "João", balance=200)
    cc.deposit(1000.0)

    seguro = LifeInsurance(100.0, "José", "345-77")

    cp = SavingsAccount("123-6", "Maria", balance= 200)
    cp.deposit(2000.0)

    ci = InvestimentAccount("123-0", "Ana", balance= 200)
    ci.deposit(100.0)


    list = [cc, seguro, cp, ci]

#calculo de impostos
    mt = TaxRandller()
    total = mt.calculate_taxes(list)

    print("\n===== Results =====")
    print(f"Current account tax: R$ {cc.get_valor_imposto():.2f}")
    print(f"Life Insurance tax: R$ {seguro.get_valor_imposto():.2f}")
    print(f"Investiment Account tax: R$ {ci.get_valor_imposto():.2f}")
    print(f"Tax total: R$ {total:.2f}")
