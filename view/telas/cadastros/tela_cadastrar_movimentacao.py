from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as ttk
from app_context import get_context
import constants
from control.item_controller import ItemController
import utils
from control.escola_controller import EscolaController
from control.fornecedor_controller import FornecedorController
from control.insumo_controller import InsumoController

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
        self.controle_insumos = InsumoController()
        self.controle_itens = ItemController()

        # Dicionários de associação nome → id
        self.map_fornecedor = {}
        self.map_escola = {}
        self.map_insumo = {}

        # Listas de nomes exibidos nos comboboxes
        self.lista_fornecedores = []
        self.lista_escolas = []
        self.lista_insumos = []

        # Lista interna para armazenar os itens movimentados
        self.itens: list[dict] = []

        self.criar_campos_formulario()
        self._atualizar_listas()
        self._configurar_eventos()
        self._ocultar_campos_iniciais()

    def mostrar(self):
        self._atualizar_listas()
        super().mostrar()

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

        # --- Itens da movimentação ---
        self.lbl_itens = ttk.Label(self.container_formulario, text="Itens da movimentação:", anchor='w')
        self.lbl_itens.grid(row=14, column=0, pady=(10, 0), sticky='nsw')

        # Treeview de itens
        self.tvw_itens = ttk.Treeview(
            self.container_formulario,
            columns=("insumo", "quantidade"),
            show="headings",
            height=6
        )
        self.tvw_itens.heading("insumo", text="Insumo")
        self.tvw_itens.heading("quantidade", text="Quantidade")
        self.tvw_itens.grid(row=15, column=0, columnspan=24, sticky='nsew')

        # Botões
        frm_botoes = ttk.Frame(self.container_formulario)
        frm_botoes.grid(row=16, column=0, columnspan=24, pady=5, sticky='w')

        ttk.Button(frm_botoes, text="Adicionar item", command=self._abrir_janela_item).pack(side='left', padx=5)
        ttk.Button(frm_botoes, text="Remover item", command=self._remover_item).pack(side='left', padx=5)

    def _configurar_eventos(self):
        """Associa eventos aos campos"""
        self.cmb_tipo_movimentacao.bind("<<ComboboxSelected>>", self._ao_selecionar_tipo)

    def _abrir_janela_item(self):
        """Abre uma janelinha para escolher o insumo e quantidade"""
        janela = ttk.Toplevel(self)
        janela.title("Adicionar item")
        # janela.geometry("300x150")

        def impede_interacao(): 
            janela.update_idletasks() # Garante que a janela seja desenhada
            janela.grab_set() # Bloqueia interações com outras janelas
            janela.focus_set()
        
        impede_interacao()

        ttk.Label(janela, text="Insumo:").pack(pady=5)
        cmb_insumo = ttk.Combobox(
            janela, 
            values=self.lista_insumos,
            state="readonly"
        )
        cmb_insumo.pack(fill='x', padx=10)

        ttk.Label(janela, text="Quantidade:").pack(pady=5)
        ent_qtd = ttk.Entry(janela)
        ent_qtd.pack(fill='x', padx=10)

        def confirmar():
            insumo = cmb_insumo.get()
            qtd = ent_qtd.get()

            if not insumo or not qtd:
                Messagebox.show_error(title="Campos vazios!", message="Preencha todos os campos.")
                return

            item_id = None
            insumo_id = self.map_insumo[insumo]
            mov_id = None
            item = self.controle_itens.to_dict((item_id, qtd, insumo_id, mov_id))
            
            self.itens.append(item)
            self.tvw_itens.insert("", "end", values=(insumo, qtd))
            janela.destroy()

        ttk.Button(janela, text="Adicionar", command=confirmar).pack(pady=10)


    def _remover_item(self):
        """Remove o item selecionado da lista e da Treeview"""
        sel = self.tvw_itens.selection()
        if not sel:
            return
        for i in sel:
            valores = self.tvw_itens.item(i, "values")
            self.itens = [x for x in self.itens if (x["insumo"], x["quantidade"]) != tuple(valores)]
            self.tvw_itens.delete(i)


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

        # Insumos
        resp_i = self.controle_insumos.listar()
        tuplas_i = resp_i.retorno if resp_i.ok() else []

        self.map_insumo = {e["nome"]: e["id"] for e in tuplas_i}
        self.lista_insumos = list(self.map_insumo.keys())

    def obter_valores_campos_formulario(self):
        """Captura os valores dos campos"""
        data = self.ent_data.get_date()
        tipo = self.cmb_tipo_movimentacao.get()[0] if self.cmb_tipo_movimentacao.get() else ""
        usuario = get_context().usuario_logado
        responsavel_id = usuario['id'] if usuario else None

        fornecedor_id = None
        escola_id = None

        if tipo == "E":  # Entrada
            nome_forn = self.cmb_fornecedor.get()
            fornecedor_id = self.map_fornecedor.get(nome_forn)
        elif tipo == "S":  # Saída
            nome_escola = self.cmb_escola.get()
            escola_id = self.map_escola.get(nome_escola)

        return (data, tipo, responsavel_id, fornecedor_id, escola_id, self.itens)
    
    def onConfirmar(self):
        campos = self.obter_valores_campos_formulario()

        data, tipo, responsavel_id, fornecedor_id, escola_id, itens = campos

        # Validação dos campos 
        if not tipo:
            Messagebox.show_error("Por favor, selecione o tipo de movimentação.")
            self.cmb_tipo_movimentacao.focus()
            return

        if not data:
            Messagebox.show_error("Por favor, informe a data da movimentação.", "Erro")
            self.ent_data.focus()
            return

        if tipo == "E" and not fornecedor_id:
            Messagebox.show_error("Por favor, selecione o fornecedor.", "Erro")
            self.cmb_fornecedor.focus()
            return

        if tipo == "S" and not escola_id:
            Messagebox.show_error("Por favor, selecione a escola.", "Erro")
            self.cmb_escola.focus()
            return

        if not itens or len(itens) == 0:
            Messagebox.show_error("Adicione ao menos um item à movimentação.", "Erro")
            return

        # --- continua
        
        itens = campos[-1]
        campos = campos[:-1]
        
        if self.flag_editar:
            campos = (self.id_para_edicao,) + campos
            self.controle.atualizar(*campos)

            # Atualizar os itens
            for item in itens:
                self.controle_itens.atualizar(item['id'], item['quantidade'], item['insumo_id'], self.id_para_edicao)
        else:
            resp = self.controle.inserir(*campos)
            if resp.ok():
                mov_id = resp.retorno
                # Inserir os itens
                for item in itens:
                    self.controle_itens.inserir(item['quantidade'], item['insumo_id'], mov_id)
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()
        
        # Volta para a tela de listagem
        self.ir_para_tela_de_listagem()

    def limpar_campos(self):
        """Limpa todos os campos do formulário e zera a lista de itens"""
        super().limpar_campos()

        # Deseleciona comboboxes
        self.cmb_tipo_movimentacao.set("")
        self.cmb_fornecedor.set("")
        self.cmb_escola.set("")

        # Limpa a lista interna de itens
        self.itens.clear()

        # Limpa a TreeView de itens
        for item in self.tvw_itens.get_children():
            self.tvw_itens.delete(item)

        # Esconde campos condicionais (fornecedor/escola)
        self._ocultar_campos_iniciais()

