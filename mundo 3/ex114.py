"""
Crie um código em Python que teste se o site 'pudim' está acessível.
"""
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[31mERRO - o site "pudim" não está acessível no momento.\033[m')
else:
    print('\033[32mO site "pudim" está acessível!\033[m')
