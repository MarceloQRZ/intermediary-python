def converte_numero(x):
    try:
        x = int(x)
        return x
    except ValueError:
        try:
            x = float(x)
            return x
        except ValueError:
            pass
while True:
    numero = converte_numero(input("digite um umero: "))


    if numero is not None:
        print(numero * 2)
    else:
        print("isso não e numero")
