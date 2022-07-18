exp = str(input(f'Degite uma expressão : '))
pilha = list()
for sim in exp:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expressão está valida!')
else:
    print(f'Sua expressão esta errada!')
