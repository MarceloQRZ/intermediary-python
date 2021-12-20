produtos = [
    {'nome':'p1', 'preco': 13},
    {'nome':'p2', 'preco': 55.55},
    {'nome':'p3', 'preco': 5.59},
    {'nome':'p4', 'preco': 22},
    {'nome':'p5', 'preco': 81.23},
    {'nome':'p6', 'preco': 5.7},
    {'nome':'p7', 'preco': 10.90},
    {'nome':'p8', 'preco': 89.82},
    {'nome':'p9', 'preco': 12},
    {'nome':'p10', 'preco': 2.90},
]

pessoas = [
    {'nome': 'Carlos', 'idade': 30},
    {'nome': 'Irineu', 'idade': 38},
    {'nome': 'Cleitin', 'idade': 12},
    {'nome': 'Pipoqueiro', 'idade': 70},
    {'nome': 'Luizin', 'idade': 5},
    {'nome': 'Cabra', 'idade': 63},
    {'nome': 'Lampiao', 'idade': 25},
    {'nome': 'Tripa', 'idade': 20},
    {'nome': 'Teteu', 'idade': 19},
    {'nome': 'Zezao', 'idade': 90}

]

def aumenta_idade(x):
    x['nova idade'] = round(x['idade'] * 1.5, 2)
    return x

def aumenta_preco(x):
    x['novo preco'] = round(x['preco'] * 1.7, 2)
    return x

idade_final = map(aumenta_idade, pessoas)
preco_final = map(aumenta_preco, produtos)

for i in idade_final:
    print(i)

print()

for i in preco_final:
    print(i)

