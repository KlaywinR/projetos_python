class Aluno:
    def __init__(self,nome,matricula,nota=0):
        self.nome = nome
        self.nota = nota 
        self.matricula = matricula
        
    def mostrarAluno(self):
         return(
             f"--Mostrando Aluno--"
             f"Nome:{self.nome}\n"
             f"Nota:{self.nota}\n"
             f"Numero Matricula:{self.matricula}\n"
         ) 
         
    def foi_aprovado(self):
##! se a nota for maior ou igual a 6 o aluno é aprovado; caso contrario - reprovado.
        if self.nota >= 6:
            print(f"Aluno:{self.nome} Aprovado!")
            return True
        else:
            print(f"Aluno: {self.nome} reprovado!")
            return False

class Professor:
    def __init__(self,nome,disciplina,formação):
        self.nome = nome 
        self.disciplina = disciplina
    ## lista vazia dos discentes:
        self.discentes = []
        self.formação = formação

    def mostrarProfessor(self):
        return(
        f'NOME: {self.nome}\n'
        f'FORMACAO ACADEMICA: {self.formação}\n'
        f'Disciplina:{self.disciplina}\n'
        f'Discentes:{self.discentes}\n' 
            
        )
    def adicionarAluno(self, aluno):
        self.discentes.append(aluno)
        
        
    def mediaTurma(self):
        ##! me retorna quantos alunos existem na lista:
        if len(self.discentes) == 0:
            return 0
        ##! percorre cada alino da lista e pega sua nota:
        total = sum(aluno.nota for aluno in self.discentes)
        ##! neste caso, acima temos o sum - responsáve pela soma de nota dos discentes;
        ##! apos isso ele me retorna o total do vlor das notas e me faz a media - assim, me mandando a media da turma:
        return total / len(self.discentes)
         
    def aprovados(self):
        #! cria  uma lista nova , percorre todos os discentes - tal qual, iclui somente os
        #! aprovados e me retorna a lsita de aprovados 
        return[aluno for aluno in self.discentes if aluno.foi_aprovado()]
    
##! 
##? 
##*


class Escolaa:
    def __init__(self):
        self.professores = []
        
    def AddProfessor(self,professor):
        self.professores.append(professor)
        
    def Relatorio(self):
        print("=== Relatório Geral da Escola ===")
        #percorre os professores presentes na escola - le a quant de discentes na liista e o valor e armazenado
        #em quantdade de alunos; 
        for prof in self.professores:
            quantidade_alunos = len(prof.discentes)
            media = prof.mediaTurma()
            print(f"Professor: {prof.nome}")
            print(f"Quantidade de alunos: {quantidade_alunos}")
            print(f"Média da turma: {media:.2f}\n")
            
###################################################################################################################
##criando os alunos 
aluno1 = Aluno("Antonieta", matricula="2025665527",nota=7)
aluno2 = Aluno("Joao Maria",matricula="2025665527", nota=10)
aluno3 = Aluno("Marina", matricula="2025665527",nota=5)
aluno4 = Aluno("Henrique", matricula="2025665527",nota=10)

##criando o primeiro professor:

p01 = Professor(nome="Demetrios Coutinho", disciplina="POO", formação="Doutor")
##adicionando os alunos ao professor Demetrios:
p01.adicionarAluno(aluno1)
p01.adicionarAluno(aluno2)

p02 = Professor(nome="Aluisio Rego", disciplina="Algoritmos", formação="Doutor")
##adicionando os alunos ao professor ALUISIO:
p02.adicionarAluno(aluno3)
p02.adicionarAluno(aluno4)


#############criando a escola e add os profesores: ##################

escola = Escolaa()
##adicionei Demetrios e Aluisio nesta escola:
escola.AddProfessor(p01)
escola.AddProfessor(p02)


#relatorio final da escola:

escola.Relatorio()

#aprovados de determinado professor - Dmetrios ou Aluisio

print('APROVADOS DE DEMETRIOS:')
for alunos in p01.aprovados():
    print(alunos.nome)
        
print('APROVADOS DE ALUISIO:')
for alunos in p02.aprovados():
    print(alunos.nome)
               




      
     
        
         
         
        
        
        
