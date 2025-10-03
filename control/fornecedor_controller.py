from model import model_base
from model.model_base import ResponseQuery

class FornecedorController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de fornecedor para seus índices.
        self.indices_campos = {
            "id": 0,
            "razao_social": 1,
            "contato": 2,
        }

    def inserir_fornecedor(self, razao_social: str, contato: str = '') -> ResponseQuery:
        """Insere um fornecedor no banco."""
        sql = f"INSERT INTO fornecedor(for_razao_social, for_contato) VALUES ('{razao_social}', '{contato}');"
        return self.model.insert(sql)

    def listar_fornecedor(self, razao_social: str = '') -> ResponseQuery:
        """Lista fornecedores filtrando pela razão social."""
        sql = f'SELECT * FROM fornecedor WHERE for_razao_social LIKE "%{razao_social}%";'
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(f) for f in resp.retorno]
        return resp

    def excluir_fornecedor(self, id: int) -> ResponseQuery:
        """Exclui um fornecedor pelo ID."""
        sql = f'DELETE FROM fornecedor WHERE for_id = {id};'
        return self.model.delete(sql)

    def atualizar_fornecedor(self, id: int, razao_social: str, contato: str) -> ResponseQuery:
        """Atualiza os dados de um fornecedor."""
        sql = f'UPDATE fornecedor SET for_razao_social = "{razao_social}", for_contato = "{contato}" WHERE for_id = {id};'
        return self.model.update(sql)

    def to_dict(self, fornecedor: tuple) -> dict:
        """Converte uma tupla de fornecedor em dicionário."""
        return {
            "id": fornecedor[self.indices_campos["id"]],
            "razao_social": fornecedor[self.indices_campos["razao_social"]],
            "contato": fornecedor[self.indices_campos["contato"]],
        }
