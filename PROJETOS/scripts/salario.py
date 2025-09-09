##salario - crie um sistema de salário bem interessante!

caixa01 = float(input('Caixa 01:Digite o valor do seu salário: '))
caixa01 = int(input('CAIXA 01: Digite a quantidade de atendimentos diários:  '))

caixa02 =  float(input('Caixa 02: Digite o valor do seu salário: '))
caixa01 = int(input('CAIXA 02: Digite a quantidade de atendimentos diários:  '))

media = caixa01 + caixa02 / 2

print("\t\t--------------------------------------------------------------------------------------------\t\t")
print("\t\t ************** DADOS FINAIS *****************\t\t")
print('\tA média de salários: {}'.format(media))

if(caixa01 >= 45):
 print("\tCAIXA 01 STATUS: Aumento Aprovado!\n O seu novo valor é de: {:.2f}\n".format(caixa01 * 1.45))
else:
 print("\tCAIXA 01 STATUS: Aumento não aprovado!")

if(caixa02 > 45):
     print("\tCAIXA 02 STATUS: Aumento Aprovado!\n O seu novo valor é de: {:.2f}\n".format(caixa02 *  1.45))
else: 
 print("\tCAIXA 02 STATUS: Aumento não aprovado!")

print("\t\t--------------------------------------------------------------------------------------------\t\t")

print("\t____________________________________________________________________________________________________________________________________________\t")
print("\t\t * CASO O CAIXA 01 FAÇA 45 ATENDIMENTOS DIÁRIOS SERÁ GRATIFICADO COM UM AUMENTO DE 25% NO SALÁRIO, CASO CONTRÁRIO NÃO RECEBE O AUMENTO* \t\t")
print("\t\t * CASO O CAIXA 02 FAÇA 45 ATENDIMENTOS DIÁRIOS SERÁ GRATIFICADO COM UM AUMENTO DE 25% NO SALÁRIO, CASO CONTRÁRIO NÃO RECEBE O AUMENTO* \t\t")
print("\t____________________________________________________________________________________________________________________________________________\t")

