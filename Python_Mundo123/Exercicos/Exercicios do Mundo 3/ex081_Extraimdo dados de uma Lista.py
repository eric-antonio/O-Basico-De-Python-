lista = list()
while True:
    lista.append(int(input(f'\033[0;32m Insira um valor: \033[m')))
    res = str(input(f'\033[0;33m Quer continuar? [S/N] : \033[M')).lower()[0]

    if res == 'n':
        break
print(f'\033[0;34m Voce digitou: {len(lista)} elementos.')
lista.reverse()
print(f'\033[0;35m Os valores e ordem decrescente são: {lista}\033[m')
if 5 not in lista:
    print(f'\033[0;31m O valore {5} não foi encontrado!\033[m')
else:
    print(f'\033[0;35m O valor 5 foi encontardo na posição {lista.index(5)}\033[m')