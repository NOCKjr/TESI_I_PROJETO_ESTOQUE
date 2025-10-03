from model.model_base import ModelBase, ResponseQuery

class InsumoController:
    def __init__(self):
        """
        Controller responsável por intermediar operações entre a aplicação e o banco
        de dados para a entidade 'insumo'.
        """
        self.model = ModelBase()

        # Mapeamento dos campos da tupla de fornecedor para seus índices.
        self.indices_campos = {
            "id": 0,
            "nome": 1,
            "media_consumida": 2,
            "quantidade_estoque": 3,
            "medida_id": 4,
        }

    def inserir_insumo(self, nome: str, media_consumida: float, quantidade_estoque: float, medida_id: int) -> ResponseQuery:
        """Insere um insumo no banco."""
        sql = (
            "INSERT INTO insumo(ins_nome, ins_media_consumida, ins_quantidade_estoque, ins_med_id) "
            f"VALUES ('{nome}', {media_consumida}, {quantidade_estoque}, {medida_id});"
        )
        return self.model.insert(sql)

    def listar_insumo(self, nome: str = '') -> ResponseQuery:
        """Lista insumos filtrando pelo nome."""
        sql = f'SELECT * FROM insumo WHERE ins_nome LIKE "%{nome}%";'
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(i) for i in resp.retorno]
        return resp

    def excluir_insumo(self, id: int) -> ResponseQuery:
        """Exclui um insumo pelo ID."""
        sql = f'DELETE FROM insumo WHERE ins_id = {id};'
        return self.model.delete(sql)

    def atualizar_insumo(self, id: int, nome: str, media_consumida: float, quantidade_estoque: float, medida_id: int) -> ResponseQuery:
        """Atualiza os dados de um insumo."""
        sql = (
            "UPDATE insumo SET "
            f"ins_nome = '{nome}', ins_media_consumida = {media_consumida}, "
            f"ins_quantidade_estoque = {quantidade_estoque}, ins_med_id = {medida_id} "
            f"WHERE ins_id = {id};"
        )
        return self.model.update(sql)

    def to_dict(self, insumo: tuple) -> dict:
        """Converte uma tupla de insumo em dicionário."""
        return {
            "id": insumo[self.indices_campos["id"]],
            "nome": insumo[self.indices_campos["nome"]],
            "media_consumida": insumo[self.indices_campos["media_consumida"]],
            "quantidade_estoque": insumo[self.indices_campos["quantidade_estoque"]],
            "medida_id": insumo[self.indices_campos["medida_id"]],
        }
