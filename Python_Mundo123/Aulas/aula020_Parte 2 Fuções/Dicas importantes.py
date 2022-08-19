""""
    É um metodo usado para obter informaçoes em python:
    No console é so degitar help(), de seguida degiatar o comando ou simbolo
    que logo de seguida tera acessoa a sua Doc! ou
    No codigo é so : help(****).
"""

""""
        Docstings- permite com que crirmos uma documentacao para o nosso codigo!
"""
def fun(b):
    global a
    """ Sem a alinea acima teriamos duas variaveis um global e a 
    outra não. Prem agora apenas temos uma e unica variavel Global.
    Que ira receber um novo valor na alinea a baixo."""
    a = 4
    b += 4  # variavel a encrementa +4 no valor que lhe foi passada pela variavel a
    c = 2
    print(f'A local vale {a}')
    print(f'B local  vale {b}')
    print(f'C local vale {c}')


def somar(i=0, j=0, k=0):
    s = i + j + k
    return s
    """" Podemos passar o valore de retorno para uma 
    nova variavel ou simplesmente aplicar direto onde pretendemos!
    Porem é pratico e seguro passar para uma variavel:
    Ex:
        def soma(a, b, c):
             s = a + b c
             return s
        
        r1 = soma(3 + 4 + 5) 
             """


a = 2
print(f'A inicialmente valia {a}')

"""" a função recebe o valor da variavel a e passa para b"""
fun(a)

r1 = somar(4, 4, 4)
r2 = somar(6, 2, 4)
r3 = somar(9)
print(f'Os valores das somas foi de \n r1 = {r1} \n r2 = {r2} \n r3 = {r3}')

print()