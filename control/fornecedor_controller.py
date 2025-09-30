from model import model_base

class FornecedorController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de fornecedor para seus índices.
        # Tupla: (id, razao_social, contato)
        # Atenção: se a estrutura do banco mudar, atualize os índices neste dicionário.
        self.indices_campos = {
            "id": 0,
            "razao_social": 1,
            "contato": 2,
        }

    def inserir_fornecedor(self, razao_social: str, contato: str = '') -> int:
        """
        Insere um fornecedor no banco.

        Args:
            razao_social (str): Razão social do fornecedor.
            contato (str): Informação de contato. Padrão ''.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f"INSERT INTO fornecedor(for_razao_social, for_contato) VALUES ('{razao_social}', '{contato}');"
        return self.model.insert(sql)

    def listar_fornecedor(self, razao_social: str = '') -> list[dict]:
        """
        Lista fornecedores que contenham o termo de busca na razão social.

        Args:
            razao_social (str): Termo de busca. Padrão ''.

        Returns:
            list[dict]: Lista de fornecedores como dicionários.
        """
        sql = f'SELECT * FROM fornecedor WHERE for_razao_social LIKE "%{razao_social}%";'
        resultado = self.model.get(sql)
        return [self.to_dict(f) for f in resultado] if resultado else []

    def excluir_fornecedor(self, id: int) -> int:
        """
        Exclui um fornecedor pelo ID.

        Args:
            id (int): ID do fornecedor.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'DELETE FROM fornecedor WHERE for_id = {id};'
        return self.model.delete(sql)

    def atualizar_fornecedor(self, id: int, razao_social: str, contato: str) -> int:
        """
        Atualiza os dados de um fornecedor.

        Args:
            id (int): ID do fornecedor.
            razao_social (str): Nova razão social.
            contato (str): Novo contato.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'UPDATE fornecedor SET for_razao_social = "{razao_social}", for_contato = "{contato}" WHERE for_id = {id};'
        return self.model.update(sql)

    def to_dict(self, fornecedor: tuple) -> dict:
        """
        Converte uma tupla de fornecedor em dicionário.

        Args:
            fornecedor (tuple): Tupla com os campos do fornecedor.

        Returns:
            dict: Fornecedor no formato dicionário.
        """
        return {
            "id": fornecedor[self.indices_campos["id"]],
            "razao_social": fornecedor[self.indices_campos["razao_social"]],
            "contato": fornecedor[self.indices_campos["contato"]],
        }
