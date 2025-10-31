import streamlit as st

# ================= Bomba =================
class Bomba:
    def __init__(self, tipocombustivel, valor_litro, qtdcombustivel):
        self.tipocombustivel = tipocombustivel
        self.valorlitro = valor_litro
        self.qtdcombustivel = qtdcombustivel

    def situacaodaBomba(self):
        st.write("---| Bomba Nosso Posto |---")
        st.write(f"Combustível: {self.tipocombustivel}")
        st.write(f"Valor do litro: R$ {self.valorlitro}")
        st.write(f"Quantidade restante: {self.qtdcombustivel} litros")
        st.write("---------------------------")

    def abastecerValor(self, valor):
        litros = valor / self.valorlitro
        if litros > self.qtdcombustivel:
            st.warning("Não existe essa quantidade de litros na bomba!")
            return 0
        else:
            self.qtdcombustivel -= litros
            st.success(f"Valor abastecido: R$ {valor}")
            st.success(f"Litros abastecidos: {litros:.2f}")
            return litros

    def abastecerLitro(self, litros):
        if litros > self.qtdcombustivel:
            st.warning("Não existe essa quantidade de combustível na bomba!")
            return 0
        else:
            valor = litros * self.valorlitro
            self.qtdcombustivel -= litros
            st.success(f"Litros abastecidos: {litros}")
            st.success(f"Valor a pagar: R$ {valor:.2f}")
            return valor

# ================= Veículo =================
class Veiculo:
    def __init__(self, vTotal, vAtual, cor, marca, modelo, tipo_comb, potencia, cambio, nmr_portas):
        self.vTotal = vTotal
        self.vAtual = vAtual
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.tipo_comb = tipo_comb
        self.potencia = potencia
        self.cambio = cambio
        self.nmr_portas = nmr_portas

    def mostrarCaracteristicasVeiculo(self):
        st.write("---| Detalhes do Veículo |---")
        st.write(f"Cor: {self.cor}")
        st.write(f"Marca: {self.marca}")
        st.write(f"Modelo: {self.modelo}")
        st.write(f"Tipo Combustível: {self.tipo_comb}")
        st.write(f"Potência: {self.potencia}")
        st.write(f"Câmbio: {self.cambio}")
        st.write(f"Número de portas: {self.nmr_portas}")
        st.write(f"Tanque atual: {self.vAtual}/{self.vTotal} litros")
        st.write("---------------------------")

    def abastecer(self, litros, bomba: Bomba):
        capacidadeDisp = self.vTotal - self.vAtual
        if litros <= 0:
            st.warning("Informe uma quantidade positiva de litros!")
            return
        if litros > bomba.qtdcombustivel:
            st.warning("Combustível insuficiente na bomba.")
            return
        if litros > capacidadeDisp:
            st.warning(f"Tanque só comporta {capacidadeDisp:.2f} litros disponíveis.")
            return
        self.vAtual += litros
        bomba.qtdcombustivel -= litros
        valor = litros * bomba.valorlitro
        st.success(f"Foram abastecidos {litros} litros. Valor: R$ {valor:.2f}")
        st.info(f"O tanque agora possui {self.vAtual:.2f}/{self.vTotal} litros.")

# ================= Streamlit =================
st.title("Posto de Combustível Nossa Senhora de Fátima")

# Criando objetos
bomba1 = Bomba("Gasolina", 5.79, 1000)
carro1 = Veiculo(60, 0, "Branco", "Toyota", "Corolla", "Flex", "180cv", "Automático", 4)

# Mostrar situação da bomba
st.subheader("Situação da Bomba")
bomba1.situacaodaBomba()

# Mostrar características do veículo
st.subheader("Veículo")
carro1.mostrarCaracteristicasVeiculo()

# Formulário de abastecimento
st.subheader("Abastecer Veículo")
litros_abastecer = st.number_input("Quantos litros você deseja abastecer?", min_value=0.0, step=1.0)
if st.button("Abastecer"):
    carro1.abastecer(litros_abastecer, bomba1)
    st.subheader("Nova situação da Bomba")
    bomba1.situacaodaBomba()
    st.subheader("Novo status do veículo")
    carro1.mostrarCaracteristicasVeiculo()
