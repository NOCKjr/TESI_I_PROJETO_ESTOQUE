from model import model_base

class MovimentacaoController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de movimentação para seus índices.
        # Tupla: (id, data, tipo, fk_mov_usu_id, fk_mov_for_id, fk_mov_esc_id)
        # Atenção: se a estrutura do banco mudar, atualize os índices neste dicionário.
        self.indices_campos = {
            "id": 0,
            "data": 1,
            "tipo": 2,
            "usuario_id": 3,
            "fornecedor_id": 4,
            "escola_id": 5,
        }

    def inserir_movimentacao(self, data: str, tipo: str, usuario_id: int, fornecedor_id: int, escola_id: int) -> int:
        """
        Insere uma movimentação no banco.

        Args:
            data (str): Data da movimentação.
            tipo (str): Tipo da movimentação.
            usuario_id (int): ID do usuário.
            fornecedor_id (int): ID do fornecedor.
            escola_id (int): ID da escola.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = (
            "INSERT INTO movimentacao(mov_data, mov_tipo, fk_mov_usu_id, fk_mov_for_id, fk_mov_esc_id) "
            f"VALUES ('{data}', '{tipo}', {usuario_id}, {fornecedor_id}, {escola_id});"
        )
        return self.model.insert(sql)

    def listar_movimentacao(self) -> list[dict]:
        """
        Lista todas as movimentações ordenadas por data decrescente.

        Returns:
            list[dict]: Lista de movimentações como dicionários.
        """
        sql = "SELECT * FROM movimentacao ORDER BY mov_data DESC;"
        resultado = self.model.get(sql)
        return [self.to_dict(m) for m in resultado] if resultado else []

    def listar_movimentacao_por_fornecedor(self, fornecedor_id: int) -> list[dict]:
        """
        Lista as movimentações filtradas por fornecedor.

        Args:
            fornecedor_id (int): ID do fornecedor.

        Returns:
            list[dict]: Lista de movimentações como dicionários.
        """
        sql = f"SELECT * FROM movimentacao WHERE fk_mov_for_id = {fornecedor_id} ORDER BY mov_data DESC;"
        resultado = self.model.get(sql)
        return [self.to_dict(m) for m in resultado] if resultado else []

    def listar_movimentacao_por_escola(self, escola_id: int) -> list[dict]:
        """
        Lista as movimentações filtradas por escola.

        Args:
            escola_id (int): ID da escola.

        Returns:
            list[dict]: Lista de movimentações como dicionários.
        """
        sql = f"SELECT * FROM movimentacao WHERE fk_mov_esc_id = {escola_id} ORDER BY mov_data DESC;"
        resultado = self.model.get(sql)
        return [self.to_dict(m) for m in resultado] if resultado else []

    def listar_movimentacao_por_usuario(self, usuario_id: int) -> list[dict]:
        """
        Lista as movimentações filtradas por usuário.

        Args:
            usuario_id (int): ID do usuário.

        Returns:
            list[dict]: Lista de movimentações como dicionários.
        """
        sql = f"SELECT * FROM movimentacao WHERE fk_mov_usu_id = {usuario_id} ORDER BY mov_data DESC;"
        resultado = self.model.get(sql)
        return [self.to_dict(m) for m in resultado] if resultado else []

    def excluir_movimentacao(self, id: int) -> int:
        """
        Exclui uma movimentação pelo ID.

        Args:
            id (int): ID da movimentação.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f"DELETE FROM movimentacao WHERE mov_id = {id};"
        return self.model.delete(sql)

    def atualizar_movimentacao(self, id: int, data: str, tipo: str, usuario_id: int, fornecedor_id: int, escola_id: int) -> int:
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
            int: Número de linhas afetadas.
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
