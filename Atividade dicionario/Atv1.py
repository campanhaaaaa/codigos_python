lista = list()
produtos = dict()

for contador in range (0,5): 
    nome = input("informe o nome do produto: ")
    produtos[nome] = int(input(f"Informe a quantidade de {nome}: "))

    lista.append(produtos.copy())

print(lista)