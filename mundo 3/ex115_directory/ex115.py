from ex115_directory.lib.interface import *
from ex115_directory.lib.menu_options import *


while True:
    choice = menu(['Cadastrar pessoas', 'Listar pessoas cadastradas', 'Sair do programa'])

    if choice == 1:
        cabecalho('CADASTRAMENTO')
        lista = cadastramento()
    elif choice == 2:
        cabecalho('LISTA DOS CADASTROS')
        listar(lista)
    elif choice == 3:
        break
    else:
        print('\033[31mERRO - digite uma opção válida.\033[m\n')

