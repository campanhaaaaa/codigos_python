lanche = ("Pizza", "Hotdog", "refri", "batata")
print(lanche)
print(type(lanche)) #estou mostrando o tipo da variavel

print(lanche[1])
print(f" o total de lache é {len(lanche)} \n ") #length

#lanche[2] = "Suco"

for contador in range(0, 4):
    print(lanche[contador])

print("-"*30)
for item in lanche:
    print(item)

print("-"*30)
# enumerate serve para permitir acessar os indices da tupl. ja a variavel indice, ira armazenar os valores do indice
for indice, elemento in enumerate(lanche):
    print(f"{indice} = {elemento}")