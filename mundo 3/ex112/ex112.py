"""
Crie uma função chamada leiaDinheiro() dentro do módulo 'dado', do ex111:
validação de dados para aceitar apenas valores que seja monetários
"""
from utilidadesCeV import moeda, dado

p = dado.leiaDinheiro('Qual o preço do produto? R$')
moeda.resumo(p, 20, 12)
