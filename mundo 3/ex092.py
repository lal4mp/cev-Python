"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho.
Cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO:
 o dicionário receberá também o ano de contratação e o salário.
 Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Informe seu nome: ')).capitalize()
dados['Ano de Nascimento'] = int(input('Informe o ano em que voce nasceu: '))
dados['Idade'] = datetime.now().year - dados['Ano de Nascimento']
dados['CTPS'] = int(input('Informe sua CTPS (0 se nao tem): '))
if dados['CTPS'] != 0:
    dados['Ano de Contratacao'] = int(input('Informe o ano em que voce foi contratado: '))
    dados['Salario'] = float(input('Informe seu salario: R$'))
    dados['Ano da Aposentadoria'] = dados['Ano de Contratacao'] + 35
    dados['Idade da Aposentadoria'] = dados['Ano da Aposentadoria'] - dados['Ano de Nascimento']

print()
for k, v in dados.items():
    print(f'{k}: {v}')


