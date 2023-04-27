"""
Modifique as funções que foram criadas no desafio 107:
elas devem aceitar um parâmetro a mais:
informe se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
import moeda  # from ex109

p = float(input('Qual o preço do produto? R$'))

print(f'\nA metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Com 10% de aumento, o preço será {moeda.aumentar(p, 10, False)}')
print(f'Com 13% de desconto, o preço será {moeda.diminuir(p, 13, False)}')
