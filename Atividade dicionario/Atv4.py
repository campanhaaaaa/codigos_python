playlist = list()
musica = dict()

for contador in range(2):
    nome = input("Qual o nome da musica: ")
    artista = input("Qual o nome do artista: ")
    tempo = float(input("Qual a duracao da musica? "))

    musica[nome] = {"artista": artista, "duracao":tempo}

    playlist.append(musica.copy())
    musica.clear()

print(playlist)
for linha in playlist:
    for chave, valor in linha.items():
        print(f"{chave}: artista = {valor["artista"]} duracao:{valor["duracao"]}")