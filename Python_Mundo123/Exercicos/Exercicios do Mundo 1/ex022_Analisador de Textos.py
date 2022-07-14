#Crei um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas e minusculas.
#Quantas letras ao todo (sem considerara espaçoes)
#Quantas letras tem o primeiro nome.
#************************************************************************
nome=str(input('Degite o seu nome completo:')).strip()
print('...Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('O seu primeiro nome tem {} letras '.format(nome.find(' ')))
separador=nome.split()
print('O seu primeiro é {} e tem {} letras'.format(separador[0],len(separador[0])))
