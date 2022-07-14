soma = 0
media = 0
velho = 0
nvelho = ''
cont = 0
for i in range(1, 5):
    print('------- {}ª Pessoa------ '.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade

    if sexo == 'M':
        nvelho = nome
        if velho < idade:
            velho = idade

        if velho < idade:
            nvelho =nome


    if sexo == 'F':
        if idade < 20:
            cont += 1

media = soma / 4
print('A média de iadade foi de {} anos'.format(media))
print('O Homen mais velho tem {} Anos e se chama {}'.format(velho,nvelho))
print('Ao todo são {} mulheres com menos de 20 anos! '.format(cont))
