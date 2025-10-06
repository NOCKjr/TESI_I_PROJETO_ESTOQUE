import ttkbootstrap as ttk
import constants

from control.endereco_controller import EnderecoController
from control.escola_controller import EscolaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.listagem.tela_listagem_base import TelaListagemBase

class TelaListagemEscolas(TelaListagemBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, constants.ENTIDADE_ESCOLA, EscolaController(), ['ID', 'NOME', 'ENDEREÇO', 'ALUNOS'], ['id', 'nome', 'endereco_id', 'numero_alunos'])
        
        # Controlador de endereço
        self.controle_endereco = EnderecoController()

    def dict_to_tuple(self, escola):
        """Mapeia os campos do dicionário escola para uma tupla"""
        return (
            escola["id"],
            escola["nome"],
            self.controle_endereco.buscar_endereco_string(escola["endereco_id"]).retorno,
            escola["numero_alunos"],
        )
