from control.controller_base import ControllerBase
from model.model_base import ResponseQuery

class EscolaController(ControllerBase):
    def __init__(self):
        """
        Controller responsável por intermediar operações entre a aplicação e o banco
        de dados para a entidade 'escola'.
        """
        
        # Mapeamento dos campos da tupla de endereço para seus índices.
        self.indices_campos = {
            "id": 0,
            "nome": 1,
            "numero_alunos": 2,
            "endereco_id": 3,
        }

        # Funções de callback para operações CRUD 
        self.funcao_inserir_item = self.inserir_escola
        self.funcao_listar_item = self.listar_escola
        # self.funcao_buscar_item = self.buscar_escola
        self.funcao_buscar_item_por_id = self.buscar_escola_por_id
        self.funcao_excluir_item = self.excluir_escola
        self.funcao_atualizar_item = self.atualizar_escola
        # self.funcao_to_dict = self.to_dict_escola

    def inserir_escola(self, nome: str, endereco_id: int, numero_alunos: int = 0) -> ResponseQuery:
        """
        Insere uma escola no banco.

        Args:
            nome (str): Nome da escola.
            endereco_id (int): ID do endereço.
            numero_alunos (int): Número de alunos. Padrão 0.

        Returns:
            ResponseQuery:
                - `retorno`: ID da escola inserida.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"INSERT INTO escola(esc_nome, esc_numero_alunos, esc_end_id) VALUES ('{nome}', {numero_alunos}, {endereco_id});"
        return self.model.insert(sql)

    def listar_escola(self, nome: str = '') -> ResponseQuery:
        """
        Lista escolas cujo nome contenha o termo informado.

        Args:
            nome (str): Termo de busca. Padrão ''.

        Returns:
            ResponseQuery:
                - `retorno`: lista de escolas como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'SELECT * FROM escola WHERE esc_nome LIKE "%{nome}%";'
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(e) for e in resp.retorno]
        return resp

    def excluir_escola(self, id: int) -> ResponseQuery:
        """Exclui uma escola pelo ID."""
        sql = f'DELETE FROM escola WHERE esc_id = {id};'
        return self.model.delete(sql)

    def atualizar_escola(self, id: int, nome: str, numero_alunos: int, endereco_id: int) -> ResponseQuery:
        """Atualiza os dados de uma escola."""
        sql = f"""UPDATE escola 
                    SET esc_nome = '{nome}', 
                        esc_numero_alunos = {numero_alunos}, 
                        esc_end_id = {endereco_id}
                  WHERE esc_id = {id};"""
        return self.model.update(sql)

    def buscar_escola_por_id(self, id: int) -> ResponseQuery:
        """Busca uma escola pelo ID e retorna como dicionário."""
        sql = f"SELECT * FROM escola WHERE esc_id = {id};"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = self.to_dict(resp.retorno[0]) if resp.retorno else None
        return resp

    def to_dict(self, escola: tuple) -> dict:
        """Converte uma tupla de escola em dicionário."""
        return {
            "id": escola[self.indices_campos["id"]],
            "nome": escola[self.indices_campos["nome"]],
            "numero_alunos": escola[self.indices_campos["numero_alunos"]],
            "endereco_id": escola[self.indices_campos["endereco_id"]],
        }
