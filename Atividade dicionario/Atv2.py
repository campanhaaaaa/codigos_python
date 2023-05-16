lista = list()
telefone = dict()

for contador in range (0,7):
    contato = input("Informe o seu nome: ")
    telefone[contato] = int(input(f"Informe o numero do seu {contato}: "))

    lista.append(telefone.copy())
    telefone.clear()

print(lista)

