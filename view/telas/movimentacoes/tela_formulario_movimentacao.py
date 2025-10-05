import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.cadastros.tela_formulario_base import TelaFormularioBase

class MovimentacaoController:
    def __init__(self):
        pass

class TelaFormularioMovimentacao(TelaFormularioBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        # Id da movimentacao quando no modo editar
        self.id_escola_editado = None

        # Controlador de escolas
        self.controle_movimentacoes = MovimentacaoController()

        # Tipo de movimentação (Entrada ou Saída)
        self.lbl_tipo_movimentacao = tk.Label(self.container_formulario, text="Tipo de movimentação:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_tipo_movimentacao.grid(row=2, column=0, pady=(10,0), sticky='nsw')
        self.cmb_tipo_movimentacao = ttk.Combobox(self.container_formulario, values=["Saída", "Entrada"], state="readonly")
        self.cmb_tipo_movimentacao.grid(row=3, column=0, columnspan=14, sticky='nsew')
        self.cmb_tipo_movimentacao.set("")
    
    def onConfirmar(self):
        self.limpar_campos()
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MOVIMENTACOES)

    def onCancelar(self):
        self.limpar_campos()
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MOVIMENTACOES)

    def limpar_campos(self):
        self.cmb_tipo_movimentacao.set("")