import ttkbootstrap as ttk
import constants
from control.escola_controller import EscolaController
from control.fornecedor_controller import FornecedorController
import utils

from control.movimentacao_controller import MovimentacaoController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.cadastros.tela_formulario_base import TelaFormularioBase


class TelaCadastrarMovimentacao(TelaFormularioBase):
    def __init__(self, master,
                       gerenciador_de_janelas: GerenciadorDeJanelasBase,
                       modo_editar=False,
                       largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master,
                         gerenciador_de_janelas,
                         constants.ENTIDADE_MOVIMENTACAO,
                         MovimentacaoController(),
                         modo_editar,
                         largura, altura)

        # Controladores
        self.controle_fornecedores = FornecedorController()
        self.controle_escolas = EscolaController()

        # Dicionários de associação nome → id
        self.map_fornecedor = {}
        self.map_escola = {}

        # Listas de nomes exibidos nos comboboxes
        self.lista_fornecedores = []
        self.lista_escolas = []

        self.criar_campos_formulario()
        self._atualizar_listas()
        self._configurar_eventos()
        self._ocultar_campos_iniciais()


    def criar_campos_formulario(self):
        super().criar_campos_formulario()

        # Tipo de movimentação (Entrada ou Saída)
        self.lbl_tipo_movimentacao = ttk.Label(self.container_formulario, text="Tipo de movimentação:", anchor='w')
        self.lbl_tipo_movimentacao.grid(row=2, column=0, pady=(10, 0), sticky='nsw')

        self.cmb_tipo_movimentacao = ttk.Combobox(
            self.container_formulario,
            values=["Entrada", "Saída"],
            state="readonly"
        )
        self.cmb_tipo_movimentacao.grid(row=3, column=0, columnspan=14, sticky='nsew')

        # Data
        self.lbl_data = ttk.Label(self.container_formulario, text="Data:", anchor='w')
        self.lbl_data.grid(row=2, column=20, pady=(10, 0), sticky='nsw')
        self.ent_data = utils.DateEntry(self.container_formulario)
        self.ent_data.grid(row=3, column=20, columnspan=10, sticky='nsew')

        # # Responsável
        # self.lbl_responsavel = ttk.Label(self.container_formulario, text="Responsável:", anchor='w')
        # self.lbl_responsavel.grid(row=8, column=0, pady=(10, 0), sticky='nsw')
        # self.ent_responsavel = ttk.Entry(self.container_formulario)
        # self.ent_responsavel.grid(row=9, column=0, columnspan=14, sticky='nsew')

        # Fornecedor
        self.lbl_fornecedor = ttk.Label(self.container_formulario, text="Fornecedor:", anchor='w')
        self.lbl_fornecedor.grid(row=10, column=0, pady=(10, 0), sticky='nsw')
        self.cmb_fornecedor = ttk.Combobox(
            self.container_formulario,
            values=self.lista_fornecedores,
            state="readonly"
        )
        self.cmb_fornecedor.grid(row=11, column=0, columnspan=14, sticky='nsew')

        # Escola
        self.lbl_escola = ttk.Label(self.container_formulario, text="Escola:", anchor='w')
        self.lbl_escola.grid(row=12, column=0, pady=(10, 0), sticky='nsw')
        self.cmb_escola = ttk.Combobox(
            self.container_formulario,
            values=self.lista_escolas,
            state="readonly"
        )
        self.cmb_escola.grid(row=13, column=0, columnspan=14, sticky='nsew')


    def _configurar_eventos(self):
        """Associa eventos aos campos"""
        self.cmb_tipo_movimentacao.bind("<<ComboboxSelected>>", self._ao_selecionar_tipo)


    def _ocultar_campos_iniciais(self):
        """Esconde todos os campos exceto Tipo e Data"""
        widgets_ocultos = [
            # self.lbl_responsavel, self.ent_responsavel,
            self.lbl_fornecedor, self.cmb_fornecedor,
            self.lbl_escola, self.cmb_escola
        ]
        for w in widgets_ocultos:
            w.grid_remove()


    def _ao_selecionar_tipo(self, event=None):
        """Mostra os campos corretos dependendo do tipo"""
        tipo = self.cmb_tipo_movimentacao.get()

        # Esconde tudo antes
        self._ocultar_campos_iniciais()

        # # Mostra "Responsável" sempre
        # self.lbl_responsavel.grid()
        # self.ent_responsavel.grid()

        if tipo == "Entrada":
            self.lbl_fornecedor.grid()
            self.cmb_fornecedor.grid()
        elif tipo == "Saída":
            self.lbl_escola.grid()
            self.cmb_escola.grid()


    def _atualizar_listas(self):
        """Atualiza as listas de fornecedores e escolas"""
        # Fornecedores
        resp_f = self.controle_fornecedores.listar()
        tuplas_f = resp_f.retorno if resp_f.ok() else []

        self.map_fornecedor = {f["razao_social"]: f["id"] for f in tuplas_f}
        self.lista_fornecedores = list(self.map_fornecedor.keys())
        self.cmb_fornecedor["values"] = self.lista_fornecedores

        # Escolas
        resp_e = self.controle_escolas.listar()
        tuplas_e = resp_e.retorno if resp_e.ok() else []

        self.map_escola = {e["nome"]: e["id"] for e in tuplas_e}
        self.lista_escolas = list(self.map_escola.keys())
        self.cmb_escola["values"] = self.lista_escolas


    def obter_valores_campos_formulario(self):
        """Captura os valores dos campos"""
        data = self.ent_data.get_date()
        tipo = self.cmb_tipo_movimentacao.get()[0] if self.cmb_tipo_movimentacao.get() else ""
        # responsavel_id = self.ent_responsavel.get()
        responsavel_id = None # <- alterar para pegar o id do usuário que está logado

        fornecedor_id = None
        escola_id = None

        if tipo == "E":  # Entrada
            nome_forn = self.cmb_fornecedor.get()
            fornecedor_id = self.map_fornecedor.get(nome_forn)
        elif tipo == "S":  # Saída
            nome_escola = self.cmb_escola.get()
            escola_id = self.map_escola.get(nome_escola)

        return (data, tipo, responsavel_id, fornecedor_id, escola_id)
