import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('O site YouTube NÃO estar acessivel no momento.')
else:
    print('o site YouTube estar acessivel!  ')