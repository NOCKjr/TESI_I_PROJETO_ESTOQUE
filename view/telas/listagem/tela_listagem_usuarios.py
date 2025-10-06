from tkinter import ttk, messagebox
import constants

from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.listagem.tela_listagem_base import TelaListagemBase
from control.usuario_controller import UsuarioController

class TelaListagemUsuarios(TelaListagemBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, tipo_entidade=constants.ENTIDADE_USUARIO, controle_entidade=UsuarioController(), cabecalho=['ID', 'LOGIN', 'EMAIL', 'TIPO'], chaves_dict=['id', 'nick', 'email', 'tipo'])
