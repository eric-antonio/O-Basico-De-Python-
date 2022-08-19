def fatorial(n, show=False):
    """"
        -> Calcula o Fatorial de um numero!
        :param n: O numero a ser calculado.
        :param show: (Opcional) Mostra ou não a conta
        :return Ovalor de Factorial de um numero n.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print(fatorial(5, show=True))
print(help(fatorial))
