from model import model_base

class EscolaController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de escola para seus índices.
        # Tupla: (id, nome, numero_alunos, endereco_id)
        # Atenção: se a estrutura do banco mudar, atualize os índices neste dicionário.
        self.indices_campos = {
            "id": 0,
            "nome": 1,
            "numero_alunos": 2,
            "endereco_id": 3,
        }

    def inserir_escola(self, nome: str, endereco_id: int, numero_alunos: int = 0) -> int:
        """
        Insere uma escola no banco.

        Args:
            nome (str): Nome da escola.
            endereco_id (int): ID do endereço.
            numero_alunos (int): Número de alunos. Padrão 0.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f"INSERT INTO escola(esc_nome, esc_numero_alunos, esc_end_id) VALUES ('{nome}', {numero_alunos}, {endereco_id});"
        return self.model.insert(sql)

    def listar_escola(self, nome: str = '') -> list[dict]:
        """
        Lista escolas cujo nome contenha o termo informado.

        Args:
            nome (str): Termo de busca. Padrão ''.

        Returns:
            list[dict]: Lista de escolas como dicionários.
        """
        sql = f'SELECT * FROM escola WHERE esc_nome LIKE "%{nome}%";'
        resultado = self.model.get(sql)
        return [self.to_dict(e) for e in resultado] if resultado else []

    def excluir_escola(self, id: int) -> int:
        """
        Exclui uma escola pelo ID.

        Args:
            id (int): ID da escola.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'DELETE FROM escola WHERE esc_id = {id};'
        return self.model.delete(sql)

    def atualizar_escola(self, id: int, nome: str, numero_alunos: int, endereco_id: int) -> int:
        """
        Atualiza os dados de uma escola.

        Args:
            id (int): ID da escola.
            nome (str): Novo nome.
            numero_alunos (int): Novo número de alunos.
            endereco_id (int): Novo ID do endereço.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f"""UPDATE escola 
                    SET esc_nome = '{nome}', 
                        esc_numero_alunos = {numero_alunos}, 
                        esc_end_id = {endereco_id}
                  WHERE esc_id = {id};"""
        return self.model.update(sql)

    def to_dict(self, escola: tuple) -> dict:
        """
        Converte uma tupla de escola em dicionário.

        Args:
            escola (tuple): Tupla com os campos da escola.

        Returns:
            dict: Escola no formato dicionário.
        """
        return {
            "id": escola[self.indices_campos["id"]],
            "nome": escola[self.indices_campos["nome"]],
            "numero_alunos": escola[self.indices_campos["numero_alunos"]],
            "endereco_id": escola[self.indices_campos["endereco_id"]],
        }
