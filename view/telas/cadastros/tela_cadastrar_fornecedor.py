import tkinter as tk
import constants

from tkinter import ttk
from control.fornecedor_controller import FornecedorController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_formulario_base import TelaFormularioBase

class TelaCadastrarFornecedor(TelaFormularioBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, modo_editar=False, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, modo_editar)

        # Se o formulário foi aberto como edição, define-se o id do fornecedor editado
        self.id_fornecedor_editado = None

        # Controlador de fornecedores
        self.controle_fornecedores = FornecedorController()

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

    def onConfirmar(self):
        ## --- valide os campos antes de inserir

        # Captura os valores dos campos
        razao_social = self.ent_razao_social.get()
        contato = self.ent_telefone_contato.get()

        if self.flag_editar:
            id = self.id_fornecedor_editado
            # Chama o controller para atualizar o fornecedor
            self.controle_fornecedores.atualizar_fornecedor(id, razao_social, contato)
        else:
            # Chama o controller para inserir novo fornecedor
            self.controle_fornecedores.inserir_fornecedor(razao_social, contato)
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()

        # Volta para a tela de listagem
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_FORNECEDORES)

    def onCancelar(self):
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()

        # Volta para a tela de listagem
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_FORNECEDORES)

    def limpar_campos(self):
        self.ent_razao_social.delete(0, 'end')
        self.ent_telefone_contato.delete(0, 'end')
        self.flag_editar = False

    def editar_fornecedor(self, fornecedor):
        self.ent_razao_social.delete(0, 'end')
        self.ent_razao_social.insert(0, fornecedor['razao-social'])
        self.ent_telefone_contato.delete(0, 'end')
        self.ent_telefone_contato.insert(0, fornecedor['contato'])
        self.id_fornecedor_editado = fornecedor['id']
        self.flag_editar = True

