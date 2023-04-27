"""
Crie uma tupla com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20).
Mostre-o por extenso.
"""
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
            'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
            'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
            'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Opção inválida. Tente novamente.\n')

print(f'Você digitou o número {contagem[n]}')
