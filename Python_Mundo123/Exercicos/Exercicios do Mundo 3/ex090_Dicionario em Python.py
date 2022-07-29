""" estudantes = dict()  """
estudantes = dict()

nome = str(input(f'Nome: '))
estudantes['nome'] = nome
media = float(input(f'Média de {nome}: '))
estudantes['média'] = media
if media <= 9.5:
    estudantes['situação'] = 'Excluiu a cadeira!'
    #print(f'Excluiu a cadeira!')
elif media <= 13:
    estudantes['situação'] = 'Vai ao Exame'
   #print(f'Vai ao exame')
elif media >= 14 and media <= 19.5:
    estudantes['situação'] = 'Dispensado!'
    #print(f'Dispensado!')
elif media >= 20:
    estudantes['situação'] = 'Com situção academica Inregular...'
print(f'*'*30)
for k, v in estudantes.items():
    print(f'- {k}: {v}')