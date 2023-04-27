"""
Crie um pacote chamado utilidadesCeV:
Ele tem dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""
from utilidadesCeV import moeda, dado

p = float(input('Qual o preço do produto? '))
moeda.resumo(p, 20, 12)
