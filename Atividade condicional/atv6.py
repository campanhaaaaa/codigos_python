percurso = float(input("Informe o percurso em km: "))
tipocarro = int(input("Informe o tipo do carro, 1, 2 ou 3: "))

if tipocarro == 1:
    total = percurso / 8
    print(f"o tipo do carro é {tipocarro} vai precisar de {total} litros de gasolina\n")
elif tipocarro == 2:
    total = percurso / 9
    print(f"o tipo do carro é {tipocarro} vai precisar de {total} litros de gasolina\n")
    
elif tipocarro == 3:
    total = percurso / 12
print(f"o tipo do carro é {tipocarro} vai precisar de {total} litros de gasolina\n")


print("Tipo de carro invalido\n")