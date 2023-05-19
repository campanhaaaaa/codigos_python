class Aluno:

    def __init__(self, nome, matricula, telefone):

        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone

    def exibirDados(self):

        print(f"Olá {self.nome} sua matricula é {self.matricula} seu telefone é {self.telefone}")
