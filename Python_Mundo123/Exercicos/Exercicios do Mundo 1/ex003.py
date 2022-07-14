#Crie um progrma que leia dois valores e mostre a soma entre eles.
n1 = int(input("\033[0;33m Degite um valor :\033[0;33m"))
n2 = int(input('\033[0;33m Degite outro valor:\033[0;33m'))
soma = n1+n2
print('\033[0;32m A soma entre \033[m'
      ' \033[0;35m {} \033[0;35m '
      '\033[0;32m e \033[0;32m \033[0;31m{} \033[0;31m \033[0;32m é igual a '
      '\033[0;34m {}!'.format(n1,n2,soma))
