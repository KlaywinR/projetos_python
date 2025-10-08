
print("___________________________________________\n")
quant = int(input("Quantas somas você deseja fazer?"))
print("_____________________________________________")
soma = 0

for n in range(1, quant+1):
    num = int(input(f"Informe o valor da peça: {n}/{quant} R$:".format(n, quant)))
    soma = soma + num
print("_____________________________________________\n")
print(f"O valor total das peças de roupas são: {soma}".format(soma))
print("_____________________________________________")   