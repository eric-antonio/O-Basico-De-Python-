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
