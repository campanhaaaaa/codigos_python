import pymysql

#Estabelecimento a conexão
conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="departamento_bd"
)

#Inserindo dados no Banco
codigo = int(input("Informe o godigo do funcionario: "))
nome = input("Informe o nome do funcionario: ")
salario = float(input("Informe o salario do funcionario: "))
cargo = input("Informe o cargo do funcionario: ")

# colocamos %s no lugar dos dados reais, para evitar possiveis ataques de sql injection. isso é uma implementação da blibioteca pymysql
comando = "insert into Funcionario values(%s, %s, %s, %s)"

campos = (codigo, nome, salario, cargo)# Criando um tupla com os dados que serão substituidos no comando

consulta = conexao.cursor()#cursor() é o objeto que irá interagir diretamente com o banco de dados

consulta.execute(comando, campos)

conexao.commit() # gravar os dados no banco

print(consulta.rowcount, " lnhas(s) inserida com sucesso\n")

conexao.close()