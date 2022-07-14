#Faça um programa que leia um frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posicao ela aparece a primeira vez.
#Em que posicao ela aparece a ultima vez.


palavra=str(input('Insira uma palavra: ')).strip().lower()
print('A letra A aparece {} vezes na frase '.format(palavra.count('a')))
print('A primeira letra A apareceu na posicao {}'.format(palavra.find('a')+1))
print('A letra A apareceu na posicao {} pela ultima vez'.format(palavra.rfind('a')+1))