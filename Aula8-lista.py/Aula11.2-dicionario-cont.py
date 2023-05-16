import os
pessoa = dict()
grupo = list()

grupo.append({"nome":"João","idade":56})
grupo.append({"nome":"Maria ","idade":27})
grupo.append({"nome":"José","idade":32})

os.system("cls")

print(grupo,"\n")
"""
for contador in range(0,3):
    pessoa["nome0"] = input("Qual o seu nome: ")
    pessoa["idade"] = int(input("Qual sua idade: "))

    grupo.append(pessoa.copy())#Ceiando cópias do dicionario, sem criar vinculo ao dicionario(copiando e limpando)
print(grupo)
"""
print(grupo,"\n")
# ACESSANDO ITENS DO DICIONARIO



for contador in range(0,3):
    print(f"{grupo[contador]['nome']} : {grupo[contador]['idade']}")

# OUTRA FORMA DE ACESAR DICIONARIO
for linha in grupo:
    for elemento in linha.values():
        print(f"{elemento}", end="--")
    print()