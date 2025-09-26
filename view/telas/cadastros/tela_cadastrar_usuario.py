import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_interface import TelaInterface
from control.usuario_controller import UsuarioController

class TelaCadastrarUsuario(TelaInterface):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')

        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas

        # Controlador de usuários
        self.controle_usuarios = UsuarioController()

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['branco'])
        self.lbl_sigeme.pack(side='top')

        ### Voltar ao menu
        self.btn_logoff = tk.Button(self, text="Voltar", command=lambda: self.alterar_para_a_tela(constants.TELA_MENU_CADASTROS))
        self.btn_logoff.place(anchor='ne', x=largura - 5, y=5)

        ### Container com o formulário de cadastro
        self.container_formulario = tk.Frame(self, bg=self.cores['cinza'], padx=10, pady=10)
        self.container_formulario.place(anchor='center', relx=0.5, rely=0.5)

        # # Nome completo
        # self.lbl_nome_completo = tk.Label(self.container_formulario, text="Nome completo:", anchor='w', bg=self.cores['cinza'])
        # self.lbl_nome_completo.grid(row=1, column=0, pady=(0,0), sticky='nsw')
        # self.ent_nome_completo = tk.Entry(self.container_formulario)
        # self.ent_nome_completo.grid(row=2, column=0, columnspan=30, sticky='nsew')

        # # CPF
        # self.lbl_cpf = tk.Label(self.container_formulario, text="CPF:", anchor='w', bg=self.cores['cinza'])
        # self.lbl_cpf.grid(row=3, column=0, pady=(2,0), sticky='nsw')
        # self.ent_cpf = tk.Entry(self.container_formulario)
        # self.ent_cpf.grid(row=4, column=0, columnspan=14, sticky='nsew')

        # # Nº de registro
        # self.lbl_numero_registro = tk.Label(self.container_formulario, text="Nº registro:", anchor='w', bg=self.cores['cinza'])
        # self.lbl_numero_registro.grid(row=3, column=15, pady=(2,0), sticky='nsw')
        # self.ent_numero_registro = tk.Entry(self.container_formulario)
        # self.ent_numero_registro.grid(row=4, column=15, columnspan=15, sticky='nsew')

        # Login do usuário
        self.lbl_login_usuario = tk.Label(self.container_formulario, text="Login usuário:", anchor='w', bg=self.cores['cinza'])
        self.lbl_login_usuario.grid(row=0, column=0, pady=(2,0), sticky='nsw')
        self.ent_login_usuario = tk.Entry(self.container_formulario)
        self.ent_login_usuario.grid(row=1, column=0, columnspan=14, sticky='nsew')

        # Senha do usuário
        self.lbl_senha_usuario = tk.Label(self.container_formulario, text="Senha usuário:", anchor='w', bg=self.cores['cinza'])
        self.lbl_senha_usuario.grid(row=0, column=15, pady=(2,0), sticky='nsw')
        self.ent_senha_usuario = tk.Entry(self.container_formulario, show='*')
        self.ent_senha_usuario.grid(row=1, column=15, columnspan=14, sticky='nsew')

        # Tipo de usuário (Administrador ou Comum)
        self.lbl_tipo_usuario = tk.Label(self.container_formulario, text="Tipo de usuário:", anchor='w', bg=self.cores['cinza'])
        self.lbl_tipo_usuario.grid(row=2, column=0, pady=(10,0), sticky='nsw')
        self.cmb_tipo_usuario = ttk.Combobox(self.container_formulario, values=["Comum", "Administrador"], state="readonly")
        self.cmb_tipo_usuario.grid(row=3, column=0, columnspan=14, sticky='nsew')
        self.cmb_tipo_usuario.set("Comum")  # Valor padrão

        ### Botões Confirmar e Cancelar
        self.btn_confirmar = tk.Button(self.container_formulario, text="Confirmar", bg=self.cores['verde'], command=self.onConfirmar)
        self.btn_confirmar.grid(row=8, column=0, sticky='nswe', pady=(10,0))

        self.btn_cancelar = tk.Button(self.container_formulario, text="Cancelar", bg=self.cores['vermelho'], command=self.onCancelar)
        self.btn_cancelar.grid(row=8, column=2, columnspan=10, sticky='nswe', pady=(10,0))

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
    
    def limpar_campos(self):
        self.ent_login_usuario.delete(0, 'end')
        self.ent_senha_usuario.delete(0, 'end')
        self.cmb_tipo_usuario.current(0)
    
    def onConfirmar(self):
        # Captura os valores dos campos
        login = self.ent_login_usuario.get()
        senha = self.ent_senha_usuario.get()
        tipo_usuario = self.cmb_tipo_usuario.get()
        
        # Converte o tipo de usuário para o código esperado pelo banco
        tipo_codigo = 'A' if tipo_usuario == "Administrador" else 'C'
        
        # Chama o controller para inserir o usuário
        self.controle_usuarios.inserir_usuario(login, senha, tipo_codigo)
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()
        
        # Volta para o menu de cadastros
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MENU_CADASTROS)

    def onCancelar(self):
        # Reseta os valores dos campos do formulário
        self.limpar_campos()
        
        # Volta para o menu de cadastros
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MENU_CADASTROS)


