import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_formulario_base import TelaFormularioBase

class TelaCadastrarFornecedor(TelaFormularioBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        # Razão Social
        self.lbl_razao_social = tk.Label(self.container_formulario, text="Razão social:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_razao_social.grid(row=1, column=0, pady=(0,0), sticky='nsw')
        self.ent_razao_social = tk.Entry(self.container_formulario)
        self.ent_razao_social.grid(row=2, column=0, columnspan=30, sticky='nsew')

        # Telefone de contato
        self.lbl_telefone_contato = tk.Label(self.container_formulario, text="Telefone de contato:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_telefone_contato.grid(row=3, column=0, pady=(2,0), sticky='nsw')
        self.ent_telefone_contato = tk.Entry(self.container_formulario)
        self.ent_telefone_contato.grid(row=4, column=0, columnspan=4, sticky='nsew')

