
altura = int(input('Digite agora a altura da parede: '))
base = int(input('Digite agora a largura da parede: ')) ## largura_d_parede

area = altura * base

print("a area total é: {}".format(area))

### qntd_d_tnt_usada:

quantidade = area / 2 

print("A quantidade de litros de tinta necessários para a pintura completa são {} litros.".format(quantidade))