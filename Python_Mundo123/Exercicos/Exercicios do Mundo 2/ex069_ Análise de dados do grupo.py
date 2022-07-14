print("-"*20)
print('Cadastro de Pessoas!')
print("-"*20)
cont = 0
codicao = 1
masculino = femenino20 =  tot18 = 0

while True:

    idade = int(input('Insira a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Insira o Sexo[M/F]: ')).upper().strip()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F'and idade < 20:
        femenino20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if resposta == 'N':
        break

print(f'O total de individoous maiores de 18 são: {tot18} \n'
      f'Ao total existem {masculino} pessooas do sexo masculino \n'
      f'Existem ao todo {femenino20}   mulheres menosres de 20')