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

        # Botão que ativa a consulta na lista de usuários
        self.btn_usuarios = tk.Button(self, text='Usuários', command=self.listar_usuarios)
        self.btn_usuarios.pack()

    def listar_usuarios(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_USUARIOS)


    def mostrar(self):
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        self.pack_forget()