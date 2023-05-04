lata350 = int(input("Indorme a quantidade de latas de 350ml: "))
garrafa600 = int(input("Indorme a quantidade de garrafas de 600ml: "))
garrafa2 = int(input("Indorme a quantidade de garrafas de 2 litros: "))

total = lata350 * 0.35 + garrafa2 * 0.6 + garrafa2 * 2
print(f"O total de litros é {total}")