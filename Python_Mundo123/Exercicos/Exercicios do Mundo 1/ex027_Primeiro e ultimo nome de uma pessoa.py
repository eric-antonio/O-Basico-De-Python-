#Faça um programa que receba um nome
# via teclado e exiba o primeiro e ultimo nome.

nome=str(input('Degite o seu nome completo: ')).strip()
n=nome.split()
print('Analisando seu nome.....')
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é : {}'.format(n[0]))
print('O seu ultimo nome é {} '.format(n[len(n)-1]))
