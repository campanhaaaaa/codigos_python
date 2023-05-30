import pymysql

conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="departamento_bd"

)

nome = input("Informe o novo nome do funcionario: ")
codigo = int(input("Qual o codigo do funcionario?: "))

comando = "update funcionario set nome = %s where cod_funcionario = %s"

valores = (nome, codigo)

consulta = conexao.cursor()

consulta.execute(comando, valores)
 
conexao.commit()

print(consulta.rowcount, "linha atualizada com secesso\n")

conexao.close()
