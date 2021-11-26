perguntas = {
    'pergunta 1': {
        'pergunta': 'quanto é 2 + 2?',
        'respostas':{'a': '2','b': '5','c': '4'},
        'resposta_certa': 'c',
    },
    'pergunta 2': {
        'pergunta': 'quanto é 8 x 7?',
        'respostas':{'a': '36','b': '48','c': '56'},
        'resposta_certa': 'c',
    },
}
print()

pontuacao = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items():
        print(f"[{rk}]: {rv}")

    resposta_usuario = input("Sua resposta: ")

    if(resposta_usuario == pv['resposta_certa']):
        print("RESPOSTA CORRETA!!!")
        pontuacao += 1
    else:
        print("RESPOSTA ERRADA!! :(")

if(pontuacao <= 1):
    print(f"voce acertou {pontuacao} resposta")
else:
    print(f"voce acertou {pontuacao} respostas")

