class Bomba:
    def __init__(self, tipocombustivel, valorlitro, qtdcombustivel):
        self.__tipocombustivel = tipocombustivel
        self.__valorlitro = valorlitro
        self.__qtdcombustivel = qtdcombustivel

##lembrando q gets le o valor privdo e set altera o avlor 

    def get_tipocombustivel(self):
        return self.__tipocombustivel

    def get_valorlitro(self):
        return self.__valorlitro

    def get_qtdcombustivel(self):
        return self.__qtdcombustivel

    def set_tipocombustivel(self, novo_tipo):
        self.__tipocombustivel = novo_tipo

    def set_valorlitro(self, novo_valor):
        self.__valorlitro = novo_valor

    def set_qtdcombustivel(self, nova_qtd):
        self.__qtdcombustivel = nova_qtd

    
    def abastecerValor(self, valor):
        litros = valor / self.__valorlitro

## ve se o tanto de litros q a pessoa quer por tem na bomba de combustivel
        if litros > self.__qtdcombustivel:
            print("Nao existe essa quantidade de litros!\n")
            return 0
        else:
            self.__qtdcombustivel -= litros
            print(f"Valor abastecido: R$ {valor}")
            print(f"Litros: {litros:.2f}\n")
        return litros

    def abastecerLitro(self, litros):
        if litros > self.__qtdcombustivel:
            print("Não existe essa quantidade de combustivel na bomba\n")
            return

        valor = litros * self.__valorlitro
        self.__qtdcombustivel -= litros
        print(f"Quantidade abastecida: {litros} litros")
        print(f"Valor a pagar: R$ {valor:.2f}\n")
        return valor

    def alterarvalorlitro(self, novovalor):
        self.__valorlitro = novovalor
        print(f"Valor do litro pós alteração: {self.__valorlitro}\n")

    def alterarCombustivel(self, novocombustivel):
        self.__tipocombustivel = novocombustivel
        print(f"Novo combustivel: {self.__tipocombustivel}\n")

    def alterarQuantidadeCombutivel(self, nvQuant):
        self.__qtdcombustivel = nvQuant
        print(f"Nova quantidade de combustível: {self.__qtdcombustivel} litros\n")

    def situacaodaBomba(self):
        print("\n---| Bomba Nosso Posto |----")
        print(f"Tipo do Combustível: {self.__tipocombustivel}")
        print(f"Valor do Litro: R$ {self.__valorlitro:.2f}")
        print(f"Quantidade na Bomba: {self.__qtdcombustivel:.2f} litros")
        print("-------------------------------\n")


######################################################
class Veiculo:

    def __init__(self, vTotal, vAtual, cor, marca, modelo, tipo_comb, potencia, cambio, nmr_portas):
        self.__vTotal = vTotal
        self.__vAtual = vAtual
        self.cor =  cor 
        self.marca = marca
        self.modelo = modelo
        self.tipo_comb = tipo_comb
        self.potencia = potencia
        self.cambio = cambio
        self.nmr_portas = nmr_portas

    #### gests e setd
    def get_vTotal(self):
        return self.__vTotal

    def get_vAtual(self):
        return self.__vAtual

    def set_vAtual(self, novoValor):
        self.__vAtual = novoValor

    
    def caracteristicasVeiculo(self, cor, marca, modelo, tipo_comb, potencia, cambio, nmr_portas):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.tipo_comb = tipo_comb
        self.potencia = potencia
        self.cambio = cambio
        self.nmr_portas = nmr_portas

    def mostrarCaracteristicasVeiculo(self):
        print("---| Detalhes do Veículo |----")
        print(f"Cor: {self.cor}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo Combustível: {self.tipo_comb}")
        print(f"Potência: {self.potencia}")
        print(f"Câmbio: {self.cambio}")
        print(f"Número de Portas: {self.nmr_portas}")
        print("-------------------------------\n")

    def abastecer(self, litros, bomba: Bomba):
        capacidadeDisp = self.__vTotal - self.__vAtual

        if litros <= 0:
            print("Quantidade positiva, por favor!!!!!!!!!")
            return

        if litros > bomba.get_qtdcombustivel():
            print("Impossível abastecer: combustível insuficiente na bomba.")
            return

        elif self.__vAtual + litros > self.__vTotal:
            print(f"Impossível abastecer: o tanque comporta apenas {capacidadeDisp:.2f} litros disponíveis.")
            return
        else:
            bomba.set_qtdcombustivel(bomba.get_qtdcombustivel() - litros)
            self.__vAtual += litros
            valor = litros * bomba.get_valorlitro()
            print(f"Foram abastecidos {litros} litros. Valor: R$ {valor:.2f}")
            print(f"O tanque agora possui {self.__vAtual:.2f} litros.\n")



################# testes feitos:
print("Mostrando uma bomba 02:")
bomba2 = Bomba("Gasolina", 5.79, 1000)
bomba2.situacaodaBomba()

carro01 = Veiculo(40, 10, cor="Branco", marca="Toyota",modelo="Corolla", tipo_comb="Gasolina", potencia="180cv", cambio="Automático", nmr_portas=4)
carro01.caracteristicasVeiculo("Branco", "Toyota", "Corolla", "Gasolina", "180cv", "Automático", 4)
carro01.mostrarCaracteristicasVeiculo()

carro01.abastecer(12, bomba2)
bomba2.situacaodaBomba()

print("Mostrando uma bomba 01 :")
bomba01 = Bomba("Gasolina", 5.80, 1900)
bomba01.situacaodaBomba()

carro02 = Veiculo(45, 25, cor="Branco", marca="Toyota",modelo="SW4", tipo_comb="Gasolina", potencia="180cv", cambio="Automático", nmr_portas=4)
carro02.caracteristicasVeiculo("Branco", "Toyota", "Sw4", "Gasolina", "180cv", "Automático", 4)
carro02.mostrarCaracteristicasVeiculo()

carro02.abastecer(10, bomba2)
bomba2.situacaodaBomba()



