'''

def saudacao(x,y):
    print(f"{x} {y}")

def soma(a,b,c):
    return a + b + c

def porcentual(numero, porcentagem):
    return (porcentagem * numero / 100 )

def divisivel(x):
    if(x % 2 == 0):
        if(x % 5 == 0):
            return "Fizz Buzz"
        return "Fizz"
    elif (x % 5 == 0):
        return "Buzz"


print(porcentual(200, 44))
print(soma(9,2,100))
saudacao("seja bem vindo", "marcelo")
print(divisivel(4))

'''
def nome(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def mestre(x):
    return f'oi {nome}'

def saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

nome(mestre, 'Marcelo')
executar2 = nome(saudacao, 'marcelo', 'bom dia')

print(executar2)