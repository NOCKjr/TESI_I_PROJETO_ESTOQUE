import tkinter as tk
import constants

from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_interface import TelaInterface

class TelaConsultas(TelaInterface):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')

        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['branco'])
        self.lbl_sigeme.pack(side='top')

        ### Voltar ao menu
        self.btn_logoff = tk.Button(self, text="Voltar", command=lambda: self.alterar_para_a_tela(constants.TELA_MENU_PRINCIPAL))
        self.btn_logoff.place(anchor='ne', x=largura - 5, y=5)

        ### Container com as opções de consultas disponíveis
        self.container_visual = tk.Frame(self, bg=self.cores['branco'], padx=30, pady=20)
        self.container_visual.place(anchor='center', relx=0.5, rely=0.45)

        # Botão que ativa a consulta na lista de usuários
        self.btn_continuar = tk.Button(self.container_visual, text='Usuários', bg=self.cores['principal'], fg=self.cores['branco'], command=self.listar_usuarios)
        self.btn_continuar.grid(row=0, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)


    def listar_usuarios(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_USUARIOS)

    def alterar_para_a_tela(self, tela):
        self.gerenciador_de_janelas.alterar_para_a_tela(tela)


    def mostrar(self):
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        self.pack_forget()