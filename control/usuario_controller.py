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

    def inserir_usuario(self, nick: str = '', email: str = '', senha: str = '', tipo: str = 'C') -> int:
        """
        Insere um usuário no banco de dados. A senha é hashificada antes de ser salva.

        Args:
            nick (str): Apelido do usuário. Padrão ''.
            email (str): Email do usuário. Padrão ''.
            senha (str): Senha do usuário (texto simples). Padrão ''.
            tipo (str): Tipo de usuário. Padrão 'C'.

        Returns:
            int: Número de linhas afetadas.
        """
        senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        sql = (
            "INSERT INTO usuario(usu_nick, usu_email, usu_senha, usu_tipo) "
            f"VALUES ('{nick}', '{email}', '{senha_hash}', '{tipo}');"
        )
        return self.model.insert(sql)

    def listar_usuario(self, termo_busca: str = '') -> list[dict]:
        """
        Lista os usuários cujo nick contenha o termo de busca.

        Args:
            termo_busca (str): Termo procurado no nick. Padrão ''.

        Returns:
            list[dict]: Lista de dicionários com os usuários correspondentes (vazia se nenhum).
        """
        sql = f'SELECT * FROM usuario WHERE usu_nick LIKE "%{termo_busca}%";'
        resultado = self.model.get(sql)
        if not resultado:
            return []
        return [self.to_dict(u) for u in resultado]

    def busca_usuario(self, nick_ou_email: str = '') -> dict | None:
        """
        Retorna um usuário pelo nick ou email informado.

        Args:
            nick_ou_email (str): Nick ou email do usuário.

        Returns:
            dict | None: Usuário correspondente como dict, ou None se não encontrado.
        """
        sql = f'SELECT * FROM usuario WHERE usu_nick = "{nick_ou_email}" OR usu_email = "{nick_ou_email}";'
        resultado = self.model.get(sql)
        return self.to_dict(resultado[0]) if resultado else None

    def excluir_usuario(self, id: int) -> int:
        """
        Exclui o usuário pelo id informado.

        Args:
            id (int): Identificador do usuário.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'DELETE FROM usuario WHERE usu_id = {id};'
        return self.model.delete(sql)

    def atualizar_usuario(self, id: int, nick: str, email: str, senha: str | None, tipo: str) -> int:
        """
        Atualiza as informações de um usuário.
        A senha será hashificada e atualizada somente se um valor não vazio for fornecido.

        Args:
            id (int): ID do usuário a ser atualizado.
            nick (str): Novo apelido.
            email (str): Novo email.
            senha (str | None): Nova senha em texto simples. Se None ou '', a senha não é alterada.
            tipo (str): Novo tipo de usuário.

        Returns:
            int: Número de linhas afetadas.
        """
        partes = [
            f"usu_nick = '{nick}'",
            f"usu_email = '{email}'",
            f"usu_tipo = '{tipo}'"
        ]
        if senha is not None and senha != '':
            senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            partes.insert(2, f"usu_senha = '{senha_hash}'")  # mantemos ordem legível

        sql = f"UPDATE usuario SET {', '.join(partes)} WHERE usu_id = {id};"
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