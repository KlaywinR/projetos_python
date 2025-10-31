class Count:
    def __init__(self, agencia, estado,number, saldo, limit, name):
        self.__agencia = agencia 
        self.__estado = estado
        self.__number = number
        self.__saldo = saldo 
        self.__limit = limit 
        self.__name = name 
        
##equivalentes a getters
    @property
    def extract(self):
     return (
    f"==============================\n"
    f"📄 Número da Conta: {self.__number}\n"
    f" - Agência: {self.__agencia}\n"
    f" - Estado da conta : {self.__estado}\n"
    f"💰 Saldo em Conta: R${self.__saldo:.2f}\n"
    f"💳 Limite da Conta: R${self.__limit:.2f}\n"
    f"👤 Nome do Titular: {self.__name}\n"
    f"=============================="
)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limit(self):
        return self.__limit

##prop setters:
    @limit.setter
    def limit(self, Newlimit):
        print(f"Valor Antes da Alteração: {self.__limit}")
        print(f"Alterando para: {Newlimit}")
        self.__limit = Newlimit
        print(f"Novo Valor do Limite :{self.__limit}")
        
        
    @extract.setter
    def extract(self):
        return f'Saldo do cliente {self.__owner}: R$ {self.__saldo}'
    

count1 = Count(agencia= 5674 , estado="Ativa", number= 52691, saldo=120,limit=30000, name="Larissa Magalhaes")
count2 = Count(agencia= 5662 , estado="Ativa", number= 99874, saldo=300,limit=80000, name="Paloma SIlva")
####### impressoes 

print("====================================\n")
print("Extrato das duas contas\n")
print(count1.extract)   
print(count2.extract)
print("====================================\n")

print("====================================\n")
print("Valores totais em R$ das contas:\n")
soma = count1.saldo + count2.saldo 
print(f"Valor Geral: {soma}")
print("====================================\n")

print("====================================\n")
print("Mudando o valor do limite da conta 1: ")
print("30.000 --> 28000: \n")
count1.limit = 28000
print("====================================\n")

print("====================================\n")
print("Mudando o valor do limite da conta 2: ")
print("30.000 --> 27000: \n")
count2.limit = 27000
print("====================================")









    
    
        

