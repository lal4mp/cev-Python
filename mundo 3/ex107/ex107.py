"""
Crie um módulo chamado moeda.py que tenha as funções:
-aumentar()
-diminuir()
-dobro()
-metade()
Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
import moeda  # from ex107

p = float(input('Qual o preço do produto? R$'))

print(f'\nA metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Com 10% de aumento, o preço será {moeda.aumentar(p, 10)}')
print(f'Com 13% de desconto, o preço será {moeda.diminuir(p, 13)}')

