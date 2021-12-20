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
    {'nome': 'Irineu', 'idade': 15},
    {'nome': 'Cleitin', 'idade': 12},
    {'nome': 'Pipoqueiro', 'idade': 70},
    {'nome': 'Luizin', 'idade': 5},
    {'nome': 'Cabra', 'idade': 13},
    {'nome': 'Lampiao', 'idade': 25},
    {'nome': 'Tripa', 'idade': 20},
    {'nome': 'Teteu', 'idade': 19},
    {'nome': 'Zezao', 'idade': 90}

]

def maior(x):
    if x['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(maior, pessoas)

for i in nova_lista:
    print(i)