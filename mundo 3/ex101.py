"""
Crie um programa que tenha uma função chamada voto():
recebe como parâmetro o ano de nascimento de uma pessoa e retorna:
se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    print(f'{idade} anos -> voto ', end='')
    if 18 <= idade < 70:
        return 'OBRIGATÓRIO'
    elif idade < 16:
        return 'NEGADO'
    else:
        return 'OPCIONAL'


# programa principal
year = int(input('Em qual ano você nasceu? '))
r = voto(year)
print(f'{r}')
