class Figurinha:
    def __init__(self,tema, dimensoes,bordao,material,numero=0):
        self.tema = tema
        self.numero = numero 
        self.material = material 
        self.dimensoes = dimensoes
        self.bordao = bordao
        
## exibindo a figurinha   
##este método me retorna o tema, numero, dimensoes e o bordao do jogador.   
    def mostrar(self):
     return(
        f'Tema:{self.tema}\n'
        f"Numero: {self.numero}\n"
        f"Material:{self.material}\n"
        f"Dimensoes:{self.dimensoes}\n"
        f"Bordão:{self.bordao}\n"
    )
     

#classe Pacotinho - responssável por guardar varias figurinhas:
class Pacotinho:
    ## inicialiando uma lista vazia
    def __init__(self,figurinhas = []):
        self.figurinhas = []  
    #usando o append coloco itens no final de uma lista vazia:
    def adicionarFigurinha(self, figurinha): 
            self.figurinhas.append(figurinha)
            
    ##! for vai percorrer cada elemento da lista e vai guardar temporariamente em F:
    def listar(self):
        for f in self.figurinhas:
            ##! impressao do elemento presente em f:
            print(f.mostrar())


class MinhaColecao:
    ##incicializa uma lista vazia:
    def __init__(self):
        self.colecao = []
    
    
    def colar(self,figurinha):
        ##este Append sera usado para guardar somente o numero da figura:
        self.colecao.append(figurinha.numero)  
        
        
    def figuras_faltantes(self):
        total = 10
        ##faz a diferenca das figuras, tais quais, imprime o total de figuras que faltam para colar:
        return total - len(self.colecao)  
        
 #criando as figurinhas com nome,numero, BORDAO, MATERIAL E DIMENSOES:
figura01 = Figurinha(
    tema="Lionel Messi",
    dimensoes="20x20", 
    bordao="GOAT",
    material="Papel", 
    numero="77")

figura02 = Figurinha(
    tema="Cristiano Ronaldo",
    dimensoes="20x20",
    bordao="SIIIII", 
    material="Papel",
    numero= "07" )

figura03 = Figurinha(
    tema="Neymar Jr.", 
    dimensoes="20x20",
    bordao="Tudo nosso, nada deles!", 
    material="Papel", 
    numero="09" )


##criando o pacote e add as figuras:
pacote = Pacotinho()
##aqui eu add a figura01 no pacote:
##Da mesma forma vou add as demasis figurinhas:
pacote.adicionarFigurinha(figura01)
pacote.adicionarFigurinha(figura02)
pacote.adicionarFigurinha(figura03)


################################### MOSTRANDO AS FIGURAS PRESENTES NO PACOTINHO ###################################
print("---------------------------\n")
print("Figuras dentro do pacotinho\t")
print("---------------------------\n")
pacote.listar()  
#################################################################################################################


##criando uma colecao - denominada "colecao01"
colecao01 = MinhaColecao()
##colando as figurinhas:

colecao01.colar(figura02)
colecao01.colar(figura03)
##colando as figurinhas:

colecao01.colar(figura01)
print("Ainda faltam colar: ", colecao01.figuras_faltantes())

###########################################################################################################

print(colecao01.colecao)


        
        
    
                     
