from conexao import Conexao
from sqlite3 import Error
class FornecedorModel:
    def __init__(self):
        self.con = Conexao()

    def get_fornecedor(self, sql):
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            resultado = cursor.execute(sql).fetchall()
            con.close()
            return resultado
        except Error as er:
            print(er)

    def insert_fornecedor(self, sql):
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

    def delete_fornecedor(self, sql):
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

    def update_fornecedor(self, sql):
        pass