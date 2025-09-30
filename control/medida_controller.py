from model import model_base

class MedidaController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de medida para seus índices.
        # Tupla: (id, unidade)
        # Atenção: se a estrutura do banco mudar, atualize os índices neste dicionário.
        self.indices_campos = {
            "id": 0,
            "unidade": 1
        }

    def inserir_medida(self, unidade: str) -> int:
        """
        Insere uma unidade de medida no banco.

        Args:
            unidade (str): Unidade de medida (ex: 'kg', 'litro').

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f"INSERT INTO medida(med_unidade) VALUES ('{unidade}');"
        return self.model.insert(sql)

    def listar_medida(self, unidade: str = '') -> list[dict]:
        """
        Lista as medidas que contenham a string informada.

        Args:
            unidade (str): Termo de busca (parte do nome da unidade). Padrão ''.

        Returns:
            list[dict]: Lista de medidas como dicionários.
        """
        sql = f'SELECT * FROM medida WHERE med_unidade LIKE "%{unidade}%";'
        resultado = self.model.get(sql)
        return [self.to_dict(m) for m in resultado] if resultado else []

    def excluir_medida(self, id: int) -> int:
        """
        Exclui uma unidade de medida pelo ID.

        Args:
            id (int): ID da medida.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'DELETE FROM medida WHERE med_id = {id};'
        return self.model.delete(sql)

    def atualizar_medida(self, id: int, unidade: str) -> int:
        """
        Atualiza uma unidade de medida existente.

        Args:
            id (int): ID da medida.
            unidade (str): Novo nome da unidade.

        Returns:
            int: Número de linhas afetadas.
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
