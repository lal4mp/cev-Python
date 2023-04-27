"""
Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Flamengo.
"""
tabela = ('Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians',
          'Internacional', 'Athletico-PR', 'Galo', 'Santos', 'América-MG',
          'Goiás', 'Bragantino', 'Fortaleza', 'São Paulo', 'Botafogo',
          'Ceará', 'Coritiba', 'Cuiabá', 'Avaí',
          'Atlético Goianiense', 'Juventude')

print(f'Os primeiros 5 colocados são: {tabela[0:5]}\n')
print(f'Os últimos 4 colocados são: {tabela[16:]}\n')
print(sorted(tabela))

print(f'\nO Flamengo está no {tabela.index("Flamengo")+1}° lugar')
