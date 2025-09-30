from model import model_base
import hashlib

class UsuarioController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de usuário para seus índices.
        # Tupla: (id, nick, email, senha, tipo)
        # Atenção: se a estrutura do banco mudar, atualize os índices neste dicionário.
        self.indices_campos = {
            "id": 0,
            "nick": 1,
            "email": 2,
            "senha": 3,
            "tipo": 4
        }

    def inserir_usuario(self, nick='', email='', senha='', tipo='C') -> int:
        """
        Insere um usuário no banco de dados.

        Args:
            nick (str): Apelido do usuário. Padrão ''.
            email (str): Email do usuário. Padrão ''.
            senha (str): Senha do usuário. Padrão ''.
            tipo (str): Tipo de usuário. Padrão 'C'.

        Returns:
            int: Número de linhas afetadas.
        """
        hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        sql = f"INSERT INTO usuario(usu_nick, usu_email, usu_senha, usu_tipo) VALUES ('{nick}', '{email}', '{hash}', '{tipo}');"
        return self.model.insert(sql)

    def listar_usuario(self, termo_busca='') -> list[dict] | None:
        """
        Lista os usuários cujo nick contenha o termo de busca.

        Args:
            termo_busca (str): Termo procurado no nick. Padrão ''.

        Returns:
            list[dict]: Lista de dicionários com os usuários correspondentes.
        """
        sql = f'SELECT * FROM usuario WHERE usu_nick LIKE "%{termo_busca}%";'
        resultado = self.model.get(sql)
        if not resultado:
            return []
        return [self.to_dict(u) for u in resultado]

    def busca_usuario(self, nick_ou_email='') -> dict | None:
        """
        Retorna um usuário pelo nick ou email informado.

        Args:
            nick_ou_email (str): Nick ou email do usuário.

        Returns:
            dict | None: Usuário correspondente como dict, ou None se não encontrado.
        """
        sql = f'SELECT * FROM usuario WHERE usu_nick = "{nick_ou_email}" OR usu_email = "{nick_ou_email}";'
        resultado = self.model.get(sql)
        if not resultado:
            return None
        return self.to_dict(resultado[0])

    def excluir_usuario(self, id) -> int:
        """
        Exclui o usuário pelo id informado.

        Args:
            id (int): Identificador do usuário.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'DELETE FROM usuario WHERE usu_id = {id};'
        return self.model.delete(sql)

    def atualizar_usuario(self, id, nick, email, senha, tipo) -> int:
        """
        Atualiza as informações de um usuário.

        Args:
            id (int): ID do usuário a ser atualizado.
            nick (str): Novo apelido.
            email (str): Novo email.
            senha (str): Nova senha (hashificada).
            tipo (str): Novo tipo de usuário.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'UPDATE usuario SET usu_nick = "{nick}", usu_email = "{email}", usu_senha = "{senha}", usu_tipo = "{tipo}" WHERE usu_id = {id};'
        return self.model.update(sql)


    def to_dict(self, usuario: tuple) -> dict:
        """
        Converte uma tupla de usuário em dicionário.

        Args:
            usuario (tuple): Tupla com os campos do usuário.

        Returns:
            dict: Usuário no formato dicionário.
        """
        return {
            "id": usuario[self.indices_campos["id"]],
            "nick": usuario[self.indices_campos["nick"]],
            "email": usuario[self.indices_campos["email"]],
            "senha": usuario[self.indices_campos["senha"]],
            "tipo": usuario[self.indices_campos["tipo"]],
        }