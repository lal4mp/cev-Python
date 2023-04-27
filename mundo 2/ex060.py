"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""
import math

num = int(input('Digite um número para ver seu fatorial: '))
x = num
fatorial = 1

print('\033[30m{}! = ' .format(num), end='')
while x > 0:
    print('{}'.format(x), end='')
    print(' x ' if x > 1 else ' = ', end='')
    fatorial *= x
    x -= 1
print('{}' .format(fatorial))

# outra forma
print('\033[30m{}! = ' .format(num), end='')
for y in range(num, 0, -1):
    if y != 1:
        print('{} x ' .format(y), end='')
    else:
        print('1', end='')
print(' = {}' .format(math.factorial(num)))



