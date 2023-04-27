"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
"""

print('\033[35m-='*10, 'INTERACTIVE HELP - PYTHON', '=-'*10)
while True:
    comando = str(input('\033[mVoce deseja ver o manual de qual comando? '))
    print(' '*22, f'\033[35mMANUAL DO COMANDO \033[1;36m\'{comando.upper()}\' \n\033[7;37m')
    help(comando)

    while True:
        r = str(input('\033[mVoce deseja acessar o manual de outro comando [s/n]? ')).lower()
        if r in 'ns':
            break
        print('\033[mOpcao invalida. Digite apenas "s" ou "n".')
    if r in 'n':
        break

