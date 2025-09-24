class ContaBancaria:
    def __init__(self, titular, saldo=0, codigo_Apo='01'):
        self.titular = titular
        self.saldo = saldo
        self.codigo_Apo = codigo_Apo
        self.nome_Apo = "Conta Corrente" if codigo_Apo == '01' else "Poupança"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso! Saldo atual: {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            print(f"Transferência de {valor} para {conta_destino.titular} realizada com sucesso!")
            return True
        else:
            print("Saldo insuficiente para transferência.")
            return False

print("Criando a primeira conta:")

nome1 = input("Digite o nome do titular: ")
saldo01 = float(input('Digite o saldo inicial:'))
codigo01 =  input('Código da Corrente - 01 | Código da Poupança - 02')

conta01 = ContaBancaria(nome1, saldo01, codigo01)

print("Criando a segunda conta:")
nome2 = input('Digite o nome do titular:')
saldo02 = float(input('Digite o saldo inicial'))
codigo02 = input('Código da Corrente - 01 | Código da Poupança - 02')

conta02 = ContaBancaria(nome2, saldo02, codigo02)

print("Realizando Transferência")

valorTransferido = float(input("Quanto deseja trasnferir para a conta de {conta01.titular} para a conta {conta02.titular}?"))
conta01.transferir(valorTransferido,conta02)

######

print(f"\nSaldo final de {conta01.titular}: {conta01.saldo}")
print(f"Saldo final de {conta02.titular}: {conta02.saldo}")