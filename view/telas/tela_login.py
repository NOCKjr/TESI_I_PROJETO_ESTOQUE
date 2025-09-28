import tkinter as tk
import constants

from tkinter import ttk
from view.telas.tela_base import TelaBase
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from control.usuario_controller import UsuarioController

class TelaLogin(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        # Controlador de usuários
        self.controle_usuarios = UsuarioController()

        ### Container com o título da aplicação e' os campos de login
        self.container_visual = tk.Frame(self, bg=constants.cores['branco'], padx=30, pady=20)
        self.container_visual.place(anchor='center', relx=0.5, rely=0.45)

        ### Logo
        self.lbl_sigeme = tk.Label(self.container_visual, text='SIGEME', bg=constants.cores['secundario'])
        self.lbl_sigeme.grid(row=0, column=1, sticky='nswe', pady=10)

        ## Modal com os campos de login
        self.modal_login = tk.Frame(self.container_visual, bg=constants.cores['cinza'], padx=30, pady=10)
        self.modal_login.grid(row=2, column=0, columnspan=3)
        
        ### Campo usuário
        self.container_usuario = tk.Frame(self.modal_login, bg=constants.cores['cinza'])
        self.container_usuario.grid(row=2, column=0, columnspan=3)
        self.lbl_usuario = tk.Label(self.container_usuario, text='Usuário:', bg=constants.cores['cinza'])
        self.lbl_usuario.pack(anchor='w', fill='y')
        self.ent_usuario = tk.Entry(self.container_usuario)
        self.ent_usuario.pack(anchor='w')

        ### Campo senha
        self.container_senha = tk.Frame(self.modal_login, bg=constants.cores['cinza'])
        self.container_senha.grid(row=3, column=0, columnspan=3)
        self.lbl_senha = tk.Label(self.container_senha, text='Senha:', bg=constants.cores['cinza'])
        self.lbl_senha.pack(anchor='w')
        self.ent_senha = tk.Entry(self.container_senha, show='*')
        self.ent_senha.pack(anchor='w')

        ### Esqueci a senha
        self.lbl_esqueciASenha = tk.Label(self.modal_login, text='Esqueceu a senha?', relief='flat', bg=constants.cores['cinza'])
        self.lbl_esqueciASenha.grid(row=4, column=2, columnspan=1, sticky='e')
        self.lbl_esqueciASenha.bind('<Button-1>', self.test)

        ### Botão continuar
        self.btn_continuar = tk.Button(self.modal_login, text='Continuar', bg=constants.cores['principal'], fg=constants.cores['branco'], command=self.onContinuar)
        self.btn_continuar.grid(row=5, column=0, columnspan=3, sticky='nswe')
    
    def test(self, event):
        print('Testando bind!')
    
    def onContinuar(self):

        if self.autenticar_login():
            self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MENU_PRINCIPAL)
            self.limpar_campos()
        else:
            tk.messagebox.showinfo("Usuário inválido", f"Login ou senha inválido(s).")
            
    def limpar_campos(self):
        self.ent_usuario.delete(0, 'end')
        self.ent_senha.delete(0, 'end')
    
    def autenticar_login(self):
        login = self.ent_usuario.get()
        senha = self.ent_senha.get()

        if login == '' or senha == '':
            return False

        # Conferir se o login existe
        usuario = self.controle_usuarios.busca_usuario(login)

        # Usuário não encontrado
        if not usuario:
            # tk.messagebox.showinfo("Quem é você?", f"Usuário não encontrado.")
            return False

        # Senha incorreta
        if senha != usuario[0][2]:
            # tk.messagebox.showinfo("Senha incorreta", f"Senha incorreta")
            return False
    
        # Login válido
        return True