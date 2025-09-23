import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_interface import TelaInterface

class TelaCadastrarEscola(TelaInterface):
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

        # Nome
        self.lbl_nome = tk.Label(self.container_formulario, text="Nome da escola:", anchor='w', bg=self.cores['cinza'])
        self.lbl_nome.grid(row=1, column=0, pady=(0,0), sticky='nsw')
        self.ent_nome = tk.Entry(self.container_formulario)
        self.ent_nome.grid(row=2, column=0, columnspan=30, sticky='nsew')
        # Número de alunos
        self.lbl_numero_alunos = tk.Label(self.container_formulario, text="Número de Alunos:", anchor='w', bg=self.cores['cinza'])
        self.lbl_numero_alunos.grid(row=3, column=0, pady=(2,0), sticky='nsw')
        self.ent_numero_alunos = tk.Entry(self.container_formulario)
        self.ent_numero_alunos.grid(row=4, column=0, columnspan=4, sticky='nsew')
        
        ## Endereço

        # Logradouro
        self.lbl_logradouro = tk.Label(self.container_formulario, text="Logradouro:", anchor='w', bg=self.cores['cinza'])
        self.lbl_logradouro.grid(row=7, column=0, pady=(2,0), sticky='nsw')
        self.ent_logradouro = tk.Entry(self.container_formulario)
        self.ent_logradouro.grid(row=8, column=0, columnspan=30, sticky='nsew')
        # Bairro
        self.lbl_bairro = tk.Label(self.container_formulario, text="Bairro:", anchor='w', bg=self.cores['cinza'])
        self.lbl_bairro.grid(row=11, column=0, pady=(2,0), sticky='nsw')
        self.ent_bairro = tk.Entry(self.container_formulario)
        self.ent_bairro.grid(row=12, column=0, columnspan=26, sticky='nsew')
        # Número
        self.lbl_numero = tk.Label(self.container_formulario, text="Número:", anchor='w', bg=self.cores['cinza'])
        self.lbl_numero.grid(row=11, column=26, pady=(2,0), sticky='nsw')
        self.ent_numero = tk.Entry(self.container_formulario)
        self.ent_numero.grid(row=12, column=26, columnspan=4, sticky='nsew')
        # Estado
        self.lbl_estado = tk.Label(self.container_formulario, text="Estado:", anchor='w', bg=self.cores['cinza'])
        self.lbl_estado.grid(row=15, column=0, pady=(2,0), sticky='nsw')
        self.ent_estado = tk.Entry(self.container_formulario)
        self.ent_estado.grid(row=16, column=0, columnspan=20, sticky='nsew')
        # CEP
        self.lbl_cep = tk.Label(self.container_formulario, text="CEP:", anchor='w', bg=self.cores['cinza'])
        self.lbl_cep.grid(row=15, column=20, pady=(2,0), sticky='nsw')
        self.ent_cep = tk.Entry(self.container_formulario)
        self.ent_cep.grid(row=16, column=20, columnspan=10, sticky='nsew')

        ### Botões Confirmar e Cancelar
        self.btn_confirmar = tk.Button(self.container_formulario, text="Confirmar", bg=self.cores['verde'], command=self.onConfirmar)
        self.btn_confirmar.grid(row=20, column=0, sticky='nswe', pady=(10,0))

        self.btn_cancelar = tk.Button(self.container_formulario, text="Cancelar", bg=self.cores['vermelho'], command=self.onCancelar)
        self.btn_cancelar.grid(row=20, column=2, columnspan=10, sticky='nswe', pady=(10,0))

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

