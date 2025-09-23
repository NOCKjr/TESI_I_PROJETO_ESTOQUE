import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_interface import TelaInterface

class TelaMenuPrincipal(TelaInterface):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')

        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas

        self.cores = {
            "principal": '#075F8B',
            "secundario": '#87C5FF',
            "cinza": "#d9d9d9",
            'branco': '#ffffff'
        }

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['branco'])
        self.lbl_sigeme.pack(side='top')

        ### Botão logoff
        self.btn_logoff = tk.Button(self, text="logoff", command=self.onLogoff)
        self.btn_logoff.place(anchor='ne', x=largura - 5, y=5)

        ### Container com as opções de navegação disponíveis
        self.container_visual = tk.Frame(self, bg=self.cores['branco'], padx=30, pady=20)
        self.container_visual.place(anchor='center', relx=0.5, rely=0.45)

        ## Botão Cadastros
        self.btn_continuar = tk.Button(self.container_visual, text='Cadastros', bg=self.cores['principal'], fg=self.cores['branco'])
        self.btn_continuar.grid(row=0, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
    
        ## Botão Movimentações
        self.btn_continuar = tk.Button(self.container_visual, text='Movimentações', bg=self.cores['principal'], fg=self.cores['branco'])
        self.btn_continuar.grid(row=1, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
    
        ## Botão Histórico
        self.btn_continuar = tk.Button(self.container_visual, text='Histórico', bg=self.cores['principal'], fg=self.cores['branco'])
        self.btn_continuar.grid(row=2, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)
    
    def mostrar(self):
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        self.pack_forget()

    def test(self, event):
        print('Testando bind!')
    
    def onLogoff(self):
        self.gerenciador_de_janelas.alterar_para_a_tela("login")

