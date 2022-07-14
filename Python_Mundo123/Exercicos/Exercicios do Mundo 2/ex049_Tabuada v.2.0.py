numero = int(input('Insira um nmero para ver a sua tabuada!:'))
print('\033[0;33m Bem Vindo a Tabuada de: {} \033[m'.format(numero))
for i in range(1,13):
    print('{} * {} = {}'.format(numero, i, numero * i))
