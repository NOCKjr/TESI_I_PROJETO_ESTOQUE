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
        self.codigo_confirmado = False

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
        self.btn_continuar.bind('<Return>', lambda event: self.onContinuar())

    
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

        # print(login, senha)

        if login == '' or senha == '':
            return False

        # Conferir se o login existe
        usuario = self.controle_usuarios.busca_usuario(login)

        # print(f"{usuario = }")

        # Usuário não encontrado
        if not usuario:
            # Messagebox.show_info("Usuário não encontrado.", title="Quem é você?")
            return False
        
        #Criptografa a senha digitada pelo usuário e compara com o hash salvo no banco de dados
        hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        # Senha incorreta
        if hash != usuario["senha"]:
            # Messagebox.show_info("Senha incorreta", title="Senha incorreta")
            return False
    
        # Login válido
        return True
    
    def solicitar_usuario(self):
        root = self.gerenciador_de_janelas.master
        
        # Cria um Toplevel
        janela = tk.Toplevel(root)
        janela.title("Redefinir Senha")
        janela.geometry("300x150")
        
        self.update_idletasks() # Garante que a janela seja desenhada
        # janela.transient(root)  # Depende da janela principal (fica sempre por cima)
        janela.grab_set()       # bloqueia interação com a janela principal
        janela.focus_set()      # Alterar o foco do teclado para a janela aberta

        ttk.Label(janela, text="Digite seu email ou nome de usuário:").pack(pady=10)
        entrada = ttk.Entry(janela)
        entrada.pack(pady=5)
        # Ao clicar em "Enter" com o campo entrada selecionado continuar() será chamado
        entrada.bind('<Return>', lambda event: continuar())

        def continuar():
            nome = entrada.get().strip()
            if not nome:
                Messagebox.show_error("Digite um nome de usuário!", title="Erro")
                self.username = None
                return
            self.username = nome
            janela.destroy()  # fecha a janela e libera o fluxo

        ttk.Button(janela, text="Continuar", command=continuar).pack(pady=10)

        # Bloqueia o processo até a janela ser fechada
        root.wait_window(janela)
    
    def solicitar_codigo(self):
        janela = tk.Toplevel(self.gerenciador_de_janelas.master)
        janela.title("Verificação de Código")
        janela.geometry("300x150")

        self.update_idletasks() # Garante que a janela seja desenhada
        janela.grab_set()

        ttk.Label(janela, text="Digite o código enviado para seu e-mail:").pack(pady=10)
        entrada = ttk.Entry(janela)
        entrada.pack(pady=5)
        # Ao clicar em "Enter" com o campo entrada selecionado confirmar() será chamado
        entrada.bind('<Return>', lambda event: confirmar())

        def confirmar():
            codigo_digitado = entrada.get().strip()
            if codigo_digitado == self.codigo_gerado:
                Messagebox.show_info("Código verificado com sucesso!", title="Sucesso")
                self.codigo_confirmado = True
                janela.destroy()
            else:
                Messagebox.show_error("Código incorreto!", title="Erro")
                self.codigo_confirmado = False


        ttk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)

        # Bloqueia até a janela ser fechada
        self.gerenciador_de_janelas.master.wait_window(janela)


    def redefinir_senha(self, event):
        # Solicita o usuário antes de enviar o código
        self.solicitar_usuario()

        print(f"{self.username = }")

        usuario = self.controle_usuarios.busca_usuario(self.username)

        if not usuario:
            Messagebox.show_error("Digite um email ou nome de usuário válido!", title="Erro")
            return
        
        print("usuario obtido")

        email_usuario = usuario['email']

        self.codigo_gerado = str(random.randint(100000, 999999))
        corpo = f"Seu código de verificação é: {self.codigo_gerado}"

        # Configurações do servidor SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email_app = 'sistema.sigeme@gmail.com'
        senha_app = 'tbbu ufnz fzqu engl' #senha de app gerada pelo google

        msg = MIMEText(corpo)
        msg['Subject'] = 'SIGEME - Código de verificação'
        msg['From'] = email_app
        msg['To'] = email_usuario #email do usuário aqui

        Messagebox.show_info(f"Um código de verificação será enviado para {email_usuario}. Por favor, aguarde.", title="Enviando email")

        try:
            print("mandando email")
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_app, senha_app)
                server.sendmail(email_app, email_usuario, msg.as_string())
            
            print("mandou")
            self.solicitar_codigo()

        except Exception as e:
            Messagebox.show_error(f"Não foi possível enviar o e-mail de verificação. Verifique sua conexão ou tente mais tarde.\nErro: {e}", title="Erro de Conexão")
            return # Interrompe o fluxo se não conseguir enviar
        
        if self.codigo_confirmado:
            Messagebox.show_info("Agora você pode redefinir sua senha!", title="Próxima etapa")

            janela = tk.Toplevel(self.gerenciador_de_janelas.master)
            janela.title("Criação da nova senha")
            janela.geometry("300x150")

            self.update_idletasks()
            janela.grab_set()

            ttk.Label(janela, text=f"Digite sua nova senha").pack(pady=10)
            entrada = ttk.Entry(janela, show="*")
            entrada.pack(pady=5)
            # Ao clicar em "Enter" com o campo entrada selecionado continuar() será chamado
            entrada.bind('<Return>', lambda event: continuar())

            def continuar():

                senha = entrada.get().strip() 
                if not senha:
                    Messagebox.show_error(title="Erro", message="Digite uma senha!")
                    return
                user = self.controle_usuarios.busca_usuario(self.username)
                self.controle_usuarios.atualizar_usuario(user["id"], user["nick"], user["email"], senha, user["tipo"])
                janela.destroy()  # fecha a janela e libera o fluxo

            ttk.Button(janela, text="Continuar", command=continuar).pack(pady=10)

        else:
            Messagebox.show_warning("Verificação não concluída.", title="Aviso")