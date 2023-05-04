salario = float(input("Informe seu salario: "))

if salario < 600:
    novosalario = (salario * 30/100) + salario
    print(f"Seu novo salario é {novosalario}\n")
else:
    print("Voce não tem direito pois ganha {salario}\n")    