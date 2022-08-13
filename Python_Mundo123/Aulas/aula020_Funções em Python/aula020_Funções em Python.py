def l():
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

mensagem(msg)