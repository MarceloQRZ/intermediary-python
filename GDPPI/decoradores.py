from time import time, sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nqa funcao {funcao.__name__}, levou {tempo:.2f}ms para executar')
    return interna

@velocidade
def demora():
    for i in range(10):
        print(i, end= '')
        #sleep(1)

demora()
