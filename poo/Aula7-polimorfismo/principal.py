from produto import Produto, Livro, Eletronico

meuLivro = Livro("Hoje é Quinta", 56, "Fulanfo Cury")
meuEletronico = Eletronico("Caixa de som", 100, "Samuk Multimarcas")

meuLivro.descrever()
meuLivro.calcularPreco()

meuEletronico.descrever()
meuEletronico.calcularPreco()


