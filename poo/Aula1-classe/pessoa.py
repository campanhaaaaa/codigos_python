class pessoa: 
    #ATRIBUTOS
    nome = "Amanda"
    idade = 18
    altura = 1.70

    #MÉTODOS
    def falar(self, texto): # self é um parametro obrigatorio do python que informa que o metodo pertence a propia classe que foi criada
        print(texto)

pessoa1 = pessoa()
pessoa1.nome = "José"
print(pessoa1.nome, pessoa1.idade)

pessoa1.falar("Olá Mundo")