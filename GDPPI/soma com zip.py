lista1 = (5, 10, 32, 14, 17, 22)
lista2 = (3, 15, 72, 44, 8)

soma = tuple(zip(lista1, lista2))

total = 0
for i in soma:
    total += sum(i)

print(total)