import tkinter as tk
import constants

from tkinter import ttk
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from control.usuario_controller import UsuarioController
from view.telas.tela_formulario_base import TelaFormularioBase

class TelaCadastrarUsuario(TelaFormularioBase):    
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, modo_editar=False, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, modo_editar)

        # Se o formulário foi aberto como edição, define-se o id do usuário editado
        self.id_usuario_editado = None

        # Controlador de usuários
        self.controle_usuarios = UsuarioController()
        
        # Login do usuário
        self.lbl_login_usuario = tk.Label(self.container_formulario, text="Login usuário:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_login_usuario.grid(row=0, column=0, pady=(2,0), sticky='nsw')
        self.ent_login_usuario = tk.Entry(self.container_formulario)
        self.ent_login_usuario.grid(row=1, column=0, columnspan=14, sticky='nsew')

        # Senha do usuário
        self.lbl_senha_usuario = tk.Label(self.container_formulario, text="Senha usuário:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_senha_usuario.grid(row=0, column=15, pady=(2,0), sticky='nsw')
        self.ent_senha_usuario = tk.Entry(self.container_formulario, show='*')
        self.ent_senha_usuario.grid(row=1, column=15, columnspan=14, sticky='nsew')

        # Email do usuário
        self.lbl_email_usuario = tk.Label(self.container_formulario, text="Email usuário:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_email_usuario.grid(row=2, column=15, pady=(2,0), sticky='nsw')
        self.ent_email_usuario = tk.Entry(self.container_formulario)
        self.ent_email_usuario.grid(row=3, column=15, columnspan=14, sticky='nsew')

        # Tipo de usuário (Administrador ou Comum)
        self.lbl_tipo_usuario = tk.Label(self.container_formulario, text="Tipo de usuário:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_tipo_usuario.grid(row=2, column=0, pady=(10,0), sticky='nsw')
        self.cmb_tipo_usuario = ttk.Combobox(self.container_formulario, values=["Comum", "Administrador"], state="readonly")
        self.cmb_tipo_usuario.grid(row=3, column=0, columnspan=14, sticky='nsew')
        self.cmb_tipo_usuario.set("Comum")  # Valor padrão

    def limpar_campos(self):
        self.ent_login_usuario.delete(0, 'end')
        self.ent_senha_usuario.delete(0, 'end')
        self.ent_email_usuario.delete(0, 'end')
        self.cmb_tipo_usuario.current(0)
        self.flag_editar = False
    
    def editar_usuario(self, usuario):

        self.ent_login_usuario.delete(0, 'end')
        self.ent_login_usuario.insert(0, usuario['login'])
        self.ent_senha_usuario.delete(0, 'end')
        self.ent_senha_usuario.insert(0, usuario['senha'])
        self.ent_email_usuario.delete(0, 'end')
        self.ent_email_usuario.insert(0, usuario['email'])
        self.cmb_tipo_usuario.current(0)
        self.cmb_tipo_usuario.current(0 if usuario['tipo'] == 'C' else 1)
        self.id_usuario_editado = usuario['id']
        self.flag_editar = True
    
    def onConfirmar(self):
        # Captura os valores dos campos
        login = self.ent_login_usuario.get()
        senha = self.ent_senha_usuario.get()
        email = self.ent_email_usuario.get()
        tipo_usuario = self.cmb_tipo_usuario.get()
        
        # Converte o tipo de usuário para o código esperado pelo banco
        tipo_codigo = 'A' if tipo_usuario == "Administrador" else 'C'
        
        if self.flag_editar:
            id = self.id_usuario_editado
            # Chama o controller para atualizar o usuário
            self.controle_usuarios.atualizar_usuario(id, login, email, senha, tipo_codigo)
        else:
            # Chama o controller para inserir novo usuário
            self.controle_usuarios.inserir_usuario(login, email, senha, tipo_codigo)
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()
        
        # Volta para a tela de listagem
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_USUARIOS)

    def onCancelar(self):
        # Reseta os valores dos campos do formulário
        self.limpar_campos()
        
        # Volta para a tela de listagem
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_USUARIOS)

    def set_flag_edicao(self, valor_flag=True):
        self.flag_editar = valor_flag

    def set_id_usuario_edicao(self, valor_id=None):
        self.id_usuario_editado = valor_id
