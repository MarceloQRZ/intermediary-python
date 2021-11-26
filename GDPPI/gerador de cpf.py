from random import randint

numero = randint(100000000, 999999999)

cpf = numero
#cpf = [int(a) for a in str(cpf)]

digito1 = 0
digito2 = 0

controle = 10
soma1 = 0
index = 0

while (controle >= 2):
    soma1 += controle * cpf[index]
    controle -= 1
    index += 1

if (11 - (soma1 % 11) > 11):
    digito1 = 0
else:
    digito1 = 11 - (soma1 % 11)

controle = 11
soma1 = 0
index = 0

while (controle >= 2):
    soma1 += controle * cpf[index]
    controle -= 1
    index += 1

if (11 - (soma1 % 11) > 11):
    digito2 = 0
else:
    digito2 = 11 - (soma1 % 11)

print(cpf)