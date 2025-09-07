## Programa desenvolvido para obter todas as informações possiveis de algo digitadio pelo usuário:

numero = input('Digite algo: ')

print('O que foi digitado foi: {}'.format(numero))

print("É numerico?", numero.isnumeric())
print("É string?" , numero.isdecimal())
print("Possui letras?", numero.isalpha())
print("É alfanumérico?", numero.isalnum())
