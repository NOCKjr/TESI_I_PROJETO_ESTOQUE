from control.controller_base import ControllerBase
from control.item_controller import ItemController
from model.model_base import ResponseQuery

class MovimentacaoController(ControllerBase):
    def __init__(self):
        super().__init__()
        """
        Controller responsável por intermediar operações entre a aplicação e o banco
        de dados para a entidade 'movimentacao'.
        """
        
        # Controladores
        self.controle_itens = ItemController()
        
        # Mapeamento dos campos da tupla de movimentação para seus índices.
        self.indices_campos = {
            "id": 0,
            "data": 1,
            "tipo": 2,
            "usuario_id": 3,
            "fornecedor_id": 4,
            "escola_id": 5,
        }

        # Funções de callback para operações CRUD 
        self.funcao_inserir_item = self.inserir_movimentacao
        self.funcao_listar_item = self.listar_movimentacao
        # self.funcao_buscar_item = self.buscar_movimentacao
        self.funcao_buscar_item_por_id = self.buscar_movimentacao_por_id
        self.funcao_excluir_item = self.excluir_movimentacao
        self.funcao_atualizar_item = self.atualizar_movimentacao
        # self.funcao_to_dict = self.to_dict_movimentacao

    def inserir_movimentacao(self, data: str, tipo: str, usuario_id: int, fornecedor_id: int = None, escola_id: int = None, itens: list[dict] = []) -> ResponseQuery:
        """
        Insere uma movimentação no banco.

        Args:
            data (str): Data da movimentação.
            tipo (str): Tipo da movimentação.
            usuario_id (int): ID do usuário.
            fornecedor_id (int): ID do fornecedor.
            escola_id (int): ID da escola.

        Returns:
            ResponseQuery: 
                - `retorno`: ID da movimentação inserida.
                - `erros`: lista de erros em caso de falha.
        """
        from utils import tratar_data_sql

        data_sql = tratar_data_sql(data)
        if not data_sql:
            return ResponseQuery(erros=["Data inválida ou vazia."])

        sql = (
            "INSERT INTO movimentacao(mov_data, mov_tipo, fk_mov_usu_id, fk_mov_for_id, fk_mov_esc_id) "
            "VALUES (?, ?, ?, ?, ?);"
        )
        valores = (data_sql, tipo, usuario_id, fornecedor_id, escola_id)
        return self.model.insert(sql, valores)

    def listar_movimentacao(self, termo_buscar: str = "") -> ResponseQuery:
        """
        Lista todas as movimentações ordenadas por data decrescente.

        Returns:
            ResponseQuery:
                - `retorno`: lista de movimentações como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = "SELECT * FROM movimentacao ORDER BY mov_data DESC, mov_id DESC;"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(m) for m in resp.retorno]
        return resp

    def buscar_movimentacao_por_id(self, id: int) -> ResponseQuery:
        """
        Busca uma movimentação pelo ID.

        Args:
            id (int): ID da movimentação.

        Returns:
            ResponseQuery:
                - `retorno`: movimentação como dicionário.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"SELECT * FROM movimentacao WHERE mov_id = {id};"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        if not resp.retorno:
            return ResponseQuery(erros=[f"Movimentação com ID {id} não encontrada."])
        resp.retorno = self.to_dict(resp.retorno[0])
        return resp

    def listar_movimentacao_por_fornecedor(self, fornecedor_id: int) -> ResponseQuery:
        """
        Lista movimentações filtradas por fornecedor.

        Args:
            fornecedor_id (int): ID do fornecedor.

        Returns:
            ResponseQuery:
                - `retorno`: lista de movimentações como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"SELECT * FROM movimentacao WHERE fk_mov_for_id = {fornecedor_id} ORDER BY mov_data DESC;"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(m) for m in resp.retorno]
        return resp

    def listar_movimentacao_por_escola(self, escola_id: int) -> ResponseQuery:
        """
        Lista movimentações filtradas por escola.

        Args:
            escola_id (int): ID da escola.

        Returns:
            ResponseQuery:
                - `retorno`: lista de movimentações como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"SELECT * FROM movimentacao WHERE fk_mov_esc_id = {escola_id} ORDER BY mov_data DESC;"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(m) for m in resp.retorno]
        return resp

    def listar_movimentacao_por_usuario(self, usuario_id: int) -> ResponseQuery:
        """
        Lista movimentações filtradas por usuário.

        Args:
            usuario_id (int): ID do usuário.

        Returns:
            ResponseQuery:
                - `retorno`: lista de movimentações como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"SELECT * FROM movimentacao WHERE fk_mov_usu_id = {usuario_id} ORDER BY mov_data DESC;"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(m) for m in resp.retorno]
        return resp

    def excluir_movimentacao(self, id: int) -> ResponseQuery:
        """
        Exclui uma movimentação pelo ID.

        Args:
            id (int): ID da movimentação.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"DELETE FROM movimentacao WHERE mov_id = {id};"
        return self.model.delete(sql)

    def atualizar_movimentacao(self, id: int, data: str, tipo: str, usuario_id: int, fornecedor_id: int, escola_id: int) -> ResponseQuery:
        """
        Atualiza uma movimentação existente.

        Args:
            id (int): ID da movimentação.
            data (str): Nova data.
            tipo (str): Novo tipo.
            usuario_id (int): ID do usuário.
            fornecedor_id (int): ID do fornecedor.
            escola_id (int): ID da escola.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"""UPDATE movimentacao SET mov_data = '{data}', 
                  mov_tipo = '{tipo}', 
                  fk_mov_usu_id = {usuario_id},
                  fk_mov_for_id = {fornecedor_id},
                  fk_mov_esc_id = {escola_id}
                  WHERE mov_id = {id};"""
        return self.model.update(sql)

    def to_dict(self, movimentacao: tuple) -> dict:
        """
        Converte uma tupla de movimentação em dicionário.

        Args:
            movimentacao (tuple): Tupla com os campos da movimentação.

        Returns:
            dict: Movimentação no formato dicionário.
        """
        return {
            "id": movimentacao[self.indices_campos["id"]],
            "data": movimentacao[self.indices_campos["data"]],
            "tipo": movimentacao[self.indices_campos["tipo"]],
            "usuario_id": movimentacao[self.indices_campos["usuario_id"]],
            "fornecedor_id": movimentacao[self.indices_campos["fornecedor_id"]],
            "escola_id": movimentacao[self.indices_campos["escola_id"]],
        }
