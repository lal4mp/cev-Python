def leiaDinheiro(text):
    while True:
        valor = str(input(text)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO: "{valor}" é um preço inválido\033[m\n')
        else:
            return float(valor)
