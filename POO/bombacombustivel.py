class Bomba:
    def __init__(self,tipocombustivel, qtdcombustivel,valorlitro = 0  ):
        self.__tipocombustivel = tipocombustivel
        self.__valorlitro = valorlitro
        self.__qtdcombustivel = qtdcombustivel
   
    def tipocombutivel(self):
        return self.__tipocombustivel
    
    def tipo_combustivel(self, novo_tipo):
        self.__tipo_combustivel = novo_tipo
    
    
    def qtdcombustivel(self):
        return self.__qtd_combustivel
   
    def qtdcombustivel(self, nova_qtd):
        self.__qtd_combustivel = nova_qtd

    def valorlitro(self):
        return self.__valor_litro

    def valorlitro(self, novo_valor):
        self.__valorlitro = novo_valor
   
   
    ##! f. abastecer pelo valor dado pelo usuario:
    def abastecerValor(self, valor):
        
        litros = valor / self.__valorlitro
        
        if litros > self.__qtdcombustivel:
            print("Nao existe essa quantidade de litros!\n")
            return 0
        else:
            self.__qtdcombustivel -= litros
            print(f"Valor abastecido: R$ {valor}\n")
            print(f"Litros: {litros}\n")
        return litros

    def abastecerLitro(self, litros):
        if litros > self.__qtdcombustivel:
            print("Não existe essa quantidade de combustivel na bomba\n")
            return
    ##* preço de compra
        valor = litros * self.__valorlitro
        
        self.__qtdcombustivel   -= litros
        print(f"Quantidade de litros que foram abastecidos: {litros}\n")
        print(f"Valor Para Pagar: {valor}\n")
        return valor
        
    ##! f. alterar o valor do litro:    
    def alterarvalorlitro(self, novovalor):
      self.__valorlitro = novovalor
      print(f"Valor do litro pós alteração: {self.__valorlitro}\n")
      
      ##! f. alterar o combustivel:
    def alterarCombustivel(self,novocombustivel): 
         self.__tipocombustivel = novocombustivel
         print(f"Novo combustivel: {self.__tipocombustivel}\n") 
        
     ##! f. alterar o combustivel prsente na bomba:
    def alterarQuantidadeCombutivel(self, nvQuant):
        self.__qtdcombustivel = nvQuant
        print(f"A nova quantidade de combustivel presente na bomba é: {self.__qtdcombustivel}\n")
    
    ##! situacao final da bomba de combustivel:
    def situacaodaBomba(self):
        print("---| Bomba Nosso Posto |----\n")
        print(f"Tipagem do Combustivel: {self.__tipocombustivel}\n")
        print(f"Valor ao Litro: {self.__valorlitro}\n")
        print(f"Quantidade restante na bomba:{self.__qtdcombustivel} litros\n")
        print("-------------------------------")
    
    ##? criando um objt qlqr:     
bomba1 = Bomba("Alcool", 6.50, 1000)


## testando tudo q for possivel testar:
print("--------- TODOS OS TESTES FEITOS -------------\n")


print("== ABASTECENDO POR VALOR ==")
bomba1.abastecerValor(10)

print("== ABASTECENDO POR LITRO ==")
bomba1.abastecerLitro(25)

print("== ALTERANDO O VALOR DO LITRO DE COMBUSTIVEL ==\n")
bomba1.alterarvalorlitro(8.00)

print("== ALTERANDO O COMBUSTIVEL -> Gasosa p/ Etanol ==\n")
bomba1.alterarCombustivel("Etanol")

print("== ALTERANDO A QUNTD. COMBUSTIVEL ==\n")
bomba1.alterarQuantidadeCombutivel(2000)

print("----- SITUAÇÃO FINAL DA BOMBA DE COMBUSTIVEL -----\n")
bomba1.situacaodaBomba()


#########################

class Veiculo:

    def __init__(self, vTotal, vAtual):
        self.__vTotal = vTotal
        self.__vAtual = vAtual

    def caracteristicasVeiculo(self, cor, marca, modelo, tipo_comb, potencia, cambio, nmr_portas, capc_tanq=0, ano_fab=0, tamanho=0):
        self.cor =  "Branco"
        self.marca = "Toyota"
        self.modelo = "Corolla"
        self.tipo_comb = "Flex"
        self.potencia = "Azul"
        self.cambio = "Automatico"
        self.nmr_portas = 4
        

    def mostrarCaracteristicasVeiculo(self):
        print("---| Detalhes do Veículo |----")
        print(f"Cor: {self.cor}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo Combustível: {self.tipo_comb}")
        print(f"Potência: {self.potencia}")
        print("-------------------------------\n")

    def abastecer(self, litros, bomba):
        capacidadeDisp = self.__vTotal - self.__vAtual

        if litros <= 0:
            print("Quantidade positiva, por favor!!!!!!!!!")
            return

        if litros > bomba.qtdcombustivel:
            print("Impossível abastecer: combustível insuficiente na bomba.")
            return

        elif self.__vAtual + litros > self.__vTotal:
            print(f"Impossível abastecer: o tanque comporta apenas {capacidadeDisp:.2f} litros disponíveis.")
            return
        else:
            bomba.qtdcombustivel -= litros
            self.__vAtual += litros
            valor = litros * bomba.valorlitro
            print(f"Foram abastecidos {litros} litros. Valor: R$ {valor:.2f}")
            print(f"O tanque agora possui {self.__vAtual:.2f} litros.\n")

bomba2 = Bomba("Gasolina", 5.79, 1000)
bomba2.situacaodaBomba()

##criando um carro qualquer:

carro01 = Veiculo(60,10)
carro01.caracteristicasVeiculo(cor="Branco",marca="Toyota", modelo="GLI", tipo_comb="ALCOOL", potencia="180cv", cambio="Automatico", nmr_portas=4)
carro01.mostrarCaracteristicasVeiculo()
##abastecendo o carrin

carro01.abastecer(12, bomba2)

##vendo a situacao da bomba 2

bomba2.situacaodaBomba()

    
        
        
        
     
                
        
 
    
    


    
        
        
        
