"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
Tudo será guardado em um dicionário, incluindo o total de gols feitos.
"""
jog = dict()
jog['Nome'] = str(input('Informe o nome do jogador: ')).title()

num_partidas = int(input(f'Quantas partidas o {jog["Nome"]} jogou? '))
aproveitamento = list()
soma = 0
print('Quantos gols ele fez na ', end='')
for x in range(0, num_partidas):
    aproveitamento.append(int(input(f'{x+1}° partida? ')))
    soma += aproveitamento[x]
    print(' '*24, end='')

print()
jog['Gols por partida'] = aproveitamento[:]
jog['Total de gols'] = soma
print(jog)

print(f'\nO jogador {jog["Nome"]} jogou {num_partidas} partidas no campeonato')
for p, g in enumerate(jog['Gols por partida']):
    print(f'\tNa partida {p+1}, ele fez {g} gol(s)')
print(f'Total de {soma} gols no campeonato')