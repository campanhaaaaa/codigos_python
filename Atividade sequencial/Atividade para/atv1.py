soma = 0
media = 0
total = 0

for contador in range(50, 71):
    total = total + 1
    soma = soma + contador # acomulando os valores
    media = soma / total
print(f"O total é {total}\n a {soma} e a media é {media}\n")