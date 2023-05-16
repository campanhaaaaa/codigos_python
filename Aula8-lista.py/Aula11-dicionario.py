lista = ["joao", 30 , "Cohab"]
pessoa = {
    "nome":"Maria",
    "idade":30,
    "bairro":"Renascença"
}
print(lista[0])
print(pessoa,"\n")
# exibindo as CHAVES ultilizando o comando keys()
print(pessoa.keys())

#exibindo os VALORES ultilizando comando  values
print(pessoa.values())

#exibindo tanto a chave como valor ultilizando o comando items()
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave} : {valor}")