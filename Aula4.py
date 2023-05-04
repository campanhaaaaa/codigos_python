texto = "Técnico em Desenvolvimento de sistemas"
print("*******Titulo*******")
print("*"*10)
print(texto)

idade = int(input("quantos anos vc tem: "))
int(idade)
print(("# "*idade))

#manioulando textos(string)

print(f"O total de letras é {len(texto)}") # len ven de length, que significa total

print(texto.upper()) # upper() coloca todo texo em maiusculo
print(texto.capitalize()) # coloca a 1 letra em maiusculo

print(texto.replace("sistemas","web")) # replace troca um texto por outro

#TRABALHANDO COM FATIAMENTO
print("Fatiando a Variavel texto")
print(texto[:3]) # vai exubir todo o texto té  posição 2, nocaso a posi~ção 3 não conta
print(texto[3:])# vai exibir todo o texto apartir da posição 3
print(texto[3:10])# vai exibir todo o texto que está na posição 3 até 10