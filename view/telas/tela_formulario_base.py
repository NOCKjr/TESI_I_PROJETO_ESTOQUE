import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_base import TelaBase

class TelaFormularioBase(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        self.numero_colunas_formulario = 30
        
        ### Container com o formulário de cadastro
        self.container_formulario = tk.Frame(self, bg=constants.cores['cinza'], padx=10, pady=10)
        self.container_formulario.place(anchor='center', relx=0.5, rely=0.5)

        # /--- Inserir campos do formulário aqui ---/

        ### Botões Confirmar e Cancelar
        self.btn_confirmar = tk.Button(self.container_formulario, text="Confirmar", bg=constants.cores['verde'], command=self.onConfirmar)
        self.btn_confirmar.grid(row=60, column=0, sticky='nswe', pady=(10,0))

        self.btn_cancelar = tk.Button(self.container_formulario, text="Cancelar", bg=constants.cores['vermelho'], command=self.onCancelar)
        self.btn_cancelar.grid(row=60, column=2, columnspan=10, sticky='nswe', pady=(10,0))

        for c in range(self.numero_colunas_formulario):
            self.container_formulario.columnconfigure(c, minsize=10)
    
    def onConfirmar(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MENU_CADASTROS)

    def onCancelar(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MENU_CADASTROS)

