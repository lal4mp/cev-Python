from ex115_directory2.lib.interface import *


def arquivoExiste(file):
    try:
        arq = open(file, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(file):
    try:
        arq = open(file, 'wt+')
        arq.close()
    except:
        print('\033[31mErro na criação do arquivo\033[m')
    else:
        print(f'Arquivo \'{file}\' criado com sucesso!')


def lerArquivo(file):
    try:
        arq = open(file, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo\033[m')
    else:
        cabecalho('CADASTROS')
        for linha in arq:
            dado = linha.split('-')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<25}{dado[1]} anos')
    finally:
        arq.close()


def cadastrar(file, nome='desconhecido', idade=0):
    try:
        arq = open(file, 'at')
    except:
        print('\033[31mErro ao abrir o arquivo\033[m')
    else:
        try:
            arq.write(f'{nome}-{idade}\n')
        except:
            print('\033[31mErro ao escrever os dados no arquivo\033[m')
        else:
            print('Novo registro realizado!')
            arq.close()
