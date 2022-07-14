from datetime import date
totmaior = 0
totmenor = 0
for i in  range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(i)))
    idade = date.today().year - nasc
    if idade >= 21:
       totmaior += 1
    else:
        totmenor += 1

print('O numero de pessoas maiores de idade é {}'.format(totmaior))
print('O numero de pessoas menores de idade é {}'.format(totmenor))