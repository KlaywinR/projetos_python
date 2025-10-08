numero01 = int(input("Digite um primeiro numero inteiro:"))

numero02 = int(input("Digite um segundo numero inteiro:"))

if numero01 > numero02:
    print(f"O {numero01} é maior que o {numero02} numero!".format(numero01))
elif numero02 > numero01:
    print(f"O {numero02} é maior que o {numero01}!".format(numero02))
else:
    print("os numeros sao iguais")
    