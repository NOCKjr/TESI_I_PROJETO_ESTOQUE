from ttkbootstrap.dialogs import Messagebox
import tkinter as tk
import constants
import hashlib
import smtplib
import random
from email.mime.text import MIMEText

from tkinter import ttk
from view.telas.tela_base import TelaBase
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from control.usuario_controller import UsuarioController

class TelaLogin(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        self.username = None

        # Controlador de usuários
        self.controle_usuarios = UsuarioController()

        ### Container com o título da aplicação e os campos de login
        self.container_visual = ttk.Frame(self, padding=(30, 20))
        self.container_visual.place(anchor='center', relx=0.5, rely=0.45)

        ### Logo (centralizado automaticamente com pack)
        self.lbl_sigeme = ttk.Label(
            self.container_visual,
            text='SIGEME',
            font=("Arial", 24, "bold")
        )
        self.lbl_sigeme.pack(pady=10)

        ## Modal com os campos de login
        self.modal_login = ttk.Frame(self.container_visual, padding=(30, 10))
        self.modal_login.pack()

        ### Campo usuário
        self.container_usuario = ttk.Frame(self.modal_login)
        self.container_usuario.pack(pady=5, fill='x')
        self.lbl_usuario = ttk.Label(self.container_usuario, text='Usuário:')
        self.lbl_usuario.pack(anchor='w')
        self.ent_usuario = ttk.Entry(self.container_usuario)
        self.ent_usuario.pack(fill='x')
        self.ent_usuario.bind('<Return>', lambda event: self.onContinuar())

        ### Campo senha
        self.container_senha = ttk.Frame(self.modal_login)
        self.container_senha.pack(pady=5, fill='x')
        self.lbl_senha = ttk.Label(self.container_senha, text='Senha:')
        self.lbl_senha.pack(anchor='w')
        self.ent_senha = ttk.Entry(self.container_senha, show='*')
        self.ent_senha.pack(fill='x')
        self.ent_senha.bind('<Return>', lambda event: self.onContinuar())

        ### Esqueci a senha
        self.lbl_esqueci_a_senha = ttk.Label(
            self.modal_login, text='Esqueceu a senha?', cursor="hand2"
        )
        self.lbl_esqueci_a_senha.pack(anchor='e', pady=5)
        self.lbl_esqueci_a_senha.bind('<Button-1>', self.redefinir_senha)

        ### Botão continuar
        self.btn_continuar = ttk.Button(
            self.modal_login, text='Continuar', command=self.onContinuar, bootstyle="success"
        )
        self.btn_continuar.pack(fill='x', pady=10)

    
    def onContinuar(self):

        if self.autenticar_login():
            self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_MENU_PRINCIPAL)
            self.limpar_campos()
        else:
            Messagebox.show_info("Login ou senha inválido(s).", title="Login não realizado")
            
    def limpar_campos(self):
        self.ent_usuario.delete(0, 'end')
        self.ent_senha.delete(0, 'end')
    
    def autenticar_login(self):
        login = self.ent_usuario.get()
        senha = self.ent_senha.get()

        if login == '' or senha == '':
            return False

        # Conferir se o login existe
        resp = self.controle_usuarios.buscar_usuario(login)
        usuario = resp.retorno

        # Usuário não encontrado
        if not usuario:
            # Messagebox.show_info("Usuário não encontrado.", title="Quem é você?")
            return False
        
        # Criptografa a senha digitada pelo usuário 
        hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        # A senha é diferente da encontrada no banco de dados
        if hash != usuario["senha"]:
            # Messagebox.show_info("Senha incorreta", title="Senha incorreta")
            return False

        # Login válido
        return True
    
    def redefinir_senha(self, event):
        root = self.gerenciador_de_janelas.master
        janela = tk.Toplevel(root)
        janela.title("Redefinir Senha")
        janela.geometry("300x150")

        # janela.transient(root) # Depende da janela principal (fica sempre por cima)
        def impede_interacao(): 
            janela.update_idletasks() # Garante que a janela seja desenhada
            janela.grab_set() # Bloqueia interações com outras janelas
            janela.focus_set()
        
        impede_interacao()

        container = ttk.Frame(janela)
        container.pack(pady=3, padx=3, fill="both", expand=True)

        def limpar_container():
            for widget in container.winfo_children():
                widget.destroy()

        def mostrar_etapa_usuario():
            limpar_container()
            ttk.Label(container, text="Digite seu email ou nome de usuário:").pack(pady=10)
            entrada = ttk.Entry(container)
            entrada.pack(pady=5)
            entrada.focus_set()
            entrada.bind('<Return>', lambda e: continuar_usuario(entrada.get().strip()))

            def continuar_usuario(nome):
                self.username = nome
                if not nome:
                    Messagebox.show_error("Digite um nome de usuário!", title="Erro", parent=janela)
                    impede_interacao()
                    return
                resp = self.controle_usuarios.buscar(nome)
                usuario = resp.retorno

                if not usuario:
                    Messagebox.show_error("Digite um email ou nome de usuário válido!", title="Erro", parent=janela)
                    impede_interacao()
                    return
                
                self.username = usuario['nick']
                etapa_envio_codigo(usuario['email'])

            ttk.Button(container, text="Continuar", command=lambda: continuar_usuario(entrada.get().strip())).pack(pady=10)

        def etapa_envio_codigo(email_usuario):

            self.codigo_gerado = str(random.randint(100000, 999999))
            corpo = f"Seu código de verificação é: {self.codigo_gerado}"

            smtp_server, smtp_port = 'smtp.gmail.com', 587
            email_app, senha_app = 'sistema.sigeme@gmail.com', 'tbbu ufnz fzqu engl'

            msg = MIMEText(corpo)
            msg['Subject'] = 'SIGEME - Código de verificação'
            msg['From'] = email_app
            msg['To'] = email_usuario

            Messagebox.show_info(f"Um código de verificação será enviado para {email_usuario}. Por favor, aguarde.", title="Enviando email", parent=janela)
            impede_interacao()

            try:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(email_app, senha_app)
                    server.sendmail(email_app, email_usuario, msg.as_string())
                mostrar_etapa_codigo()
            except Exception as e:
                Messagebox.show_error(f"Não foi possível enviar o e-mail. Verifique sua conexão.\nErro: {e}", title="Erro de Conexão", parent=janela)
                janela.destroy()

        def mostrar_etapa_codigo():
            impede_interacao()
            limpar_container()
            ttk.Label(container, text="Digite o código enviado para seu e-mail:").pack(pady=10)
            entrada = ttk.Entry(container)
            entrada.pack(pady=5)
            entrada.focus_set()
            entrada.bind('<Return>', lambda e: confirmar_codigo(entrada.get().strip()))


            def confirmar_codigo(codigo_digitado):
                if codigo_digitado == self.codigo_gerado:
                    Messagebox.show_info("Código verificado com sucesso!", title="Sucesso", parent=janela)
                    mostrar_etapa_nova_senha()
                else:
                    Messagebox.show_error("Código incorreto!", title="Erro", parent=janela)
                    impede_interacao()

            ttk.Button(container, text="Confirmar", command=lambda: confirmar_codigo(entrada.get().strip())).pack(pady=10)

        def mostrar_etapa_nova_senha():
            impede_interacao()
            limpar_container()
            janela.title("Criação da nova senha")
            ttk.Label(container, text="Digite sua nova senha:").pack(pady=10)
            entrada = ttk.Entry(container, show="*")
            entrada.pack(pady=5)
            entrada.focus_set()
            entrada.bind('<Return>', lambda e: salvar_nova_senha(entrada.get().strip()))

            def salvar_nova_senha(senha):
                if not senha:
                    Messagebox.show_error("Digite uma senha!", title="Erro", parent=janela)
                    impede_interacao()
                    return
                resp = self.controle_usuarios.buscar(self.username)
                user = resp.retorno
                self.controle_usuarios.atualizar_usuario(user["id"], user["nick"], user["email"], senha, user["tipo"])
                Messagebox.show_info("Senha redefinida com sucesso!", title="Sucesso", parent=janela)
                janela.destroy()

            ttk.Button(container, text="Salvar", command=lambda: salvar_nova_senha(entrada.get().strip())).pack(pady=10)

        mostrar_etapa_usuario()
        self.master.wait_window(janela)