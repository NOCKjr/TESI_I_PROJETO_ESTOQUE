import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from control.usuario_controller import UsuarioController
from view.telas.cadastros.tela_formulario_base import TelaFormularioBase

class TelaCadastrarUsuario(TelaFormularioBase):
    def __init__(self, master, 
                       gerenciador_de_janelas: GerenciadorDeJanelasBase, 
                       modo_editar=False, 
                       largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, 
                         gerenciador_de_janelas, 
                         constants.ENTIDADE_USUARIO, 
                         UsuarioController(), 
                         modo_editar,
                         largura, altura)

        self.criar_campos_formulario()
    
    def criar_campos_formulario(self):
        super().criar_campos_formulario()

        # Login do usuário
        self.lbl_nick_usuario = tk.Label(self.container_formulario, text="Login usuário:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_nick_usuario.grid(row=0, column=0, pady=(2,0), sticky='nsw')
        self.ent_nick_usuario = tk.Entry(self.container_formulario)
        self.ent_nick_usuario.grid(row=1, column=0, columnspan=14, sticky='nsew')

        # Senha do usuário
        self.lbl_senha_usuario = tk.Label(self.container_formulario, text="Senha usuário:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_senha_usuario.grid(row=0, column=15, pady=(2,0), sticky='nsw')
        self.ent_senha_usuario = tk.Entry(self.container_formulario, show='*')
        self.ent_senha_usuario.grid(row=1, column=15, columnspan=15, sticky='nsew')

        # Email do usuário
        self.lbl_email_usuario = tk.Label(self.container_formulario, text="Email:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_email_usuario.grid(row=4, column=0, pady=(2,0), sticky='nsw')
        self.ent_email_usuario = tk.Entry(self.container_formulario)
        self.ent_email_usuario.grid(row=5, column=0, columnspan=30, sticky='nsew')

        # Tipo de usuário (Administrador ou Comum)
        self.lbl_tipo_usuario = tk.Label(self.container_formulario, text="Tipo de usuário:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_tipo_usuario.grid(row=8, column=0, pady=(10,0), sticky='nsw')
        self.cmb_tipo_usuario = ttk.Combobox(self.container_formulario, values=["Comum", "Administrador"], state="readonly")
        self.cmb_tipo_usuario.grid(row=9, column=0, columnspan=15, sticky='nsew')
        self.cmb_tipo_usuario.set("Comum")  # Valor padrão
    
    def editar_usuario(self, usuario):
        # Nick
        self.ent_nick_usuario.delete(0, 'end')
        self.ent_nick_usuario.insert(0, usuario['nick'])

        # Senha (placeholder em vez da senha real)
        self.ent_senha_usuario.delete(0, 'end')
        self.ent_senha_usuario.insert(0, "Digite a nova senha")
        self.ent_senha_usuario.config(fg="grey", show="")

        # funções para simular o placeholder
        def on_focus_in(event):
            if self.ent_senha_usuario.get() == "Digite a nova senha":
                self.ent_senha_usuario.delete(0, 'end')
                self.ent_senha_usuario.config(fg="black", show="*")

        def on_focus_out(event):
            if self.ent_senha_usuario.get() == "":
                self.ent_senha_usuario.insert(0, "Digite a nova senha")
                self.ent_senha_usuario.config(fg="grey", show="")

        self.ent_senha_usuario.bind("<FocusIn>", on_focus_in)
        self.ent_senha_usuario.bind("<FocusOut>", on_focus_out)

        # Email
        self.ent_email_usuario.delete(0, 'end')
        self.ent_email_usuario.insert(0, usuario['email'])

        # Tipo de usuário
        self.cmb_tipo_usuario.current(0 if usuario['tipo'] == 'C' else 1)

        # Flags de edição
        self.id_para_edicao = usuario['id']
        self.flag_editar = True

    def obter_campos_formulario(self):
        
        # Captura os valores dos campos
        nick = self.ent_nick_usuario.get()
        senha = self.ent_senha_usuario.get()
        email = self.ent_email_usuario.get()
        tipo_usuario = self.cmb_tipo_usuario.get()
        
        # Converte o tipo de usuário para o código esperado pelo banco
        tipo_codigo = 'A' if tipo_usuario == "Administrador" else 'C'

        return (nick, email, senha, tipo_codigo)
