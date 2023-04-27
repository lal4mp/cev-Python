def aumentar(preco, taxa):
    preco += (taxa/100)*preco
    return preco


def diminuir(preco, taxa):
    preco -= (taxa/100)*preco
    return preco


def dobro(preco):
    preco *= 2
    return preco


def metade(preco):
    preco /= 2
    return preco