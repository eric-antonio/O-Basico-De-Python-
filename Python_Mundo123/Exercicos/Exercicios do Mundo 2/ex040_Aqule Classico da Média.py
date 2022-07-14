nome = str(input('\033[0;34m Insira o nome do/a aluno/a: '))
nota1 = float(input('\033[0;33m Insira a nota da priméira avaliação:'))
nota2 = float(input(' Insira a nota da segunda avaloção:'))
nota3 = float(input(' Insira a nota da Terceira avalição:\033[m'))

media = (nota1 + nota2 + nota3)/3

if media >=14:
    print('\033[0;36m O/A aluno/a foi {} dispensou com media {}'.format(nome,media))
elif media <= 13 and media >=10:
    print('\033[0;35m O/A aluno/a {} vai ao Exame com {}'.format(nome,media))
elif media <10:
    print('\033[0;31m O/A aluno/a {} foi reprovado com {:.2f}'.format(nome,media))


