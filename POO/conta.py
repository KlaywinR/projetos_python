class ContaBancaria:
    def __init__(self, titular, saldo=0, codigo_Apo='01'):
        self.titular = titular
        self.saldo = saldo
        self.codigo_Apo = codigo_Apo
        self.nome_Apo = "Conta Corrente" if codigo_Apo == '01' else "Poupança"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso! \nSaldo atual: {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            print(f"\nTransferência de {valor} para {conta_destino.titular} realizada com sucesso!")
            return True
        else:
            print("Saldo insuficiente para transferência.")
            return False
# Interface para o usuário        
print("-----------------------------------------------------------------------")
print("\t\tCriando a primeira conta:\t\t") 
print("-----------------------------------------------------------------------")

nome1 = input("Por favor, digite o nome do titular:")
saldo01 = float(input('Digite o saldo inicial:'))
codigo01 =  input('Código da Corrente - 01 | Código da Poupança - 02')


conta01 = ContaBancaria(nome1, saldo01, codigo01)

#criando a segunda conta - são necessárias duas contas para a transferência bancária!
#intrface para usuário
print("-----------------------------------------------------------------------")
print("\t\tCriando a segunda conta:\t\t") 
print("-----------------------------------------------------------------------")

nome2 = input('Por favor, digite o nome do titular:')
saldo02 = float(input('Digite o saldo inicial:'))
codigo02 = input('Código da Corrente - 01 | Código da Poupança - 02:')

conta02 = ContaBancaria(nome2, saldo02, codigo02)

print("Realizando Transferência Bancária - Por favor, aguarde...")

valorTransferido = float(input(f"Quanto deseja transferir para a conta de {conta01.titular} para a conta de {conta02.titular}?".format(conta01,conta02)))
conta01.transferir(valorTransferido,conta02)

###### Mostrando resultados finais:

print(f"\nSaldo final de: {conta01.titular}".format(conta01.saldo))
print(f"Saldo final de: {conta02.titular}".format(conta02.saldo))