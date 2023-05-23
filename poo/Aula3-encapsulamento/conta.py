class Conta: 
    def __init__(self, numero, titular, saldo, limite=100):

        self.__numero = numero #em phyton tornamos um elemento privado com 2unberline. com 1 underline ele estar protegido. com nemhum underline, está publico
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite # esse atributo possui um valor padrão de forma que o usuario podera ou não informa este valor

    def relatorio(self):
        print(f" Olá {self.__titular} o numero da sua conta é {self.__numero} e o seu saldo atual é R${self.__saldo} o limite é até {self.__limite}")

    def exibirSaldo(self):
        print(f" seu saldo é {self.__saldo}")

        # o metodo get irá retornar ou exibir o valor do atributo

    def getlimite(self):
        return self.__limite
    
        # o metodo set irá alterar o conteudo do atributo, sem exibir nada
            
    def setlimite(self, valor):
        if valor < 0:
            print("Valor menor que zero, informe outro valor")
        else:
            self.__limite = valor