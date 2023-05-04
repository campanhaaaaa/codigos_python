valor = int(input("Informe o valor qualquer: "))
maior = 0
posicao = 0

for contador in range(1, valor + 1):
    item = int(input("Informe um valor: "))
    if item >= maior:
        maior = item
        posicao = contador

print(f"O maior valor é {maior} e esta na posicao {posicao}\n")