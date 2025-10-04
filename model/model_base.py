from model.conexao import Conexao
from sqlite3 import Error, IntegrityError

class ResponseQuery:
    def __init__(self, retorno=None, erros=None):
        # Retorno esperado da consulta (lista, id, linhas afetadas etc.)
        self.retorno = retorno
        
        # Lista de erros (objetos ou strings)
        self.erros = erros or []

    def add_erro(self, erro):
        """Adiciona um erro à lista (pode ser string ou Exception)"""
        self.erros.append(erro)

    def ok(self) -> bool:
        """Retorna True se não houve erros"""
        return len(self.erros) == 0

class ModelBase:
    def __init__(self):
        self.con = Conexao()

    def get(self, sql):
        """Faz uma consulta no banco"""
        resp = ResponseQuery()
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            resultado = cursor.execute(sql).fetchall()
            con.close()
            resp.retorno = resultado
        except Error as er:
            resp.add_erro(str(er))
        return resp

    def insert(self, sql, params=None):
        """Insere um registro no banco e retorna o ID"""
        resp = ResponseQuery()
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            con.commit()
            resp.retorno = cursor.lastrowid
            con.close()
        except (IntegrityError, Error) as er:
            resp.add_erro(str(er))
        return resp

    def delete(self, sql):
        """Deleta um registro"""
        resp = ResponseQuery()
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            resp.retorno = cursor.rowcount
            con.close()
        except Error as er:
            resp.add_erro(str(er))
        return resp

    def update(self, sql):
        """Atualiza um registro"""
        resp = ResponseQuery()
        try:
            con = self.con.get_conexao()
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            resp.retorno = cursor.rowcount
            con.close()
        except Error as er:
            resp.add_erro(str(er))
        return resp
