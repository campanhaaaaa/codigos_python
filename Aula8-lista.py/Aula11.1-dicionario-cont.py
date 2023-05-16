import os
estado = {"uf": "Maranhão", "sigla": "MA"}
os.system("cls")
print(estado)

#FORMA1: inserindo dados em um dicionario

#FORMA 1
estado["população"] = "20.000.000"
print(estado)

#FORMA 2
estado.update({"capital":"São Luis"})
print(estado)

#REMOVER ITEMS DO DICIONARIO
#FORMA 1
estado.pop("uf")
print(estado)

#FORMA 2
del(estado["população"])
print(estado)

#FORMA 3 - APAGAR TODO CONTEUDO
estado.clear()
print(estado)