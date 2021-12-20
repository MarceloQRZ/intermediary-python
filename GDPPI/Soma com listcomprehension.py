carrinho = []

carrinho.append(("produto 1", 20))
carrinho.append(("produto 2", 30))
carrinho.append(("produto 3", 50))

total = sum([y for x, y in carrinho])
print(total)