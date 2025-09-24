class ContaBancaria:
    def __init__(self, titular,data=None, saldo=0):
       self.titular = titular    
       self.saldo = saldo
       self.data = data 
       
    def depositar(self, valor):
      self.saldo += valor
      return(
        f"Depósito de: {self.valor} feito com sucesso!\n"
        f"Saldo atual:{self.saldo}"
      )
      
    def sacar(self, valor):
        if valor > self.saldo:
         print("Valor indisponível para saque.")
        else:
            self.saldo -= valor
            return(
                f"Saque no valor de:{self.valor}\n"
                f"Saldo atual: {self.saldo}"
            )
            
    def ver_saldo(self):
        return(
            f"Titular da Conta: {self.titular}\n"
            f"Data: {self.data}\n"
            f"Saldo Atual: R${self.saldo}\n"
        )
        
nome = input("Nome do titular da conta: ")
data = int(input('Data de hoje:'))
saldo_iniciiaal = float(input("Valor inicial da conta:"))

conta = ContaBancaria(nome,saldo_iniciiaal,data)

while True:
    print(f"Cliente {nome}, o que você deseja?")
    print("1 - Ver Saldo da Minha Conta.")
    print("2 - Sacar Dinheiro.")
    print("3 - Depositar.")
    print("4 - Sair")
    
    
    opcaoDoCliente = input('Por favor, escolha uma opção para prosseguirmos com o seu atendimento.')
    
    if opcaoDoCliente == "1":
      print(conta.ver_saldo())
      
    elif opcaoDoCliente == "2":
       valor = float(input("Digite o valor para saque:"))
       print(conta.sacar(valor))
    
    elif opcaoDoCliente == "3":
        valor = float(input("Digite o valor para depósito:"))
        print(conta.depositar(valor))
        
    elif opcaoDoCliente == "4":
        print("Saindo do sistema.")
        break
    
    else: 
        print("Opção inválida.")
        
        
    
    