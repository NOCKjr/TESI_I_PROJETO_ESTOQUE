from tkinter import ttk, messagebox
import constants

from control.escola_controller import EscolaController
from control.fornecedor_controller import FornecedorController
from control.movimentacao_controller import MovimentacaoController
from control.usuario_controller import UsuarioController
from view.telas.cadastros.tela_cadastrar_movimentacao import TelaCadastrarMovimentacao
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase

class TelaDetalharMovimentacao(TelaCadastrarMovimentacao):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, 
                         gerenciador_de_janelas)
        
        self.is_detalhado = True
    
    def aplicar_modo_detalhamento(self):
        """Se is_detalhando estiver ativo, desativa campos e botões."""
        if not self.is_detalhando:
            return

        # Desativa comboboxes e entradas
        campos = [
            self.cmb_tipo_movimentacao,
            self.ent_data,
            self.cmb_fornecedor,
            self.cmb_escola,
        ]
        for campo in campos:
            campo.configure(state='disabled')

        # Bloqueia interação na Treeview
        self.tvw_itens.configure(selectmode="none")
        # Alternativamente, bind de evento para impedir edição
        self.tvw_itens.unbind("<Double-1>")

        # Desativa botões de inserção/remoção
        self.btn_adicionar_item.pack_forget()
        self.btn_remover_item.pack_forget()

        # Desativa botões de confirmar/cancelar
        self.btn_confirmar.pack_forget()
        self.btn_cancelar.pack_forget()
    
    def desaplicar_modo_detalhamento(self):
        # Reativa botões de inserção/remoção
        self.btn_adicionar_item.pack(side='left', padx=5)
        self.btn_remover_item.pack(side='left', padx=5)

