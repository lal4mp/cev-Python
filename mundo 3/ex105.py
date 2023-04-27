"""
Faça um programa que tenha uma função notas():
que pode receber várias notas de alunos e retorna um dicionário com as seguintes informações:
-quantidade de notas
–maior nota
–menor nota
–média da turma
–situação (opcional)
"""


def notas(*notas, sit=True):
    """
    A função 'notas' calcula dados (quantidade de notas, maior e menor nota, média das notas e situação) de uma turma.
    :param notas: recebe as notas dos alunos.
    :param sit: opcional -> mostra (True) ou não (False) a situação da turma, em relação a média das notas.
    :return: retorna um dicionário com os dados calculados.
    """

    dados = dict()
    dados['quantidade de notas'] = len(notas)
    dados['maior nota'] = max(notas)
    dados['menor nota'] = min(notas)
    dados['média da turma'] = sum(notas) / len(notas)

    if sit:
        if dados['média da turma'] >= 5:
            dados['situação'] = 'Boa'
        elif dados['média da turma'] <= 3:
            dados['situação'] = 'Ruim'
        else:
            dados['situação'] = 'Razoavel'

    return dados


# programa principal
dados = (notas(3, 5, 4, 1, 2, sit=False))
dados2 = (notas(3, 5, 4, 1, 2))
print(dados)
print(dados2)

print('\n\n')
help(notas)
