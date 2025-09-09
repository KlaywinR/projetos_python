## escrevendo um conversor de medidas 
print("\t\t__________________________________________________________________________________\t\t")
centimetros = int(input('Digite o total de centimetros que deseja converter para metros: '))
metros = float(input('Digite o total de metros que deseja converter para centimetros:'))
milimetros = float(input('Digite o total de metros que deseja converter para milímetros:'))
decam = int(input('Digite o valor em metros que deseja converter para decâmetros:'))

print("\t\t__________________________________________________________________________________\t\t")
print("Os centimetros digitados são equivalentes a: {}" .format(centimetros / 100))
print("Os metros digitados são equivalentes a: {} centimetros.".format(metros * 100))
print("Os metros digitados são equivalentes a: {} milímetros".format(metros / 1000))
print("Os metros digitados são equivalentes a: {} decâmetros".format(metros * 10))
print("\t\t__________________________________________________________________________________\t\t")



