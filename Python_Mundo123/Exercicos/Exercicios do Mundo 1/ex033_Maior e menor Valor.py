a=int(input('Insira o primeiro numero: '))
b=int(input('Insira o segundo numero: '))
c=int(input('Insira o terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print('O menor valor digitado foi {}'.format(menor))

maior = a
if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c
print('O maior valor inserido foi {}'.format(maior))