import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_interface import TelaInterface

class TelaCadastrarUsuario(TelaInterface):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')

        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['branco'])
        self.lbl_sigeme.pack(side='top')

        ### Voltar ao menu
        self.btn_logoff = tk.Button(self, text="Voltar", command=lambda: self.alterar_para_a_tela(constants.TELA_MENU_CADASTROS))
        self.btn_logoff.place(anchor='ne', x=largura - 5, y=5)

        ### Container com o formulário de cadastro
        self.container_formulario = tk.Frame(self, bg=self.cores['cinza'], padx=10, pady=10)
        self.container_formulario.place(anchor='center', relx=0.5, rely=0.5)

        # Nome completo
        self.lbl_nome_completo = tk.Label(self.container_formulario, text="Nome completo:", anchor='w', bg=self.cores['cinza'])
        self.lbl_nome_completo.grid(row=1, column=0, pady=(0,0), sticky='nsw')
        self.ent_nome_completo = tk.Entry(self.container_formulario)
        self.ent_nome_completo.grid(row=2, column=0, columnspan=30, sticky='nsew')
        # CPF
        self.lbl_cpf = tk.Label(self.container_formulario, text="CPF:", anchor='w', bg=self.cores['cinza'])
        self.lbl_cpf.grid(row=3, column=0, pady=(2,0), sticky='nsw')
        self.ent_cpf = tk.Entry(self.container_formulario)
        self.ent_cpf.grid(row=4, column=0, columnspan=14, sticky='nsew')
        # Nº de registro
        self.lbl_numero_registro = tk.Label(self.container_formulario, text="Nº registro:", anchor='w', bg=self.cores['cinza'])
        self.lbl_numero_registro.grid(row=3, column=15, pady=(2,0), sticky='nsw')
        self.ent_numero_registro = tk.Entry(self.container_formulario)
        self.ent_numero_registro.grid(row=4, column=15, columnspan=15, sticky='nsew')
        # Login do usuário
        self.lbl_login_usuario = tk.Label(self.container_formulario, text="Login usuário:", anchor='w', bg=self.cores['cinza'])
        self.lbl_login_usuario.grid(row=5, column=0, pady=(2,0), sticky='nsw')
        self.ent_login_usuario = tk.Entry(self.container_formulario)
        self.ent_login_usuario.grid(row=6, column=0, columnspan=14, sticky='nsew')

        ### Botões Confirmar e Cancelar
        self.btn_confirmar = tk.Button(self.container_formulario, text="Confirmar", bg=self.cores['verde'], command=self.onConfirmar)
        self.btn_confirmar.grid(row=7, column=0, sticky='nswe', pady=(10,0))

        self.btn_cancelar = tk.Button(self.container_formulario, text="Cancelar", bg=self.cores['vermelho'], command=self.onCancelar)
        self.btn_cancelar.grid(row=7, column=2, columnspan=10, sticky='nswe', pady=(10,0))

        for c in range(30):
            self.container_formulario.columnconfigure(c, minsize=10)


    
    def mostrar(self):
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        self.pack_forget()

    def test(self, event):
        print('Testando bind!')
    
    def alterar_para_a_tela(self, proxima_tela):
        self.gerenciador_de_janelas.alterar_para_a_tela(proxima_tela)
    
    def onConfirmar(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MENU_CADASTROS)

    def onCancelar(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MENU_CADASTROS)


