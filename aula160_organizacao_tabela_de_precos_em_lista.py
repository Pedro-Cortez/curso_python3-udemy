from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumento_10_por_cento(price):
    novo_preco = price + (price * 10/100)
    return novo_preco

print(f'TABELA DE REFERÊNCIA'.center(40, ' '))
print(*produtos, sep='\n')
print('\n')

# Produtos com aumento de 10%
novos_produtos = deepcopy(produtos)

print(f' TABELA COM AUMENTO '.center(40, '='))
for tabela in novos_produtos:
    preco_mais_10 = aumento_10_por_cento(tabela['preco'])
    tabela['preco'] = round(preco_mais_10, 2)
    print(f'{tabela["nome"]:.<30}  R$ {tabela["preco"]}')
    

# Produtos em ordem decrescente (nome)
cardapio = {}
produtos_ordenados_por_nome = deepcopy(produtos)
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key = lambda cardapio : cardapio['nome'], reverse = True)
print(f'\nTabela de produtos ordenada por nome (decrescente):')
print(*produtos_ordenados_por_nome, sep='\n')

# Produtos em ordem crescente (preço)
cardapio = {}
produtos_desordenados = deepcopy(produtos)
produtos_ordenados_por_preco = sorted(produtos_desordenados, key = lambda cardapio : cardapio['preco'])
print(f'\nTabela de produtos ordenada por preço (crescente):') 
print(*produtos_ordenados_por_preco, sep='\n')
