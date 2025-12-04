from abc import ABC, abstractmethod

class Taxable(ABC):

    @abstractmethod
    def get_valor_imposto(self):
        pass

class Account:
    def __init__(self, number, holder, balance):
        self._number = number
        self._holder = holder 
        self._balance = balance
        
    def deposit(self, value):
        self._balance += value
        
    def sacar(self, value):
        if value <= self._balance:
            self._balance -= value
            
    def get_balance(self):
        return self._balance

class CurrentAccount(Account,Taxable):
    def __init__(self, number, holder, balance):
        super().__init__(number, holder, balance)
       
    
    def get_valor_imposto(self):
        return self._balance * 0.01
    

class LifeInsurance(Taxable):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice
         
    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

class TaxManipulator:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        
        for item in lista_tributaveis:
            total += item.get_valor_imposto()
            
        return total
            
    
    
if __name__ == "__main__":

    print("----  Testing Current Account ----- ")
    cc1 = CurrentAccount("123-3", "Demetrios", 1000.0)
    cc2 = CurrentAccount("555-4", "Maria", 2000.0)

    print("Inicial Balance - Current Account 1:", cc1.get_balance())
    cc1.deposit(500)
    print("After Deposit:", cc1.get_balance())
    cc1.sacar(300)
    print("After Withdrawall:", cc1.get_balance())
    print("Tax - Current Account 1:", cc1.get_valor_imposto())

    print("\n ----- Testing Life Insurance ----- ")
    seguro1 = LifeInsurance(100, "Antonella", "321-99")
    seguro2 = LifeInsurance(300, "Carlos", "778-55")

    print("Insurance value 1 including tax:", seguro1.get_valor_imposto())
    print("Insurance value 2 including tax:", seguro2.get_valor_imposto())

    print("\n---- Testing Tax Manipulator ---- ")

    lista = [cc1, cc2, seguro1, seguro2]

    manipulador = TaxManipulator()
    total = manipulador.calcula_impostos(lista)

    print(f"\nTotal taxes charged: R$ {total}")
        
