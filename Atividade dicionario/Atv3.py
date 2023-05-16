lista = list()
preco = dict()

for contador in range(0,8):
    prato = input("Informe o seu prato: ")
    preco [prato] = int(input(f"Informe o valor do {prato}: "))

    lista.append(preco.copy)
    preco.clear()

print(lista)

