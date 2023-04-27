"""
Faça um programa que leia algo pelo teclado.
Mostre na tela o seu tipo primitivo e todas as possíveis informações sobre ele.
"""

x = input("Digite algo: ")
print("Tipo primitivo:", type(x))
print("É um número? ", x.isnumeric())
print("É alfabético? ", x.isalpha())
print("É alfanúmerico? ", x.isalnum())
print("Está em maiúsculo? ", x.isupper())
print("Está em minúsculo? ", x.islower())
print("Está capitalizada? ", x.istitle())
print("Só tem espaços? ", x.isspace())
