"""
Melhore o jogo do DESAFIO 28
onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
import random

print('\033[1;35m----------JOGO ADIVINHA----------\033[m')
n = random.randint(0, 10)
print('Olá, sou seu computador!'
      '\nAcabei de pensar em um número entre 0 e 10. Tente adivinhar qual foi!')
num = int(input('Qual o seu palpite? '))
count = 1

while num != n:
    print('\n\033[31mVoce errou \u2639\033[m \nTente novamente!')
    num = int(input('Qual o seu palpite? '))
    count += 1

print('\n\033[1;32mParabéns!! \nVocê acertou \U0001F604'
      '\nO número sorteado era o {}.'
      '\nNúmero de tentativas: {}' .format(n, count))
