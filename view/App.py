import ttkbootstrap as ttk
from app_context import get_context
import constants

from view.telas.cadastros.tela_cadastrar_movimentacao import TelaCadastrarMovimentacao
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase

from view.telas.listagem.tela_listagem_movimentacoes import TelaListagemMovimentacoes
from view.telas.tela_login import TelaLogin
from view.telas.tela_base import TelaBase
from view.telas.tela_menu_principal import TelaMenuPrincipal
from view.telas.tela_menu_cadastros import TelaMenuCadastros
from view.telas.cadastros.tela_formulario_base import TelaFormularioBase

from view.telas.cadastros.tela_cadastrar_escola import TelaCadastrarEscola
from view.telas.cadastros.tela_cadastrar_fornecedor import TelaCadastrarFornecedor
from view.telas.cadastros.tela_cadastrar_insumo import TelaCadastrarInsumo
from view.telas.cadastros.tela_cadastrar_usuario import TelaCadastrarUsuario

from view.telas.listagem.tela_listagem_escolas import TelaListagemEscolas
from view.telas.listagem.tela_listagem_fornecedores import TelaListagemFornecedores
from view.telas.listagem.tela_listagem_insumos import TelaListagemInsumos
from view.telas.listagem.tela_consultas import TelaConsultas
from view.telas.listagem.tela_listagem_usuarios import TelaListagemUsuarios

from view.telas.movimentacoes.tela_formulario_movimentacao import TelaFormularioMovimentacao
from view.telas.movimentacoes.tela_movimentacoes import TelaMovimentacoes

from view.telas.historico.tela_historico import TelaHistorico
from view.telas.menus.menu_navegacao import MenuNavegacao

