import tkinter as tk
import ttkbootstrap as ttk
import constants

from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_interface import TelaInterface
from control.usuario_controller import UsuarioController


class TelaConsultas(TelaInterface):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')

        self.controle_usuarios = UsuarioController()

        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['branco'])
        self.lbl_sigeme.pack(side='top')

        # Botão que ativa a consulta na lista de usuários
        self.btn_usuarios = tk.Button(self, text='Usuários', command=self.listar_usuarios)
        self.btn_usuarios.pack()

    def listar_usuarios(self):
        colunas = ['ID', 'LOGIN', 'SENHA', 'TIPO']
        self.tvw_usuarios = ttk.Treeview(self, height=5, columns=colunas, show='headings')
        tuplas = self.controle_usuarios.listar_usuario()

        for coluna in colunas:
            self.tvw_usuarios.heading(coluna, text=coluna)
            self.tvw_usuarios.column(coluna, width=100, anchor="center")

        for item in tuplas:
            self.tvw_usuarios.insert('', 'end', values=item)
        self.tvw_usuarios.pack()


    def mostrar(self):
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        self.pack_forget()