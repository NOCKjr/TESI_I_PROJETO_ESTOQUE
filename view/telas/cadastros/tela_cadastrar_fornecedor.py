import tkinter as tk
import constants

from tkinter import ttk
from control.fornecedor_controller import FornecedorController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.cadastros.tela_formulario_base import TelaFormularioBase

class TelaCadastrarFornecedor(TelaFormularioBase):
    def __init__(self, master, 
                       gerenciador_de_janelas: GerenciadorDeJanelasBase, 
                       modo_editar=False, 
                       largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, 
                         gerenciador_de_janelas, 
                         constants.ENTIDADE_FORNECEDOR, 
                         FornecedorController(), 
                         modo_editar,
                         largura, altura)

        self.criar_campos_formulario()
    
    def criar_campos_formulario(self):
        super().criar_campos_formulario()

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

    def editar_fornecedor(self, fornecedor):
        self.ent_razao_social.delete(0, 'end')
        self.ent_razao_social.insert(0, fornecedor['razao_social']) 
        self.ent_telefone_contato.delete(0, 'end')
        self.ent_telefone_contato.insert(0, fornecedor['contato'])

        self.id_para_edicao = fornecedor['id']
        self.flag_editar = True

    def obter_valores_campos_formulario(self):
        # Captura os valores dos campos
        razao_social = self.ent_razao_social.get()
        contato = self.ent_telefone_contato.get()

        return (razao_social, contato)

