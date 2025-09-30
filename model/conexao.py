import sqlite3
from sqlite3 import Error

class Conexao:
    def get_conexao(self):
        """Retorna um objeto de conexão com o banco de dados"""
        
        caminho = 'banco/banco.db'
        try:
            con = sqlite3.connect(caminho)
            return con
        except Error as er:
            print(er)