from datetime import date
ano = int(input('\033[0;33m Insira o seu ano de nascimento: \033[m: '))
idade = date.today().year - ano

if idade < 9:

    print('Categoria Mirim')

elif idade <= 14:

    print('Categoria Infantil')

elif idade <=19:

    print('Categoria Junior')

elif idade <= 25:

    print('Categoria Senior')
elif idade > 25:

    print('Categoria Mestre')