#Faça um programa que leia um numero de 0 a 9999 e mostre na tela
#cada um dos digitos separados.
#Ex: Digite um numeo: 1834
#unidade:4 dezena 3 centena : 8 milhar :1

numero=int(input('Degite um numero: '))
u=numero//1%10
d=numero//10%10
c=numero//100%10
m=numero//1000%10

print('Analisasndo o numeo {}'.format(numero))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
