from model import model_base

class InsumoController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de insumo para seus índices.
        # Tupla: (id, nome, media_consumida, quantidade_estoque, medida_id)
        # Atenção: se a estrutura do banco mudar, atualize os índices neste dicionário.
        self.indices_campos = {
            "id": 0,
            "nome": 1,
            "media_consumida": 2,
            "quantidade_estoque": 3,
            "medida_id": 4,
        }

    def inserir_insumo(self, nome: str, media_consumida: float, quantidade_estoque: float, medida_id: int) -> int:
        """
        Insere um insumo no banco.

        Args:
            nome (str): Nome do insumo.
            media_consumida (float): Média de consumo do insumo.
            quantidade_estoque (float): Quantidade disponível em estoque.
            medida_id (int): ID da unidade de medida.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = (
            "INSERT INTO insumo(ins_nome, ins_media_consumida, ins_quantidade_estoque, ins_med_id) "
            f"VALUES ('{nome}', {media_consumida}, {quantidade_estoque}, {medida_id});"
        )
        return self.model.insert(sql)

    def listar_insumo(self, nome: str = '') -> list[dict]:
        """
        Lista os insumos cujo nome contenha o termo de busca.

        Args:
            nome (str): Termo de busca. Padrão ''.

        Returns:
            list[dict]: Lista de insumos como dicionários.
        """
        sql = f'SELECT * FROM insumo WHERE ins_nome LIKE "%{nome}%";'
        resultado = self.model.get(sql)
        return [self.to_dict(i) for i in resultado] if resultado else []

    def excluir_insumo(self, id: int) -> int:
        """
        Exclui um insumo pelo ID.

        Args:
            id (int): ID do insumo.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'DELETE FROM insumo WHERE ins_id = {id};'
        return self.model.delete(sql)

    def atualizar_insumo(self, id: int, nome: str, media_consumida: float, quantidade_estoque: float, medida_id: int) -> int:
        """
        Atualiza os dados de um insumo.

        Args:
            id (int): ID do insumo.
            nome (str): Novo nome.
            media_consumida (float): Nova média de consumo.
            quantidade_estoque (float): Nova quantidade em estoque.
            medida_id (int): Novo ID da unidade de medida.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = (
            "UPDATE insumo SET "
            f"ins_nome = '{nome}', ins_media_consumida = {media_consumida}, "
            f"ins_quantidade_estoque = {quantidade_estoque}, ins_med_id = {medida_id} "
            f"WHERE ins_id = {id};"
        )
        return self.model.update(sql)

    def to_dict(self, insumo: tuple) -> dict:
        """
        Converte uma tupla de insumo em dicionário.

        Args:
            insumo (tuple): Tupla com os campos do insumo.

        Returns:
            dict: Insumo no formato dicionário.
        """
        return {
            "id": insumo[self.indices_campos["id"]],
            "nome": insumo[self.indices_campos["nome"]],
            "media_consumida": insumo[self.indices_campos["media_consumida"]],
            "quantidade_estoque": insumo[self.indices_campos["quantidade_estoque"]],
            "medida_id": insumo[self.indices_campos["medida_id"]],
        }
