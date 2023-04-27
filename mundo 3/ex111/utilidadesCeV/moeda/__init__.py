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


def resumo(preco=0, t_aumento=0, t_desconto=0):
    print()
    print(' '*7, '\033[7mRESUMO DO PRODUTO\033[m')
    print(f'{"Preço:":<25}{moeda(preco)}')
    print(f'{"Dobro do preço:":<25}{dobro(preco)}')
    print(f'{"Metade do preço:":<25}{metade(preco)}')
    print(f'{f"Com {t_aumento} % de aumento:":<25}{aumentar(preco, t_aumento)}')
    print(f'{f"Com {t_desconto} % de desconto:":<25}{diminuir(preco, t_desconto)}')
