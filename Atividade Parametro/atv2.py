while True:
    a = int(input("Informe um valor qualuqer: "))
    b = int(input("Informe um outro valor qualuqer diferente: "))

    if a != b:
        break
def somaImpar(inicial, final):
    soma = 0
    for contador in range(inicial, final+1):
        if contador % 2 ==1:
            soma += contador
    return soma
total = 0
contDivisores = 0

def mediaMultiplo3(inicial, final):
    for contador in range(inicial, final+1):
        if contador % 3 ==0:
            total += contador #isto e pra somar todos os divisores
            contDivisores += 1 #isto é para contar todos os divisores

    return total / contDivisores

if a < b:
    print(f" A soma dos Impares é: {somaImpar(a,b)}")
else:
    print(f"A media dos Multiplos de 3 é: {mediaMultiplo3(b,a)}")

