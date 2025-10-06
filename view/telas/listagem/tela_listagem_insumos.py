from tkinter import ttk, messagebox
import constants

from control.insumo_controller import InsumoController
from control.medida_controller import MedidaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.listagem.tela_listagem_base import TelaListagemBase
from view.telas.menus.menu_painel_de_opcoes_crud import MenuPainelDeOpcoesCRUD

class TelaListagemInsumos(TelaListagemBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, constants.ENTIDADE_INSUMO, InsumoController(), ['ID', 'NOME', 'ESTOQUE', 'MÉDIA CONSUMIDA', 'UNIDADE'], ['id', 'nome', 'quantidade_estoque', 'media_consumida', 'medida_id'])

        # Controlador de unidade de medida
        self.controle_unidade_medida = MedidaController()

    def dict_to_tuple(self, insumo):
        """Mapeia os campos do dicionário para uma tupla"""
        return (
            insumo["id"],
            insumo["nome"],
            insumo["quantidade_estoque"],
            insumo["media_consumida"],
            self.controle_unidade_medida.buscar(insumo["medida_id"]).retorno["unidade"],
        )
