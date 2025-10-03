from model import model_base
from model.model_base import ResponseQuery

class ItemController:
    def __init__(self):
        """
        Controller responsável pelas operações de item no banco.
        """
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de item para seus índices.
        self.indices_campos = {
            "id": 0,
            "quantidade": 1,
            "insumo_id": 2,
            "movimentacao_id": 3,
        }

    def inserir_item(self, quantidade: float, insumo_id: int, movimentacao_id: int) -> ResponseQuery:
        """
        Insere um item associado a uma movimentação.

        Args:
            quantidade (float): Quantidade do item.
            insumo_id (int): ID do insumo.
            movimentacao_id (int): ID da movimentação.

        Returns:
            ResponseQuery:
                - `retorno`: ID do item inserido.
                - `erros`: lista de erros em caso de falha.
        """
        sql = (
            "INSERT INTO item(itm_quantidade, fk_itm_ins_id, fk_itm_mov_id) "
            f"VALUES ({quantidade}, {insumo_id}, {movimentacao_id});"
        )
        return self.model.insert(sql)

    def listar_item(self, movimentacao_id: int) -> ResponseQuery:
        """
        Lista os itens de uma movimentação.

        Args:
            movimentacao_id (int): ID da movimentação.

        Returns:
            ResponseQuery:
                - `retorno`: lista de itens como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'SELECT * FROM item WHERE fk_itm_mov_id = {movimentacao_id};'
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(i) for i in resp.retorno]
        return resp

    def excluir_item(self, id: int) -> ResponseQuery:
        """
        Exclui um item pelo ID.

        Args:
            id (int): ID do item.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'DELETE FROM item WHERE itm_id = {id};'
        return self.model.delete(sql)

    def atualizar_item(self, id: int, quantidade: float, insumo_id: int, movimentacao_id: int) -> ResponseQuery:
        """
        Atualiza os dados de um item existente.

        Args:
            id (int): ID do item.
            quantidade (float): Nova quantidade.
            insumo_id (int): Novo ID do insumo.
            movimentacao_id (int): Novo ID da movimentação.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = (
            "UPDATE item SET "
            f"itm_quantidade = {quantidade}, fk_itm_ins_id = {insumo_id}, fk_itm_mov_id = {movimentacao_id} "
            f"WHERE itm_id = {id};"
        )
        return self.model.update(sql)

    def to_dict(self, item: tuple) -> dict:
        """
        Converte uma tupla de item em dicionário.

        Args:
            item (tuple): Tupla com os campos do item.

        Returns:
            dict: Item no formato dicionário.
        """
        return {
            "id": item[self.indices_campos["id"]],
            "quantidade": item[self.indices_campos["quantidade"]],
            "insumo_id": item[self.indices_campos["insumo_id"]],
            "movimentacao_id": item[self.indices_campos["movimentacao_id"]],
        }
