inicial = int(input("Informe um valor inicial: "))
final = int(input("Informe um valor final: "))
soma = 0
for contador in range(inicial, final + 1):
    soma = soma + contador

print(f"A soma de {inicial} + {final} é {soma}\n")
