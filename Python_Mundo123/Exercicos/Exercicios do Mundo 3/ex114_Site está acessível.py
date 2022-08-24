import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'O site Pum não esta acessecivel! no momento')
else:
    print(f'Tudo ok!')