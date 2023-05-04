while True:
    final = int(input("Informe um valor maior que zero: "))
    if final > 0:
         break


contador = 1
while contador <= final:
    print(contador, end=" ")
    contador += 1