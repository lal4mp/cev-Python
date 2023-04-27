"""
Adapte o código do desafio #107
Crie uma função adicional chamada moeda():
mostrar os números como um valor monetário formatado.
"""
import moeda  # from ex108

p = float(input('Qual o preço do produto? R$'))

print(f'\nA metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Com 10% de aumento, o preço será {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Com 13% de desconto, o preço será {moeda.moeda(moeda.diminuir(p, 13))}')
