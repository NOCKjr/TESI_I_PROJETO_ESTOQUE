import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_interface import TelaInterface

class TelaMenuCadastros(TelaInterface):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')

        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['branco'])
        self.lbl_sigeme.pack(side='top')

        ### Container com as opções de navegação disponíveis
        self.container_visual = tk.Frame(self, bg=self.cores['branco'], padx=30, pady=20)
        self.container_visual.place(anchor='center', relx=0.5, rely=0.45)

        ## Botão Cadastrar Usuário
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastrar Usuário', bg=self.cores['principal'], fg=self.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_USUARIO))
        self.btn_continuar.grid(row=0, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
        
        ## Botão Cadastrar Escola
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastrar Escola', bg=self.cores['principal'], fg=self.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_ESCOLA))
        self.btn_continuar.grid(row=1, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
        
        ## Botão Cadastrar Fornecedor
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastrar Fornecedor', bg=self.cores['principal'], fg=self.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_FORNECEDOR))
        self.btn_continuar.grid(row=2, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
        
        ## Botão Cadastrar Insumo
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastrar Insumo', bg=self.cores['principal'], fg=self.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_INSUMO))
        self.btn_continuar.grid(row=3, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
        
        ## Voltar ao Menu
        self.btn_continuar = tk.Button(self.container_visual, text='Voltar ao Menu', bg=self.cores['principal'], fg=self.cores['branco'], command=lambda: self.alterar_para_a_tela(constants.TELA_MENU_PRINCIPAL))
        self.btn_continuar.grid(row=4, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)

    
    def mostrar(self):
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        self.pack_forget()

    def test(self, event):
        print('Testando bind!')
    
    def alterar_para_a_tela(self, proxima_tela):
        self.gerenciador_de_janelas.alterar_para_a_tela(proxima_tela)

