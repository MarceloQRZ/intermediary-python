#Palavra escondida

palavra_chave = input("Digite a palavra que devera ser descoberta: ")
palavras = []
vida = 5

while True:
    if vida <= 0:
        print("A casa caiu!!")
        break

    tentativa = input("Digite uma letra: ")

    if len(tentativa) > 1:
        print("Hey men, apenas uma letra por vez!")
        continue

    palavras.append(tentativa)
    if tentativa in palavra_chave:
        print(f"A letra {tentativa} ta por aqui!")
    else:
        print(f"A mano, a letra {tentativa} nao ta aqui nao! :(")
        palavras.pop()

    secreta = ''
    for algo in palavra_chave:
        if algo in palavras:
            secreta += algo
        else:
            secreta += '*'

    if secreta == palavra_chave:
        print(f"Ganhou, men! A palavra era essa daqui ooh: {secreta}")
        break
    else:
        print(f"Ate agora a palavra ta assim: {secreta}")

    if tentativa not in palavra_chave:
        vida -= 1

    print(f"Tu ainda tem {vida} de vida\n")
