import tkinter as tk
import constants
import utils

from tkinter import ttk
from control.movimentacao_controller import MovimentacaoController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.cadastros.tela_formulario_base import TelaFormularioBase

class TelaCadastrarMovimentacao(TelaFormularioBase):
    def __init__(self, master, 
                       gerenciador_de_janelas: GerenciadorDeJanelasBase, 
                       modo_editar=False, 
                       largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, 
                         gerenciador_de_janelas, 
                         constants.ENTIDADE_MOVIMENTACAO, 
                         MovimentacaoController(), 
                         modo_editar,
                         largura, altura)

        self.criar_campos_formulario()
    
    def criar_campos_formulario(self):
        super().criar_campos_formulario()

        # Tipo de movimentação (Entrada ou Saída)
        self.lbl_tipo_movimentacao = ttk.Label(self.container_formulario, text="Tipo de movimentação:", anchor='w')
        self.lbl_tipo_movimentacao.grid(row=2, column=0, pady=(10, 0), sticky='nsw')
        self.cmb_tipo_movimentacao = ttk.Combobox(self.container_formulario, values=["Saída", "Entrada"], state="readonly")
        self.cmb_tipo_movimentacao.grid(row=3, column=0, columnspan=14, sticky='nsew')
        self.cmb_tipo_movimentacao.set("")

        # Data
        self.lbl_data = ttk.Label(self.container_formulario, text="Data:", anchor='w')
        self.lbl_data.grid(row=2, column=20, pady=(10, 0), sticky='nsw')
        self.ent_data = utils.DateEntry(self.container_formulario)
        self.ent_data.grid(row=3, column=20, columnspan=10, sticky='nsew')
        # self.lbl_data = ttk.Label(self.container_formulario, text="Data:", anchor='w')
        # self.lbl_data.grid(row=2, column=20, pady=(10, 0), sticky='nsw')
        # self.ent_data = ttk.Entry(self.container_formulario)
        # self.ent_data.grid(row=3, column=20, columnspan=10, sticky='nsew')

        # Usuário
        self.lbl_usuario = ttk.Label(self.container_formulario, text="Usuário:", anchor='w')
        self.lbl_usuario.grid(row=8, column=0, pady=(10, 0), sticky='nsw')
        self.ent_usuario = ttk.Entry(self.container_formulario)
        self.ent_usuario.grid(row=9, column=0, columnspan=14, sticky='nsew')

        # Fornecedor
        self.lbl_fornecedor = ttk.Label(self.container_formulario, text="Fornecedor:", anchor='w')
        self.lbl_fornecedor.grid(row=10, column=0, pady=(10, 0), sticky='nsw')
        self.ent_fornecedor = ttk.Entry(self.container_formulario)
        self.ent_fornecedor.grid(row=11, column=0, columnspan=14, sticky='nsew')

        # Escola
        self.lbl_escola = ttk.Label(self.container_formulario, text="Escola:", anchor='w')
        self.lbl_escola.grid(row=12, column=0, pady=(10, 0), sticky='nsw')
        self.ent_escola = ttk.Entry(self.container_formulario)
        self.ent_escola.grid(row=13, column=0, columnspan=14, sticky='nsew')


    def obter_valores_campos_formulario(self):
        # Captura os valores dos campos
        data = self.ent_data.get()
        tipo = self.cmb_tipo_movimentacao.get()
        usuario_id = self.ent_usuario.get()
        fornecedor_id = self.ent_fornecedor.get()
        escola_id = self.ent_escola.get()

        return (data, tipo, usuario_id, fornecedor_id, escola_id)

