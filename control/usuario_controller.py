from model import model_base
import hashlib

class UsuarioController:
    def __init__(self):
        self.model = model_base.ModelBase()

    def inserir_usuario(self, nick='', email='', senha='', tipo='C'):
        hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        sql = f"INSERT INTO usuario(usu_nick, usu_email,usu_senha, usu_tipo) VALUES ('{nick}', '{email}', '{hash}', '{tipo}');"
        return self.model.insert(sql)

    def listar_usuario(self, nick=''):
        sql = f'SELECT * FROM usuario WHERE usu_nick LIKE "%{nick}%";'
        return self.model.get(sql)

    def busca_usuario_por_nick(self, nick=''):
        sql = f'SELECT * FROM usuario WHERE usu_nick LIKE "{nick}";'
        return self.model.get(sql)

    def busca_usuario_por_email(self, email=''):
        sql = f'SELECT * FROM usuario WHERE usu_email LIKE "{email}";'
        return self.model.get(sql)

    def excluir_usuario(self, id):
        sql = f'DELETE FROM usuario WHERE usu_id = {id}'
        return self.model.delete(sql)

    def atualizar_usuario(self, id, nick, email, senha, tipo):
        sql = f'UPDATE usuario SET usu_nick = "{nick}", usu_email = "{email}", usu_senha = "{senha}", usu_tipo = "{tipo}" WHERE usu_id = {id};'
        return self.model.update(sql)