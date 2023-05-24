class Funcionario:
    def __init__(self,cargo,nome):
        self._cargo = cargo
        self._nome = nome

    def informacoes(self):
        print(f"Olá {self._nome}, seu cargo atual é {self._cargo}\n")

class Gerente(Funcionario):
    def __init__(self, cargo, nome, salario):
        super().__init__(cargo, nome) #Super()
        self._salario = salario

    def exibirSalario(self):
        print(f"Seu nome é {self._nome} e voce ganha {self._salario}\n")
    