def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0,formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    #Mesmo comadndo so de forma diferente!
    return res if not formato else moeda(res)


def metade(preco=0,formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='MT'):
    return f'{preco:.2f}{moeda}'.replace('.', ',')


def resumo(preco=0, aumento=10, reducao=5, fomato=False):

    print('\033[0;33m-\033[m'*30)
    print(f'Sistema Resumido'.center(30))
    print('\033[0;33m-\033[m'*30)

    m = metade(preco, moeda)
    a = aumentar(preco, aumento, True)
    r = diminuir(preco, reducao, True)
    d = dobro(preco, True)
    print(f'A metade de {preco} é {m} \n'
          f'O dobro de {preco} é {d} \n'
          f'Aumentando {aumento}% temos {a}\n'
          f'Diminuindo {reducao}% temos {r}')
    print('\033[0;33m-\033[m' * 30)