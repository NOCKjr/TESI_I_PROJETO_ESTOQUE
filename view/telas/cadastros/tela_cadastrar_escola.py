import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_formulario_base import TelaFormularioBase

class TelaCadastrarEscola(TelaFormularioBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)
        
        # Nome
        self.lbl_nome = tk.Label(self.container_formulario, text="Nome da escola:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_nome.grid(row=1, column=0, pady=(0,0), sticky='nsw')
        self.ent_nome = tk.Entry(self.container_formulario)
        self.ent_nome.grid(row=2, column=0, columnspan=30, sticky='nsew')
        # Número de alunos
        self.lbl_numero_alunos = tk.Label(self.container_formulario, text="Número de Alunos:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_numero_alunos.grid(row=3, column=0, pady=(2,0), sticky='nsw')
        self.ent_numero_alunos = tk.Entry(self.container_formulario)
        self.ent_numero_alunos.grid(row=4, column=0, columnspan=4, sticky='nsew')
        
        ## Endereço

        # Logradouro
        self.lbl_logradouro = tk.Label(self.container_formulario, text="Logradouro:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_logradouro.grid(row=7, column=0, pady=(2,0), sticky='nsw')
        self.ent_logradouro = tk.Entry(self.container_formulario)
        self.ent_logradouro.grid(row=8, column=0, columnspan=30, sticky='nsew')
        # Bairro
        self.lbl_bairro = tk.Label(self.container_formulario, text="Bairro:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_bairro.grid(row=11, column=0, pady=(2,0), sticky='nsw')
        self.ent_bairro = tk.Entry(self.container_formulario)
        self.ent_bairro.grid(row=12, column=0, columnspan=26, sticky='nsew')
        # Número
        self.lbl_numero = tk.Label(self.container_formulario, text="Número:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_numero.grid(row=11, column=26, pady=(2,0), sticky='nsw')
        self.ent_numero = tk.Entry(self.container_formulario)
        self.ent_numero.grid(row=12, column=26, columnspan=4, sticky='nsew')
        # Estado
        self.lbl_estado = tk.Label(self.container_formulario, text="Estado:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_estado.grid(row=15, column=0, pady=(2,0), sticky='nsw')
        self.ent_estado = tk.Entry(self.container_formulario)
        self.ent_estado.grid(row=16, column=0, columnspan=20, sticky='nsew')
        # CEP
        self.lbl_cep = tk.Label(self.container_formulario, text="CEP:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_cep.grid(row=15, column=20, pady=(2,0), sticky='nsw')
        self.ent_cep = tk.Entry(self.container_formulario)
        self.ent_cep.grid(row=16, column=20, columnspan=10, sticky='nsew')
