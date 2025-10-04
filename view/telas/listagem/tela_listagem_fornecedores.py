import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.fornecedor_controller import FornecedorController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.listagem.tela_listagem_base import TelaListagemBase

class TelaListagemFornecedores(TelaListagemBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, constants.ENTIDADE_FORNECEDOR, FornecedorController(), ['ID', 'RAZÃO SOCIAL', 'CONTATO'], ['id', 'razao_social', 'contato'])
