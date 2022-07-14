from datetime import date
atual = date.today().year
nasc = int(input('Ano de mascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))

if idade == 18:
    print('Diraja-se imediatemente para se alistra!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Voce ainda n tem 18 Anos! ainda faltam {} anos!'.format(saldo))
    print('Seu alistamento sera em {}'.format(ano))
elif idade >18:
    saldo = idade -18
    ano = atual - saldo
    print('Voce ja devia ter se alistado a {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))