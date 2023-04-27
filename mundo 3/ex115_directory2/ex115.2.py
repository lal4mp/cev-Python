from ex115_directory2.lib.interface import *
from ex115_directory2.lib.arquivos import *

file = 'cadastros.txt'
if not arquivoExiste(file):
    criarArquivo(file)

while True:
    choice = menu(['Cadastrar nova pessoa', 'Listar pessoas cadastradas', 'Sair do programa'])

    if choice == 1:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(file, nome.title(), idade)

    elif choice == 2:
        lerArquivo(file)

    elif choice == 3:
        break

    else:
        print('\033[31mERRO - digite uma opção válida.\033[m\n')
