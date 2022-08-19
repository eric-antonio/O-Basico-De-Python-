def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f' Com {idade} anos em Moçambique!\n' \
               f'\033[0;31m Não vota!\033[m'
    elif idade >= 65:
        return f' Com {idade} anos em Moçambique!\n' \
               f'\033[0;33m Voto é Opcional! \033[m'
    elif idade >= 18 < 65:
        return f' Com {idade} anos em Moçambique!\n' \
               f'\033[0;32m Votó Obrigatorio!\033[m'


ano = int(input(f'Insira o ano em que nasceu: '))
print(voto(ano))
