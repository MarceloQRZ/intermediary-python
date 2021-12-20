from itertools import groupby
remedinhos = [
    {'nome':'deca', 'nota': 'A'},
    {'nome':'durateston', 'nota': 'B'},
    {'nome':'hemogelin', 'nota': 'A'},
    {'nome':'oximetolona', 'nota': 'C'},
    {'nome':'metandriol', 'nota': 'A'},
    {'nome':'donazol', 'nota': 'B'},
    {'nome':'mesterolona', 'nota': 'A'},
    {'nome':'Testosterona', 'nota': 'A'},
    {'nome':'Nandrolona', 'nota': 'C'}
]

ordenacao = lambda item: item['nota']
remedinhos.sort(key = ordenacao)
remedinhos_agrupados = groupby(remedinhos, ordenacao)

for agrupamento, paradinhas_agrupadas in remedinhos_agrupados:
    print(f'\nagrupamento {agrupamento}')
    for paradinhas in paradinhas_agrupadas:
        print(f'\tparadinhas{paradinhas}')