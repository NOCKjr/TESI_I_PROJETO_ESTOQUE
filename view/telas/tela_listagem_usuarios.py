import tkinter as tk
from tkinter import ttk
import constants

from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_interface import TelaInterface
from control.usuario_controller import UsuarioController

class TelaListagemUsuarios(TelaInterface):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')

        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas

        # Controlador de usuários
        self.controle_usuarios = UsuarioController()

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['branco'])
        self.lbl_sigeme.pack(side='top')

        ### Voltar ao menu
        self.btn_logoff = tk.Button(self, text="Voltar", command=lambda: self.alterar_para_a_tela(constants.TELA_CONSULTAS))
        self.btn_logoff.place(anchor='ne', x=largura - 5, y=5)

        # Criar e exibir a listagem de usuários
        self.criar_listagem_usuarios()

    def criar_listagem_usuarios(self):
        colunas = ['ID', 'LOGIN', 'SENHA', 'TIPO']
        self.tvw_usuarios = ttk.Treeview(self, height=5, columns=colunas, show='headings')
        tuplas = self.controle_usuarios.listar_usuario()
        
        self.tvw_usuarios.heading('ID', text='ID')
        self.tvw_usuarios.column('ID', width=20, anchor='center')

        self.tvw_usuarios.heading('LOGIN', text='LOGIN')
        self.tvw_usuarios.column('LOGIN', width=200, anchor='center')

        self.tvw_usuarios.heading('SENHA', text='SENHA')
        self.tvw_usuarios.column('SENHA', width=200, anchor='center')

        self.tvw_usuarios.heading('TIPO', text='TIPO')
        self.tvw_usuarios.column('TIPO', width=20, anchor='center')

        for item in tuplas:
            self.tvw_usuarios.insert('', 'end', values=item)
        self.tvw_usuarios.pack(pady=17, padx=10, fill='x', expand=False)

    def mostrar(self):
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        self.pack_forget()
    
    def alterar_para_a_tela(self, tela):
        self.gerenciador_de_janelas.alterar_para_a_tela(tela)