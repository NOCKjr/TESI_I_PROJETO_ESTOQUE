import tkinter as tk
from tkinter import ttk
import constants

class TelaMenuPrincipal(tk.Frame):
    def __init__(self, master, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')        

        self.cores = {
            "principal": '#075F8B',
            "secundario": '#87C5FF',
            "cinza": "#d9d9d9",
            'branco': '#ffffff'
        }

        ### Container com as opções de navegação disponíveis
        self.container_visual = tk.Frame(self, bg=self.cores['branco'], padx=30, pady=20)
        self.container_visual.place(anchor='center', relx=0.5, rely=0.45)

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['secundario'])
        self.lbl_sigeme.place(anchor='n', relx=0.5, y=10)

        # ## Modal com os campos de login
        # self.modal_login = tk.Frame(self.container_visual, bg=self.cores['cinza'], padx=30, pady=10)
        # self.modal_login.grid(row=2, column=0, columnspan=3)
        
        # ### Campo usuário
        # self.container_usuario = tk.Frame(self.modal_login, bg=self.cores['cinza'])
        # self.container_usuario.grid(row=2, column=0, columnspan=3)
        # self.lbl_usuario = tk.Label(self.container_usuario, text='Usuário:', bg=self.cores['cinza'])
        # self.lbl_usuario.pack(anchor='w', fill='y')
        # self.ent_usuario = tk.Entry(self.container_usuario)
        # self.ent_usuario.pack(anchor='w')

        # ### Campo senha
        # self.container_senha = tk.Frame(self.modal_login, bg=self.cores['cinza'])
        # self.container_senha.grid(row=3, column=0, columnspan=3)
        # self.lbl_senha = tk.Label(self.container_senha, text='Senha:', bg=self.cores['cinza'])
        # self.lbl_senha.pack(anchor='w')
        # self.ent_senha = tk.Entry(self.container_senha, show='*')
        # self.ent_senha.pack(anchor='w')

        # ### Esqueci a senha
        # self.lbl_esqueciASenha = tk.Label(self.modal_login, text='Esqueceu a senha?', relief='flat', bg=self.cores['cinza'])
        # self.lbl_esqueciASenha.grid(row=4, column=2, columnspan=1, sticky='e')
        # self.lbl_esqueciASenha.bind('<Button-1>', self.test)

        # ### Botão continuar
        # self.btn_continuar = tk.Button(self.modal_login, text='Continuar', bg=self.cores['principal'], fg=self.cores['branco'])
        # self.btn_continuar.grid(row=5, column=0, columnspan=3, sticky='nswe')

    def test(self, event):
        print('Testando bind!')