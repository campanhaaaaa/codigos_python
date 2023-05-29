import pymysql

conexao =  pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "departamento_bd"
)

comando = "select * from funcionario"

consulta = conexao.cursor()

consulta.execute(comando)

#exibir a consulta no banco
resultado = consulta.fetchall()# fetchall( irá trazer todas as linhas de registro que ja existem no banco)

print(resultado,"\n")
for itens in resultado:
    print(f"nome: {itens[1]}, cargo: {itens[3]}")

conexao.close()