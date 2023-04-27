"""
Aprimore o desafio 93 para que ele funcione com vários jogadores.
Incluia um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
players = list()
jog = dict()

while True:
    jog['Nome'] = str(input('Informe o nome do jogador: ')).title()
    jog['N° de partidas'] = int(input(f'Quantas partidas o {jog["Nome"]} jogou? '))

    gols_por_partida = list()
    soma_gols = 0
    print('Quantos gols ele fez na ', end='')
    for x in range(0, jog['N° de partidas']):
        if x != 0:
            print(' ' * 24, end='')
        gols_por_partida.append(int(input(f'{x+1}° partida? ')))
        soma_gols += gols_por_partida[x]

    jog['Gols por partida'] = gols_por_partida[:]
    jog['Total de gols'] = soma_gols

    print(jog)
    players.append(jog.copy())
    jog.clear()

    while True:
        r = str(input('\nVoce deseja adicionar mais pessoas [s/n]? ')).lower()
        if r in 'ns':
            break
        print('Opcao invalida. Digite apenas "s" ou "n".')
    if r in 'n':
        break

    print()
    print('-='*50)
    print()

print()
print('-='*50)
print()
print('\033[35mCodigo', ' '*5, 'Nome', ' '*15, 'N° de partidas', ' '*5, 'Total de gols', ' '*5, 'Gols por partida\033[m')
for i, y in enumerate(players):
    print(f'{i:<13}{y["Nome"]:<21}{y["N° de partidas"]:<21}{y["Total de gols"]:<20}{y["Gols por partida"]}')

print()
print('-='*50)
print()

while True:
    while True:
        r = str(input('Voce deseja acessar o levantamento de algum jogador? ')).lower()
        if r in 'ns':
            break
        print('Opcao invalida. Digite apenas "s" ou "n".')
    if r in 'n':
        break

    while True:
        j = int(input('De qual jogador (informe seu respectivo codigo)? '))
        if(j < 0 or j >= len(players)):
            print('Codigo nao encontrado. Tente novamente.')
        else:
            break

    print(f'\033[36m\nLevantamento do jogador {players[j]["Nome"]}\033[m')
    print(f'{players[j]["Total de gols"]} gols em {players[j]["N° de partidas"]} partidas:')
    for p, g in enumerate(players[j]['Gols por partida']):
        print(f'\tNa partida {p + 1}, ele fez {g} gol(s)')

    print()
    print('-='*50)
    print()
