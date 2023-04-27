"""
Melhore o DESAFIO 61, pergunte para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""
print('    \033[1:35mPROGRESSÃO ARITMÉTICA\033[m')
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

x = a1
count = 1

# modo 1
total = 10
mais = 1
while mais != 0:
    while count <= total:
        print('\033[36m{}\033[m'.format(x), end='')
        print(' -> ' if count < total else '\n', end='')
        x += r
        count += 1
    mais = int(input('\nVocê deseja mostra mais quantos termos? '))
    total += mais


# modo alternativo
while count <= 10:
    print('\033[36m{}\033[m'.format(x), end='')
    if count < 10:
        print(' -> ', end='')
    else:
        perg = 'S'
        while perg in 'S':
            perg = str(input('\n\nVocê deseja mostra mais termos (S ou N)? ')).upper().strip()
            if perg in 'S':
                quant = int(input('Quantos? '))
                count = 1
                while count <= quant:
                    x += r
                    print('\033[36m{}\033[m'.format(x), end='')
                    print(' -> ' if count < quant else '', end='')
                    count += 1
            elif perg in 'N':
                exit()
            else:
                print('Opção inválida')
    x += r
    count += 1

