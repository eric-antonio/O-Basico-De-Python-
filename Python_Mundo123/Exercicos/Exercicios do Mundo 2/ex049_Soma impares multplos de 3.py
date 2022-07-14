#Faça um programa que calcule a soma entre todos os numeros
# impares que são multiplos de tres que se encontram
# no intervalo de 1 ate 500

soma=0
cont=0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print('A soma de todos os {} valores solicitados é de :{}'.format(cont,soma))
