valor = int (input("Informe um valor qualquer: "))

for contador in range(1, valor+1):
    if(valor % contador == 0):
        print(contador)