## programa desenvolvido com o intuito de descobrir a media de um determinado aluno do IFRN
nome_aluno = input('Qual o seu nome?')
matricula = input(f'Qual o numero da sua matrícula{nome_aluno}?')
curso = input(f'Qual o curso você deseja saber a média de notas {nome_aluno}?')

print(f"{nome_aluno}(a) Por favor, digite as suas notas no nosso sistema!")

nota01 = float(input('Qual foi a sua nota na primeira avaliação? (0 a 10)'))
nota02 = float(input('Qual foi a sua nota na segunda avaliação? (0 a 10)'))
nota03 = float(input('Qual foi a sua nota na terceira avaliação? (0 a 10)'))
nota04 = float(input('Qual foi a sua nota na quarta avaliação? (0 a 10)'))

notafinal = (nota01 + nota02) / 4

print(f"Nome do Aluno: {nome_aluno}\n",
      f"Sob Matrícula:{matricula}\n", 
      f"Discente do curso de:{curso}\n",
      f"A sua nota final eh:{notafinal}\n"
    )

if(notafinal >= 60):
    print("Discente Aprovado!")
else: print("Discente Reprovado.")





    
    


 