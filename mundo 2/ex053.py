"""
Crie um programa que leia uma frase qualquer.
Diga se ela é um palíndromo, desconsiderando os espaços.
"""
frase = str(input('Escreva uma frase: ')).strip().lower()
palavras = frase.split() #separou as palavras da frase em uma lista
junto = ''.join(palavras) #juntou as palavras da lista em uma string
inverso = junto[::-1]

'''
Outra forma:
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
'''

if junto == inverso:
    print('A frase "{}" É um palíndromo' .format(frase))
else:
    print('A frase "{}" NÃO É um palíndromo' .format(frase))


