n1=float(input('Insira  a priemira nota: '))
n2=float(input('insira a segunda nota: '))
media=(n1+n2)/2
if media <=9:
    print('Reprovado com {}'.format(media))
    print('Para o Ano tem mais!')
elif media <= 13:
    print('Aprovado com {}'.format(media))
    print('Melhor se preparar para o exame!')
elif media >14:
    print('Dispensado com {}'.format(media))
    print('Parabens!')