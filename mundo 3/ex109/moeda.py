def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(preco=0, taxa=0, form=True):
    preco += (taxa/100)*preco
    if form is True:
        return moeda(preco)
    else:
        return preco


def diminuir(preco=0, taxa=0, form=True):
    preco -= (taxa/100)*preco
    return moeda(preco) if form is True else preco


def dobro(preco=0, form=True):
    preco *= 2
    if form is True:
        return moeda(preco)
    else:
        return preco


def metade(preco=0, form=True):
    preco /= 2
    return moeda(preco) if form is True else preco

