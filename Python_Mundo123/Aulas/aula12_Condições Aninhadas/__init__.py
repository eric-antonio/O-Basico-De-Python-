nome = str(input('\033[0;32m Qual é o seu nome? : '))
if nome == 'Éric':
    print(' \033[0;33m Que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('\033[0;36m Seu nome é muito pupular em Moz!')
elif nome in 'Jessica Bianca Ana Juliana':
    print('\033[0;35m Sua gostosa!')
else:
    print('\033[0;32m Prazer em te conhecer!. \033!')

print('\033[0;32m Tenha um bom dia,\033[m\033[0;36m{}!'.format(nome))