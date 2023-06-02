import pymysql

class PacoteViagem:
    def conexao(self):
        con= pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="agencia_db"
        )
        return con
    
    def cadastrar_pacote (self, id, destino, preco, descricao):
        
        conexao= self.conexao()
        self.id= id
        self.destino= destino
        self.preco= preco
        self.descricao= descricao
        
        comando= "insert into pacoteviagem values(%s, %s, %s, %s)"
        
        valores= (id, destino, preco, descricao)
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, valores)
        
        conexao.commit()
        
        print(consulta.rowcount, "linhas inseridas com sucesso\n")
        
        conexao.close()
        
    def consultar_pacote (self):
        
        conexao= self.conexao()
        
        comando= "select * from pacoteviagem"
        
        consulta= conexao.cursor()
        
        consulta.execute(comando)
        
        resultado= consulta.fetchall()
        
        print(" TABELA DE VIAGEM ===========================")
        
        cont=0
        for perc in resultado:
            cont+=1
            print(f"id: {perc[0]}\t destino: {perc[1]}\t Preço: {perc[2]}\t descricao: {perc[3]}\n")
         
        print(" Viagens Cadastradas ==================\n") 
        print(f"Há {cont} Viagens Disponiveis.\n")
        print("===========================================")
        
    def deletar_pacote (self, id):
        self.codigo= id
        conexao= self.conexao()
        
        comando= "delete from pacoteviagem where id =%s"
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, self.id)
        
        conexao.commit()
        
        
        if consulta.rowcount == 0:
            print("Erro: Nenhum item foi deletado")
        elif consulta.rowcount > 0:
            print(consulta.rowcount, "linhas exluidas com sucesso!")
        
        conexao.close()
         
    def id_pacote (self, destino, id):
        
        conexao= self.conexao()
        self.destino= destino
        self.id= id
        
        comando= "update pacoteviagem set nome = %s where id = %s"
        
        valores= (self.destino, self.id)
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, valores)
        
        conexao.commit()
        
        print(consulta.rowcount, "linha foi atualizada com sucesso!")
        
        conexao.close()   
        
        
        
    def preco (self, preco, id):
        
        conexao= self.conexao()
        self.preco= preco
        self.codigo= id
        
        comando= "update pacoteviagem set preco = %s where id = %s"
        
        valores= (self.preco, self.id)
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, valores)
        
        conexao.commit()
        
        print(consulta.rowcount, "linha foi atualizada com sucesso!")
        
        conexao.close()
        
    def descricao(self, descricao, id):
        conexao= self.conexao()
        self.descricao= descricao
        self.id= id
        
        comando= "update pacoteviagem set descricao = %s where id = %s"
        
        valores= (self.descricao, self.id)
        
        consulta= conexao.cursor()
        
        consulta.execute(comando, valores)
        
        conexao.commit()
        
        print(consulta.rowcount, "linha foi atualizada com sucesso")
        
        conexao.close()
        