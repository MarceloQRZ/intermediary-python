string = '0123456789012345678901234567890123456789'
cont = 10

controle = [string[i: i+cont] for i in range(0, len(string), cont)]
retorno = '.'.join(controle)
print(controle)
print(retorno)