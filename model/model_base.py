from model.conexao import Conexao
from sqlite3 import Error
class ModelBase:
    def __init__(self):
        # Conexão com o banco de dados
        self.con = Conexao()

    def get(self, sql):
        """Faz uma consulta no banco"""
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            resultado = cursor.execute(sql).fetchall()
            con.close()
            return resultado
        except Error as er:
            print(er)
    
    def insert(self, sql, params=None):
        """Insere um registro no banco e retorna o ID do registro inserido"""
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            con.commit()
            last_id = cursor.lastrowid
            con.close()
            return last_id
        except Error as er:
            print(er)
            return None


    def delete(self, sql):
        """Delete um registro do banco"""
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
            con.close()
            return cursor.rowcount
        except Error as er:
            print(er)

    def update(self, sql):
        """Atualiza um registro do banco"""
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            if cursor.rowcount == 1:
                con.commit()
            con.close()
            return cursor.rowcount
        except Error as er:
            print(er)

