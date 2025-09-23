from model import usuario_model

class UsuarioController:
    def __init__(self):
        self.model = usuario_model.UsuarioModel()

    def inserir_usuario(self, login='', senha='', tipo='C'):
        sql = f"INSERT INTO usuario(usu_login, usu_senha, usu_tipo) VALUES ('{login}', '{senha}', '{tipo}');"
        return self.model.insert(sql)

    def listar_usuario(self, login=''):
        sql = f'SELECT * FROM usuario WHERE usu_login LIKE "%{login}%";'
        return self.model.get(sql)

    def excluir_usuario(self, id):
        sql = f'DELETE FROM usuario WHERE usu_id = {id}'
        return self.model.delete(sql)

    def atualizar_usuario(self):
        pass