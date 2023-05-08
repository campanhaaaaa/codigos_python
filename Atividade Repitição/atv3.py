mediaturma = 0
mediamulheres = 0
maior = 0
somaturma = 0
somamulheres = 0
contmulheres = 0

for contador in range (1,7):
    altura = float(input("Informe sua altura: "))
    sexo = int(input("Informe o codigo do sexo: 1-masc ou 2-fem: "))

    if contador == 1:
        menor = altura
    else:
        if altura >= maior:
            maior = altura

        if altura <= menor: 
            menor = altura

    if sexo == 2: 
        somamulheres += altura
        contmulheres += 1

    somaturma += altura
print(f"A maior altura é {maior} e a menor altura é {menor}")
print(f"A maior da alturas das mulheres é {somamulheres / contmulheres}")
print(f"A media de alturas da turma é {somaturma / 6}\n")
