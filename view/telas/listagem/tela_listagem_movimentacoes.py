import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.escola_controller import EscolaController
from control.fornecedor_controller import FornecedorController
from control.movimentacao_controller import MovimentacaoController
from control.usuario_controller import UsuarioController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.listagem.tela_listagem_base import TelaListagemBase

class TelaListagemMovimentacoes(TelaListagemBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, 
                         gerenciador_de_janelas, 
                         constants.ENTIDADE_MOVIMENTACAO, 
                         MovimentacaoController(), 
                         ['ID', 'DATA', 'TIPO', 'USUÁRIO', 'FORNECEDOR', 'ESCOLA'], 
                         ['id', 'data', 'tipo', 'usuario_id', 'fornecedor_id', 'escola_id'])

        # Controladores
        self.controle_escola = EscolaController()
        self.controle_usuario = UsuarioController()
        self.controle_fornecedor = FornecedorController()

    def dict_to_tuple(self, movimentacao):
        """Mapeia os campos do dicionário para uma tupla"""
        return tuple(
            movimentacao["id"],
            movimentacao["data"],
            movimentacao["tipo"],
            movimentacao["usuario_id"],
            movimentacao["fornecedor_id"],
            movimentacao["escola_id"],
        )
