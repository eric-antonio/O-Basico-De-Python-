""""def l():
    print(f'\033[0;33m -=\033[m'*10)
l()
print(f'Curso em Video'.center(25))
l()

#Função com parametro
msg = str(input(f'Insira o texto: '))
def mensagem(msg):
    print(f'\033[0;33m -=\033[m' * 10)
    print(f'{msg}'.center(25))
    print(f'\033[0;33m -=\033[m' * 10)

mensagem(msg)"""

""""---Praticando---"""
""""---- Funçoes do Programa ----"""


def soma(a, b):
    som = a + b
    print(f' A soma de A + B = {som}')


def contador(*valoes):
    s = 0
    for i in valoes:
        s += i
    print(f'A soma dos valors {valoes} = {s}')



def dobra(lst):
    pos = 0
    print(f'A lista inicial {lst}')
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f'A lista dobrada {lst}')


""""---- Programa ----"""
soma(4, 5)
contador(4, 7, 7, 8)
valores = [3, 4, 5, 6, 7]
dobra(valores)
