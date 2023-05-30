import pymysql

class Funcionario:

    def conexao(self):
        conexao = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="departamento_bd"
            )
        return conexao
    
    def inserir(self, codigo, nome, salario, cargo):

        conexao = self.conexao()# estamos chamando o metodo que irá conectar ao banco

        comando = "insert into funionario values(%s, %s, %s, %s)"

        valores = (codigo, nome, salario, cargo)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)
        conexao.commit()
        print(consulta.rowcount, "linha iserida com secesso \n")
        conexao.close()

    def consultar(self):
        conexao = self.conexao()

        comando = "select * from funcionario"
        consulta = conexao.cursor()
        consulta.execute(comando)

        resultado = consulta.fetchall()
        print(resultado, "\n")

        conexao.close()