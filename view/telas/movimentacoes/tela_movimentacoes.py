import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_base import TelaBase

class TelaMovimentacoes(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        self.btn_adicionar = tk.Button(self, text="Nova Movimentação", command=lambda: self.onAdicionar())
        self.btn_adicionar.pack()
    
    def onAdicionar(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_FORMULARIO_MOVIMENTACOES)


