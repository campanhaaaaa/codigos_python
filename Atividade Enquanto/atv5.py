while True:

    valor = int(input("Escolha um valor de 1 a 9: "))
    if valor >= 1 and valor <= 9:
        break

    
contador = 1


while contador <= 10:
    if valor % 2 == 0:
        print (f"{valor} x {contador} {valor * contador}")

    else:
        print (f"{valor} + {contador} {valor + contador}")

        
    contador += 1