class App(GerenciadorDeJanelasBase):
    def __init__(self, master):
        super().__init__(master)

        # Referências das telas usadas
        self.telas: dict[str, TelaBase] = {
            constants.TELA_LOGIN:                   TelaLogin(self.content_frame, self),                # Tela de login
            constants.TELA_MENU_PRINCIPAL:          TelaMenuPrincipal(self.content_frame, self),        # Tela de menu principal
            constants.TELA_MENU_CADASTROS:          TelaMenuCadastros(self.content_frame, self),        # Tela de menu de cadastros
            constants.TELA_CADASTRAR_USUARIO:       TelaCadastrarUsuario(self.content_frame, self),     # Tela cadsatro de usuário
            constants.TELA_CADASTRAR_ESCOLA:        TelaCadastrarEscola(self.content_frame, self),      # Tela cadsatro de escola
            constants.TELA_CADASTRAR_FORNECEDOR:    TelaCadastrarFornecedor(self.content_frame, self),  # Tela cadsatro de fornecedor
            constants.TELA_CADASTRAR_INSUMO:        TelaCadastrarInsumo(self.content_frame, self),      # Tela cadsatro de insumo
            constants.TELA_CADASTRAR_MOVIMENTACAO:  TelaCadastrarMovimentacao(self.content_frame, self),        # Tela de inserir movimentações
            constants.TELA_MOVIMENTACOES:           TelaMovimentacoes(self.content_frame, self),        # Tela de movimentações
            constants.TELA_HISTORICO:               TelaHistorico(self.content_frame, self),            # Tela de histórico
            constants.TELA_CONSULTAS:               TelaConsultas(self.content_frame, self),            # Tela de consultas
            constants.TELA_LISTAGEM_USUARIOS:       TelaListagemUsuarios(self.content_frame, self),     # Tela de listagem de usuários
            constants.TELA_LISTAGEM_ESCOLAS:        TelaListagemEscolas(self.content_frame, self),      # Tela de listagem de escolas
            constants.TELA_LISTAGEM_FORNECEDORES:   TelaListagemFornecedores(self.content_frame, self), # Tela de listagem de fornecedores
            constants.TELA_LISTAGEM_INSUMOS:        TelaListagemInsumos(self.content_frame, self),      # Tela de listagem de insumos
            constants.TELA_LISTAGEM_MOVIMENTACOES:  TelaListagemMovimentacoes(self.content_frame, self),      # Tela de listagem de insumos
            constants.TELA_EDITAR_USUARIO:          TelaCadastrarUsuario(self.content_frame, self),     # Tela de editar um usuário
            constants.TELA_EDITAR_ESCOLA:           TelaCadastrarEscola(self.content_frame, self),      # Tela de editar uma escola
            constants.TELA_EDITAR_FORNECEDOR:       TelaCadastrarFornecedor(self.content_frame, self),  # Tela de editar um fornecedor
            constants.TELA_EDITAR_INSUMO:           TelaCadastrarInsumo(self.content_frame, self),      # Tela de editar um insumo
            constants.TELA_EDITAR_MOVIMENTACAO:     TelaCadastrarMovimentacao(self.content_frame, self),      # Tela de editar um insumo
            constants.TELA_DETALHAR_MOVIMENTACAO:   TelaCadastrarMovimentacao(self.content_frame, self),      # Tela de editar um insumo
        }

        # Escala inicial
        self.escala = get_context().escala
        self.aplicar_escala()

        # Bind dos atalhos
        self.bind_all("<Control-plus>", self.aumentar_escala)
        self.bind_all("<Control-minus>", self.diminuir_escala)
        self.bind_all("<Control-equal>", self.aumentar_escala)
        
        # Inicia na tela de login
        self.alterar_para_a_tela(constants.TELA_LOGIN)
        # self.alterar_para_a_tela(constants.TELA_MENU_PRINCIPAL)
        # self.alterar_para_a_tela(constants.TELA_CADASTRAR_MOVIMENTACAO)
        # self.alterar_para_a_tela(constants.TELA_CADASTRAR_USUARIO)
        # self.alterar_para_a_tela(constants.TELA_CADASTRAR_INSUMO)
        # self.alterar_para_a_tela(constants.TELA_MENU_CADASTROS)
        # self.alterar_para_a_tela(constants.TELA_CONSULTAS)

    def aplicar_escala(self):
        """Aplica o fator de escala atual à interface."""
        get_context().atualizar_fonte(self.escala)

        style = ttk.Style()

        # --- Logo ---
        style.configure('Logo.TLabel', font=('Arial', max(int(20 * self.escala), 1), 'bold'))
        style.configure('.', font=('Arial', max(int(12 * self.escala), 1)))

        # --- Treeview ---
        base_rowheight = 20
        nova_altura = int(base_rowheight * self.escala)
        self._atualizar_treeviews_em_todas_as_telas(nova_altura)

        # Atualiza widgets Entry, Label, Combobox etc em todas as telas
        for tela in self.telas.values():
            if hasattr(tela, 'atualizar_fonte_widgets'):
                tela.atualizar_fonte_widgets(self.escala)


    def aumentar_escala(self, event=None):
        self.escala = min(round(self.escala + 0.1, 1), 1.5)
        get_context().atualizar_fonte(self.escala)
        self.aplicar_escala()

    def diminuir_escala(self, event=None):
        self.escala = max(round(self.escala - 0.1, 1), 0.75)
        get_context().atualizar_fonte(self.escala)
        self.aplicar_escala()
    
    def _atualizar_treeviews_em_todas_as_telas(self, nova_altura: int):
        """Chama o método de ajuste em cada tela registrada."""
        for tela in self.telas.values():
            if hasattr(tela, "atualizar_altura_treeviews"):
                tela.atualizar_altura_treeviews(nova_altura)

    def get_tela(self, nome_tela: str):
        """Retorna a instância da tela com o nome fornecido"""
        if nome_tela in self.telas:
            return self.telas[nome_tela]
    
    def editar(self, item, tipo_entidade):
        """Abre a tela de edição para o `item` do `tipo_de_entidade` fornecido"""
        match tipo_entidade:
            case constants.ENTIDADE_USUARIO:
                self.editar_usuario(item)
            case constants.ENTIDADE_ESCOLA:
                self.editar_escola(item)
            case constants.ENTIDADE_FORNECEDOR:
                self.editar_fornecedor(item)
            case constants.ENTIDADE_INSUMO:
                self.editar_insumo(item)
            case constants.ENTIDADE_MOVIMENTACAO:
                self.editar_movimentacao(item)
            case _:
                pass
    
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
    
    def editar_movimentacao(self, movimentacao):
        tela_editar = self.get_tela(constants.TELA_EDITAR_MOVIMENTACAO)

        # Configura o formulário para editar a movimentacao informada
        tela_editar.editar_movimentacao(movimentacao)

        # Abre o formulário para edição
        self.alterar_para_a_tela(constants.TELA_EDITAR_MOVIMENTACAO)
    
    def editar_escola(self, escola):
        tela_editar = self.get_tela(constants.TELA_EDITAR_ESCOLA)
        
        # Configura o formulário para editar o escola informado
        tela_editar.editar_escola(escola)

        # Abre o formulário para edição
        self.alterar_para_a_tela(constants.TELA_EDITAR_ESCOLA)
    
    def editar_fornecedor(self, fornecedor):
        tela_editar = self.get_tela(constants.TELA_EDITAR_FORNECEDOR)

        if type(fornecedor) == list or type(fornecedor) == tuple:
            fornecedor = {
                'id': fornecedor[0],
                'razao-social': fornecedor[1],
                'contato': fornecedor[2],
            }
        # Configura o formulário para editar o fornecedor informado
        tela_editar.editar_fornecedor(fornecedor)

        # Abre o formulário para edição
        self.alterar_para_a_tela(constants.TELA_EDITAR_FORNECEDOR)
    
    def editar_insumo(self, insumo):
        tela_editar = self.get_tela(constants.TELA_EDITAR_INSUMO)

        if type(insumo) == list or type(insumo) == tuple:
            insumo = {
                'id': insumo[0],
                'nome': insumo[1],
                'media-consumo': insumo[2],
                'estoque': insumo[3],
                'medida': insumo[4]
            }
        # Configura o formulário para editar o insumo informado
        tela_editar.editar_insumo(insumo)

        # Abre o formulário para edição
        self.alterar_para_a_tela(constants.TELA_EDITAR_INSUMO)
    
    def detalhar_movimentacao(self, movimentacao_id):
        tela_detalhar = self.get_tela(constants.TELA_DETALHAR_MOVIMENTACAO)

        # Preenche os campos da tela
        tela_detalhar.detalhar(movimentacao_id)

        # Mostra a tela detalhada
        self.alterar_para_a_tela(constants.TELA_DETALHAR_MOVIMENTACAO)
    
    def atualizar_status_da_barra_de_menu(self):
        """Desativa a barra de menu caso esteja na tela de login."""

        if self.tela_atual == self.get_tela(constants.TELA_LOGIN):
            self.menu_navegacao.esconder()
        else:
            self.menu_navegacao.exibir()
        
    def alterar_para_a_tela(self, proxima_tela):
        super().alterar_para_a_tela(proxima_tela)
        self.atualizar_status_da_barra_de_menu()
