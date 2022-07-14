soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n !=999:
        soma += n
        cont +=1
print('Você digitou {} digitos e a soma entre ele foi de {}'.format(cont,soma))
