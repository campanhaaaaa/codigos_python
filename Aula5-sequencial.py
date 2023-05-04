nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

media = (nota1 + nota2)/2

if media >= 7:
        print("Voce passou :)")

elif media == 6:
            print("Voce está de recuperação")
else:
            print("Voce reprovou :(")