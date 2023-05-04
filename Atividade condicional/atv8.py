a = float(input("Informe o lado A: "))
a = float(input("Informe o lado B: "))
a = float(input("Informe o lado C: "))

if a < b+c and b < a+c and c < a+b:
    print("Temos um triangulo\n")
else:
    print("Voce não enconbtrou um triangulo\n")