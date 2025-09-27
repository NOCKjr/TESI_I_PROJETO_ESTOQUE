import tkinter as tk
import constants
from tkinter import ttk

from view.telas.cadastros.tela_cadastrar_escola import TelaCadastrarEscola
from view.telas.cadastros.tela_cadastrar_fornecedor import TelaCadastrarFornecedor
from view.telas.cadastros.tela_cadastrar_insumo import TelaCadastrarInsumo
from view.telas.cadastros.tela_cadastrar_usuario import TelaCadastrarUsuario
from view.telas.historico.tela_historico import TelaHistorico
from view.telas.menus.menu_navegacao import MenuNavegacao
from view.telas.movimentacoes.tela_movimentacoes import TelaMovimentacoes
from view.telas.tela_interface import TelaInterface
from view.telas.tela_login import TelaLogin
from view.telas.tela_menu_cadastros import TelaMenuCadastros
from view.telas.tela_menu_principal import TelaMenuPrincipal
from view.telas.listagem.tela_consultas import TelaConsultas
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.listagem.tela_listagem_usuarios import TelaListagemUsuarios

class App(GerenciadorDeJanelasBase):
    def __init__(self, master):
        super().__init__(master)

        # Referências das telas usadas
        self.telas: dict[str, TelaInterface] = {
            constants.TELA_LOGIN: TelaLogin(self.content_frame, self),                              # Tela de login
            constants.TELA_MENU_PRINCIPAL: TelaMenuPrincipal(self.content_frame, self),             # Tela de menu principal
            constants.TELA_MENU_CADASTROS: TelaMenuCadastros(self.content_frame, self),             # Tela de menu de cadastros
            constants.TELA_CADASTRAR_USUARIO: TelaCadastrarUsuario(self.content_frame, self),       # Tela cadsatro de usuário
            constants.TELA_CADASTRAR_ESCOLA: TelaCadastrarEscola(self.content_frame, self),         # Tela cadsatro de escola
            constants.TELA_CADASTRAR_FORNECEDOR: TelaCadastrarFornecedor(self.content_frame, self), # Tela cadsatro de fornecedor
            constants.TELA_CADASTRAR_INSUMO: TelaCadastrarInsumo(self.content_frame, self),         # Tela cadsatro de insumo
            constants.TELA_MOVIMENTACOES: TelaMovimentacoes(self.content_frame, self),              # Tela de movimentações
            constants.TELA_HISTORICO: TelaHistorico(self.content_frame, self),                      # Tela de histórico
            constants.TELA_CONSULTAS: TelaConsultas(self.content_frame, self),                      # Tela de consultas
            constants.TELA_LISTAGEM_USUARIOS: TelaListagemUsuarios(self.content_frame, self),       # Tela de listagem de usuários
            constants.TELA_EDITAR_USUARIO: TelaCadastrarUsuario(self.content_frame, self),          # Tela de editar um usuário
        }
        
        # Inicia na tela de login
        self.alterar_para_a_tela(constants.TELA_LOGIN)
        # self.alterar_para_a_tela(constants.TELA_MENU_CADASTROS)
        # self.alterar_para_a_tela(constants.TELA_CONSULTAS)
    
    def criar_barra_de_menu(self):
        # Cria a barra de menu
        self.barra_menu = tk.Menu(self.master)
        
        # Variável para indicar qual aba está selecionada (movimentações, usuários, escolas, ...)
        self.var_tela_ativa = tk.StringVar(value="")

        # Menu "Movimentações"
        self.barra_menu.add_command(label="Movimentações", command=lambda: self.alterar_para_a_tela(constants.TELA_MOVIMENTACOES))

        # Menu "Usuários"
        self.barra_menu.add_command(label='Usuários', command=lambda: self.alterar_para_a_tela(constants.TELA_LISTAGEM_USUARIOS))

        # Menu "Escolas"
        self.barra_menu.add_command(label='Escolas', command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_ESCOLA))

        # Menu "Fornecedores"
        self.barra_menu.add_command(label='Fornecedores', command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_FORNECEDOR))

        # Menu "Insumos"
        self.barra_menu.add_command(label='Insumos', command=lambda: self.alterar_para_a_tela(constants.TELA_CADASTRAR_INSUMO))

        # Adicionar o menu à janela
        
    def get_tela(self, nome_tela: str):
        if nome_tela in self.telas:
            return self.telas[nome_tela]
    
    def editar_usuario(self, usuario):
        tela_editar = self.get_tela(constants.TELA_EDITAR_USUARIO)

        if type(usuario) == list or type(usuario) == tuple:
            usuario = {
                'id': usuario[0],
                'login': usuario[1],
                'senha': usuario[2],
                'tipo': usuario[3]
            }
        # Configura o formulário para editar o usuario informado
        tela_editar.editar_usuario(usuario)

        # Abre o formulário para edição
        self.alterar_para_a_tela(constants.TELA_EDITAR_USUARIO)
    
    def atualizar_status_da_barra_de_menu(self):
        """Desativa a barra de menu caso esteja na tela de login."""

        if self.tela_atual == self.get_tela(constants.TELA_LOGIN):
            self.menu_navegacao.esconder()
        else:
            self.menu_navegacao.exibir()
        
    def alterar_para_a_tela(self, proxima_tela):
        super().alterar_para_a_tela(proxima_tela)
        self.atualizar_status_da_barra_de_menu()
