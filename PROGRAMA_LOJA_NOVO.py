from colorama import Fore, Back, Style

produtos = {'CAMISAS E TECTEL': 11, 'LISTRADAS, POLOS E CAMISAS DE TIME ': 30, 'ELASTANO': 20, 'CAMISAS DA TOMMY': 18,
            'CAMISAS VARIDAS': 25, 'BONÉS E CHINELOS': 15, 'MEIAS': 7, 'CORTA VENTO': 65, 'ÓCULOS NORMAL': 50,
            'ÓCULOS DE DESCANÇO': 45, 'CALÇAS JEANS': 30, 'CUECAS': 6, 'GATILHOS': 6, 'TÊNIS NIKE 4 MOLA': 75,
            'TÊNIS OAKLEY FLEK': 85, 'TÊNIS OAKLEY MODOC': 90, 'TÊNIS FILA': 35}

lista = list(produtos)

print('==================================')
print('       PROGRAMA DA LOJA ')
print('==================================')

valor_hoje = int(input('VALOR TOTAL DE VENDAS HOJE: '))

soma_total_produtos = contador = soma_tenis = soma_quantidade = meta = soma_valor = 0

for c, v in produtos.items():
    quantidade = str(input(f'({contador}) - Quantiade de {Fore.RED}{Back.BLUE}{c}{Style.RESET_ALL} que você vendeu: ')) # PEGA A QUANTIDADE DESSE PRODUTO VENDIDO

    if quantidade == "":
        quantidade = 0
    else:
        quantidade = int(quantidade)

    soma_produtos = quantidade * v # RECEBE A SOMA DA QUANTIDADE VENDIDA VEZES O VALOR DE CUSTO DO DOPRODUTO
    soma_total_produtos += soma_produtos # ACUMULA A SOMA TOTAL DE CUSTO DOS PRODUTOS DA VARIÁVEL "soma_produtos"

    if lista[contador][0] == 'T' and contador < 18:
        soma_tenis = soma_tenis + quantidade * 5 # RECEBE A SOMA DE TÊNIS VENDIDOS VEZES 5,00
    else:
        soma_quantidade = soma_quantidade + quantidade / 2 # RECEBE A SOMA DOS OUTROS PRODUTOS VENDIDOS DIVIDIDO / 2
    contador += 1

if valor_hoje >= 500:
    meta = 5

"""reposta = input("VENDEU MAIS ALGUM PRODUTO POR FORA [S/N] ? ").upper()

if resposta[:1] == "S":
    while True:

        resposta_2 = str(input("FOI TÊNIS [S/N] ? ")).upper()
        if resposta_2[:1] == "S":
            quantidade = int(input("QUANTOS ? "))
            valor = int(input("QUAL VALOR VOCÊ PAGOU PELO PRODUTO ? "))
            soma_tenis = soma_tenis + quantidade * 5
            soma_valor += valor
        else:
            valor = int(input("QUAL VALOR VOCÊ PAGOU PELO PRODUTO ? "))
            soma_quantidade += 0.50
            soma_valor += valor

        resposta = input("VENDEU MAIS ALGUM PRODUTO POR FORA [S/N] ? ").upper()
        if resposta[:1] != "S":
            break"""

print(30*"=")
print(f"META: {meta}")
print(f"TÊNIS: {soma_tenis}")
print(f"OUTROS PRODUTOS: {soma_quantidade}")
print("DIÁRIA 20.00")
print(Back.RED,f"TOTAL: {soma_quantidade + soma_tenis + meta + 20}", Style.RESET_ALL)
print(30*"=")
print(Back.GREEN, Fore.YELLOW, f"EU: {valor_hoje - soma_tenis- soma_quantidade - soma_total_produtos - meta - soma_valor - 20}", Style.RESET_ALL)