def notas(*n, sit=False):
    """"
            Configuração Para As Avaliações!
            Média = 13.5 Dispensado
            Média = 9.5-----13.4 Vai ao Exame!
            Média = 9.4 Reprovado
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 13.5:
            r['situação'] = 'Dispensado'
        elif 9.5 <= r['media'] < 14:
            r['situação'] = 'Estudante tem Exame'
        elif r['media'] <= 9.4:
            r['situação'] = 'Excluido!'

    return r


resp = notas(17, 15, 8.4, sit=True)
print(resp)
help(notas)