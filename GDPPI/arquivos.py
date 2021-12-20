import os

with open('nome.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    file.seek(0.0)
    print(file.read())

with open('nome.txt', 'a+') as file:
    file.write('linha 4\n')
    file.write('linha 5\n')
    file.write('linha 6\n')
    file.seek(0.0)
    print(file.read())

os.remove('nome.txt')



