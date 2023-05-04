import os # importando blibioteca para trabalhar com sistema operacional
dentroIntervalo = 0 
foraIntervalo = 0
contador = 1

os.system("cls") # irá limpar a tela

while contador <= 5:
    valor = int(input(f"Informe o valor {contador}: "))
    if valor >= 10 and valor <= 20:
        dentroIntervalo += 1 
    else: 
        foraIntervalo += 1
    contador += 1

print (f"Valores dentro do intervalo: {dentroIntervalo}")
print (f"Valoores fora do intervalo: {foraIntervalo}")