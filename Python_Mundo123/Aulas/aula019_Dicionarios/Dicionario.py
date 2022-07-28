"""" Para instanciar dados em Python é necessario Ter em conrta os fundamentos anteriores abordados.
Ex:
 dados = dict()- é uma das formas de instanciar dados em Python.
 dados = { 'nome':'Pedro' , 'idade':25}
o indice agora são': nome e idade!
 Temos agora o seguinte Dicionario:
     -------------
     'Pedro'| 25 |
     ------------
     Para adicioanar um novo indice juntamente com um elemento faz-se uso do comando:
     dados[sexo] = 'M'
     Passando o nosso dicionario a ser composto por:
        nome  idade  sexo
      --------------------
     |'Pedro'| 25 |   'M'|
     --------------------
     Para eleiminar um indice juntamente com os seu elemento faz-se uso do comando:
     del dados['idade']
     Passando o nosso dicionario a ser composto por:
         nome   sexo
      --------------
     |'Pedro'| 'M'|
     ---------------

     Os dicionarios são referenciados por 3 termos as 'KYES' 'VALUES' 'ITEMS'
     Uma representação ilustrariva na fig 1.jgp


     E Possivel adicionar um diconario a uma lista locadora = list()
     Uma representação ilustrariva na fig 2.jgp


     Caso exista alguma duvida recomendo rever o video!
     https://youtu.be/ZWj8o692qGY
"""


"""
pessoa = {'nome': 'eric',
          'sexo': 'M',
          'idade': 22}
print(f' O {pessoa["nome"]} tem {pessoa["idade"]} anos!')

for k, v in pessoa.items():
    print(f'{k:<4} = {v:<2}')

print(f'----Usando o  del')
del pessoa['sexo']
for k, v in pessoa.items():
    print(f'{k:<4}= {v:<4}')

print(f'---Adicionando dados ao dicionario')
pessoa['peso'] = 85.3
pessoa['sexo'] = 'M'
for k, v in pessoa.items():
    print(f'{k:<4}= {v:<4}') """

"""Cirando um dicionario dentro de uma lista!"""

provincia1 = {'cidade': 'Maputo Cidade', 'Sigla': 'MC'}
provincia2 = {'cidade': 'Maputo Provinvia', 'Sigla': 'MP'}
provincia3 = {'cidade': 'Gaza', 'Sigla': 'GZ'}
provincia4 = {'cidade': 'Cidade Da Beira', 'Sigla': 'BR'}
provincia5 = {'cidade': 'Cabo Delgado', 'Sigla': 'CD'}
moz = list()
moz.append(provincia1), moz.append(provincia2), moz.append(provincia3), moz.append(provincia4), moz.append(provincia5)


for i, v in enumerate(moz):
    print(f'{v}')
