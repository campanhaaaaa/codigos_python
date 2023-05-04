maior = 0
num = 1
while num != 0:
    num = int(input("Informe um valor: "))
    if num >= maior:
        maior = num
    

print(f"O maior valor digitado foi {maior}\n")