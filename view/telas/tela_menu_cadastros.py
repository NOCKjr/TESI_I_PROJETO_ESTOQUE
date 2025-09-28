import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_base import TelaBase

class TelaMenuCadastros(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        ### Container com as opções de navegação disponíveis
        self.container_visual = tk.Frame(self, bg=constants.cores['branco'], padx=30, pady=20)
        self.container_visual.place(anchor='center', relx=0.5, rely=0.45)

        ## Botão Cadastrar Usuário
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastrar Usuário', bg=constants.cores['principal'], fg=constants.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_USUARIO))
        self.btn_continuar.grid(row=0, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
        
        ## Botão Cadastrar Escola
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastrar Escola', bg=constants.cores['principal'], fg=constants.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_ESCOLA))
        self.btn_continuar.grid(row=1, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
        
        ## Botão Cadastrar Fornecedor
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastrar Fornecedor', bg=constants.cores['principal'], fg=constants.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_FORNECEDOR))
        self.btn_continuar.grid(row=2, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
        
        ## Botão Cadastrar Insumo
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastrar Insumo', bg=constants.cores['principal'], fg=constants.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_INSUMO))
        self.btn_continuar.grid(row=3, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
        
        ## Voltar ao Menu
        self.btn_continuar = tk.Button(self.container_visual, text='Voltar ao Menu', bg=constants.cores['principal'], fg=constants.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_MENU_PRINCIPAL))
        self.btn_continuar.grid(row=4, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)

    
    def test(self, event):
        print('Testando bind!')
    