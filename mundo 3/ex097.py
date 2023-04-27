"""
Faça um programa que tenha uma função chamada escreva():
recebe um texto qualquer como parâmetro.
Mstre uma mensagem com tamanho adaptável.
"""

def escreva(texto):
    print('~' * (len(texto)+4))
    print(f'  {texto}  ')
    print('~' * (len(texto)+4))

# Programa Principal
text = str(input('Digite um frase: '))
escreva(text)
