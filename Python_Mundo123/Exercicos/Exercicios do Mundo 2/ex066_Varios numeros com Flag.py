soma = cont = 0
while True:
    n = int(input('\033[0;32m Insira um numero: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f' \033[0;33m Você digitou '
      f'\033[0;34m{cont}\033[m'
      f'\033[0;33m numeros e a soma dele é de: '
      f'\033[0;34m{soma}\033[m')
print(f'Acabou...')