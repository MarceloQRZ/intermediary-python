'''
CPF = 60363554327
6 * 10 = 60             #   6 * 11 = 66
0 * 9  = 0              #   0 * 10 = 0
3 * 8  = 24             #   3 * 9  = 27
6 * 7  = 42             #   6 * 8  = 48
3 * 6  = 18             #   3 * 7  = 21
5 * 5  = 25             #   5 * 6  = 30
5 * 4  = 20             #   5 * 5  = 25
4 * 3  = 12             #   4 * 4  = 16
3 * 2  = 6              #   3 * 3  = 9
                        #   2 * 2  = 4
         207                         246
        
11 - (201 % 11) = 2         11 - (246 % 11) = 7         
11 > 9 = 0
digito 1 = 2                digito 2 = 7
'''
cpf = input("Digite o seu CPF: ")
cpf = [int(a) for a in str(cpf)]

digito1 = 0
digito2 = 0

controle = 10
soma1 = 0
index = 0

while(controle >= 2):
    soma1 += controle * cpf[index]
    controle -= 1
    index += 1

if(11 - (soma1 % 11) > 11):
    digito1 = 0
else:
    digito1 = 11 - (soma1 % 11)

controle = 11
soma1 = 0
index = 0

while(controle >= 2):
    soma1 += controle * cpf[index]
    controle -= 1
    index += 1

if(11 - (soma1 % 11) > 11):
    digito2 = 0
else:
    digito2 = 11 - (soma1 % 11)

if digito1 == cpf[9] and digito2 == cpf[10]:
    print("CPF valido!")
else:
    print("CPF invalido!")