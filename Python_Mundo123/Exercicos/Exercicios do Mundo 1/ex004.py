#Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo
#e tdodas informações sobre ele.

a=input('Insira algo:')
print('Voce inseriu : {} e o seu tipo primitivo é : {}'.format(a,type(a)))
print('So tem espaços ? :{}'.format(a.isspace()))
print('É um numero ? : {}'.format(a.isnumeric()))
print('É alfabetico? :'.format(a.isalpha()))
print('É alfanumerico? : {}'.format(a.isalnum()))
print('Esta em maiusculas? : {}'.format(a.isupper()))
print('Esta em minusculas? : {}'.format(a.isupper()))
print('Esta em Capitalizada? : {}'.format(a.isupper()))