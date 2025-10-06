import constants

import ttkbootstrap as ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_base import TelaBase

class TelaConsultas(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        ### Container com as opções de consultas disponíveis
        self.container_visual = ttk.Frame(self, padding=(30, 20), bootstyle="info")
        self.container_visual.place(anchor='center', relx=0.5, rely=0.45)

        # Botão que ativa a consulta na lista de usuários
        self.btn_usuarios = ttk.Button(self.container_visual, text='Usuários', bootstyle="primary", command=self.listar_usuarios)
        self.btn_usuarios.grid(row=0, column=0, columnspan=1, sticky='nswe', padx=2, pady=2)

    def listar_usuarios(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_USUARIOS)
