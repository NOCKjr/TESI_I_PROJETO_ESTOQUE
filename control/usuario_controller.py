import hashlib
from control.controller_base import ControllerBase
from model.model_base import ResponseQuery

class UsuarioController(ControllerBase):
    def __init__(self):
        super().__init__()
        """
        Controller responsável por intermediar operações entre a aplicação e o banco
        de dados para a entidade 'usuario'.
        """

        # Mapeamento dos campos da tupla de usuário para seus índices.
        self.indices_campos = {
            "id": 0,
            "nick": 1,
            "email": 2,
            "senha": 3,
            "tipo": 4,
        }

        # Funções de callback para operações CRUD 
        self.funcao_inserir_item = self.inserir_usuario
        self.funcao_listar_item = self.listar_usuario
        self.funcao_buscar_item = self.buscar_usuario
        self.funcao_buscar_item_por_id = self.buscar_usuario_por_id
        self.funcao_excluir_item = self.excluir_usuario
        self.funcao_atualizar_item = self.atualizar_usuario
        # self.funcao_to_dict = self.to_dict_usuario

    def inserir_usuario(self, nick: str = '', email: str = '', senha: str = '', tipo: str = 'C') -> ResponseQuery:
        """
        Insere um usuário no banco de dados. 
        A senha é convertida em hash SHA-256 antes de ser salva.

        Args:
            nick (str): Apelido do usuário. Padrão ''.
            email (str): Email do usuário. Padrão ''.
            senha (str): Senha do usuário em texto simples. Padrão ''.
            tipo (str): Tipo do usuário (ex: 'C' para comum, 'A' para admin). Padrão 'C'.

        Returns:
            ResponseQuery: 
                - `retorno`: ID do usuário inserido (int).
                - `erros`: lista de erros caso ocorra falha.
        """
        senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        sql = (
            "INSERT INTO usuario(usu_nick, usu_email, usu_senha, usu_tipo) "
            f"VALUES ('{nick}', '{email}', '{senha_hash}', '{tipo}');"
        )
        resp = self.model.insert(sql)

        if not resp.ok():
            for er in resp.erros:
                msg = str(er).lower()
                if "nick" in msg:
                    return ResponseQuery(erros=["NICK_DUPLICADO"])
                elif "email" in msg:
                    return ResponseQuery(erros=["EMAIL_DUPLICADO"])
                else:
                    return ResponseQuery(erros=[str(er)])
        
        return resp

    def listar_usuario(self, termo_busca: str = '') -> ResponseQuery:
        """
        Lista os usuários cujo `nick` contenha o termo de busca.

        Args:
            termo_busca (str): Termo procurado no nick. Padrão ''.

        Returns:
            ResponseQuery:
                - `retorno`: lista de usuários como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'SELECT * FROM usuario WHERE usu_nick LIKE "%{termo_busca}%";'
        resp = self.model.get(sql)
        if resp.ok():
            resp.retorno = [self.to_dict(u) for u in resp.retorno]
        return resp

    def buscar_usuario(self, nick_ou_email: str = '') -> ResponseQuery:
        """
        Retorna um usuário pelo nick OU email informado.

        Args:
            nick_ou_email (str): Nick ou email do usuário.

        Returns:
            ResponseQuery:
                - `retorno`: dicionário do usuário ou None.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'SELECT * FROM usuario WHERE usu_nick = "{nick_ou_email}" OR usu_email = "{nick_ou_email}";'
        resp = self.model.get(sql)
        if resp.ok():
            resp.retorno = self.to_dict(resp.retorno[0]) if resp.retorno else None
        return resp

    def buscar_usuario_por_id(self, id: int) -> ResponseQuery:
        """
        Retorna um usuário pelo ID.

        Args:
            id (int): ID do usuário.

        Returns:
            ResponseQuery:
                - `retorno`: dicionário do usuário ou None.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'SELECT * FROM usuario WHERE usu_id = {id};'
        resp = self.model.get(sql)
        if resp.ok():
            resp.retorno = self.to_dict(resp.retorno[0]) if resp.retorno else None
        return resp

    def excluir_usuario(self, id: int) -> ResponseQuery:
        """
        Exclui um usuário do banco pelo seu ID.

        Args:
            id (int): Identificador do usuário.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'DELETE FROM usuario WHERE usu_id = {id};'
        return self.model.delete(sql)

    def atualizar_usuario(self, id: int, nick: str, email: str, senha: str | None, tipo: str) -> ResponseQuery:
        """
        Atualiza os dados de um usuário existente.
        A senha será atualizada apenas se fornecida e não vazia.

        Args:
            id (int): ID do usuário.
            nick (str): Novo apelido.
            email (str): Novo email.
            senha (str | None): Nova senha em texto simples. Se None ou '', não será alterada.
            tipo (str): Novo tipo de usuário.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        partes = [
            f"usu_nick = '{nick}'",
            f"usu_email = '{email}'",
            f"usu_tipo = '{tipo}'"
        ]
        if senha:
            senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            partes.insert(2, f"usu_senha = '{senha_hash}'")

        sql = f"UPDATE usuario SET {', '.join(partes)} WHERE usu_id = {id};"
        return self.model.update(sql)

    def to_dict(self, usuario: tuple) -> dict:
        """
        Converte uma tupla de usuário em dicionário.

        Args:
            usuario (tuple): Tupla retornada pelo banco.

        Returns:
            dict: Representação do usuário no formato dicionário.
        """
        return {
            "id": usuario[self.indices_campos["id"]],
            "nick": usuario[self.indices_campos["nick"]],
            "email": usuario[self.indices_campos["email"]],
            "senha": usuario[self.indices_campos["senha"]],
            "tipo": usuario[self.indices_campos["tipo"]],
        }
