import math
numero = int(input("Digite um numero inteiro:"))

if numero > 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada do numero que voce digitou é: {raiz}".format(raiz))
else:
    print("Este numero e invalido no nosso sistema!")