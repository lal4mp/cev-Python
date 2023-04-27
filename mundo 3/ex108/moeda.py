def aumentar(preco=0, taxa=0):
    preco += (taxa/100)*preco
    return preco


def diminuir(preco=0, taxa=0):
    preco -= (taxa/100)*preco
    return preco


def dobro(preco=0):
    preco *= 2
    return preco


def metade(preco=0):
    preco /= 2
    return preco


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')
