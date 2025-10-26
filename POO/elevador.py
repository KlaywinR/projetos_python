class Elevador:
#----Todos os valores sao  zerados, apos inicializar que serao definidos os valores
    def __init__(self):
        self.__andar_atual = 0
        self.__total_andares = 0
        self.__capacidade = 0
        self.__pessoas_presentes = 0
        
# --------------------------- inicializar elevador - definicao de quantidades:
    def inicializar(self, capacidade: int, total_andares: int) -> None:
        self.set_capacidade(capacidade)
        self.set_total_andares(total_andares)
        
#--------------------------- met publicos
#- Chama metdodo privado em cada caso - acessiveis fora de classe.
    def entrar(self) -> None:
        if self.__tem_espaco():
            self.__pessoas_presentes += 1
            print("Mensagem: Uma pessoa entrou.")
            print("Quantidade de pessoas presentes:", self.__pessoas_presentes)
        else:
            print("Não há como adentrar ao elevador, capacidade máxima excedida.")

    def sair(self) -> None:
        if self.__tem_gente():
            self.__pessoas_presentes -= 1
            print("Mensagem: Uma pessoa saiu.")
            print("Quantidade de pessoas presentes:", self.__pessoas_presentes)
        else:
            print("Erro: elevador vazio!")

    def subir(self) -> None:
        if self.__pode_subir():
            self.__andar_atual += 1
            print("Subiu para o andar:", self.__andar_atual)
        else:
            print("Mensagem de Erro: já se encontra no último andar!")

    def descer(self) -> None:
        if self.__pode_descer():
            self.__andar_atual -= 1
            print("Desceu para o andar:", self.__andar_atual)
        else:
            print("Erro: já está no térreo!")

#------------------------------------------------------ metd. privados
#- A ação é possivel?
    def __tem_espaco(self) -> bool:
        return self.__pessoas_presentes < self.__capacidade

    def __tem_gente(self) -> bool:
        return self.__pessoas_presentes > 0

    def __pode_subir(self) -> bool:
        return self.__andar_atual < self.__total_andares

    def __pode_descer(self) -> bool:
        return self.__andar_atual > 0

#--------------------------------------------- gets e seters
    def get_andar_atual(self) -> int:
        return self.__andar_atual
# só muda o andar caso seja um valor válido 
    def set_andar_atual(self, novo_andar: int) -> None:
        if 0 <= novo_andar <= self.__total_andares:
            self.__andar_atual = novo_andar
        else:
            print("Erro: andar inválido!")

    def get_total_andares(self) -> int:
        return self.__total_andares
#- Só é aceito valores maiores do que zero:
    def set_total_andares(self, total: int) -> None:
        if total >= 0:
            self.__total_andares = total
        else:
            print("Erro: total de andares inválido!")
                
#-Impedimento de valores inválidos 
    def get_capacidade(self) -> int:
        return self.__capacidade

    def set_capacidade(self, capacidade: int) -> None:
        if capacidade > 0:
            self.__capacidade = capacidade
        else:
            print("Erro: capacidade inválida!")

    def get_pessoas_presentes(self) -> int:
        return self.__pessoas_presentes

#caso as pessoas estejam dentro do limite = aceitas -> erro
    def set_pessoas_presentes(self, pessoas: int) -> None:
        if 0 <= pessoas <= self.__capacidade:
            self.__pessoas_presentes = pessoas
        else:
            print("Erro: quantidade de pessoas inválida!")


##tests
elevador01 = Elevador()
elevador01.inicializar(3, 5)

# exceder capacidade maxima:
elevador01.entrar()
#elevador01.entrar()
##elevador01.entrar()
##elevador01.entrar()  # Erro: lotado

#indo ao limite de andarees
elevador01.subir()
##elevador01.subir()
##elevador01.subir()
##elevador01.subir()
##elevador01.subir()  # Erro: último andar

# saiindo ate ficar vazio
elevador01.sair()
##elevador01.sair()
##elevador01.sair()
##elevador01.sair()  # Erro: vazio

#estado atual
print("Andar atual:", elevador01.get_andar_atual())
print("Pessoas presentes:", elevador01.get_pessoas_presentes())

#-- AMBOS SERAO erros; excedem valores.
##elevador01.set_capacidade(0)          # Erro
##elevador01.set_total_andares(-1)      # Erro
##elevador01.set_pessoas_presentes(10)  # Erro


