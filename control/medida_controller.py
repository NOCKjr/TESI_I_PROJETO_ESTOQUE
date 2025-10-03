from control.controller_base import ControllerBase
from model.model_base import ResponseQuery

class MedidaController(ControllerBase):
    def __init__(self):
        """
        Controller responsável por intermediar operações entre a aplicação e o banco
        de dados para a entidade 'medida'.
        """

        # Mapeamento dos campos da tupla de medida para seus índices.
        self.indices_campos = {
            "id": 0,
            "unidade": 1,
        }

        # Funções de callback para operações CRUD 
        self.funcao_inserir_item = self.inserir_medida
        self.funcao_listar_item = self.listar_medida
        # self.funcao_buscar_item = self.buscar_medida
        # self.funcao_buscar_item_por_id = self.buscar_medida_por_id
        self.funcao_excluir_item = self.excluir_medida
        self.funcao_atualizar_item = self.atualizar_medida
        # self.funcao_to_dict = self.to_dict_medida

    def inserir_medida(self, unidade: str) -> ResponseQuery:
        """
        Insere uma unidade de medida no banco.

        Args:
            unidade (str): Unidade de medida (ex: 'kg', 'litro').

        Returns:
            ResponseQuery:
                - `retorno`: ID da medida inserida.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"INSERT INTO medida(med_unidade) VALUES ('{unidade}');"
        return self.model.insert(sql)

    def listar_medida(self, unidade: str = '') -> ResponseQuery:
        """
        Lista as medidas que contenham a string informada.

        Args:
            unidade (str): Termo de busca (parte do nome da unidade). Padrão ''.

        Returns:
            ResponseQuery:
                - `retorno`: lista de medidas como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'SELECT * FROM medida WHERE med_unidade LIKE "%{unidade}%";'
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(m) for m in resp.retorno]
        return resp

    def buscar_medida(self, id: int) -> ResponseQuery:
        """
        Busca uma unidade de medida pelo ID.

        Args:
            id (int): ID da medida a ser buscada.

        Returns:
            ResponseQuery:
                - `retorno`: dicionário da medida, ou None se não encontrada.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"SELECT * FROM medida WHERE med_id = {id};"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = self.to_dict(resp.retorno[0]) if resp.retorno else None
        return resp

    def excluir_medida(self, id: int) -> ResponseQuery:
        """
        Exclui uma unidade de medida pelo ID.

        Args:
            id (int): ID da medida.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'DELETE FROM medida WHERE med_id = {id};'
        return self.model.delete(sql)

    def atualizar_medida(self, id: int, unidade: str) -> ResponseQuery:
        """
        Atualiza uma unidade de medida existente.

        Args:
            id (int): ID da medida.
            unidade (str): Novo nome da unidade.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"UPDATE medida SET med_unidade = '{unidade}' WHERE med_id = {id};"
        return self.model.update(sql)

    def to_dict(self, medida: tuple) -> dict:
        """
        Converte uma tupla de medida em dicionário.

        Args:
            medida (tuple): Tupla com os campos da medida.

        Returns:
            dict: Medida no formato dicionário.
        """
        return {
            "id": medida[self.indices_campos["id"]],
            "unidade": medida[self.indices_campos["unidade"]],
        }
