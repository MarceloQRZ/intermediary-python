def adicionar(opcao, lista):
    lista.append(opcao)

def show_op(lista):
    print('-----TAREFAS-----\n')
    print(lista)
    print()

def desfazer(lista, reducao):
    if not lista:
        print('nada para desfazer')
        return
    ultimo_lista = lista.pop()
    reducao.append(ultimo_lista)

def refazer(lista, reducao):
    if not reducao:
        print('nada a refazer')
        return
    ultimo_lista = reducao.pop()
    lista.append(ultimo_lista)

if __name__ == '__main__':
    lista = []
    reducao = []

    while True:
        opcao = input('-----ESCOLHA UM COMANDO-----\n\n'
                      '[add]  para adicionar\n'
                      '[undu] para refazer\n'
                      '[redu] para desfazer\n'
                      '[ls]   para listar\n')

        if opcao == 'add':
            tarefa = input("Digite a tarefa: ")
            adicionar(tarefa, lista)
            print()

        if opcao == 'undu':
            refazer(lista, reducao)

        elif opcao == 'redu':
            desfazer(lista, reducao)

        elif opcao == 'ls':
            show_op(lista)

