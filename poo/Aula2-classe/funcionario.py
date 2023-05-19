class Funcionario:
    #Criando o metodo construtor
    def __init__(self, nome, cargo, salario):
        #estamos criando os atributos da classe ultilizando metodo construtor. nesse caso precisamos passar os parametros que serão usados como valores dos atributos da classe.
        
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


    def exibirDados(self):

        print(f"Olá {self.nome} seu cargo é {self.cargo} seu salario é {self.salario}")

