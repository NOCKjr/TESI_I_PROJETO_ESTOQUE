import tkinter as tk
from tkinter import messagebox
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
        # Ao clicar em "Enter" com o campo usuário selecionado self.onContinuar() será chamado
        self.ent_usuario.bind('<Return>', lambda event: self.onContinuar())

        ### Campo senha
        self.container_senha = tk.Frame(self.modal_login, bg=constants.cores['cinza'])
        self.container_senha.grid(row=3, column=0, columnspan=3)
        self.lbl_senha = tk.Label(self.container_senha, text='Senha:', bg=constants.cores['cinza'])
        self.lbl_senha.pack(anchor='w')
        self.ent_senha = tk.Entry(self.container_senha, show='*')
        self.ent_senha.pack(anchor='w')
        # Ao clicar em "Enter" com o campo senha selecionado self.onContinuar() será chamado
        self.ent_senha.bind('<Return>', lambda event: self.onContinuar())

        ### Esqueci a senha
        self.lbl_esqueci_a_senha = tk.Label(self.modal_login, text='Esqueceu a senha?', relief='flat', bg=constants.cores['cinza'])
        self.lbl_esqueci_a_senha.grid(row=4, column=2, columnspan=1, sticky='e')
        self.lbl_esqueci_a_senha.bind('<Button-1>', self.redefinir_senha)
        # Melhorara a usabilidade adicionando um cursor de mãozinha ao passar o mouse sobre o label
        self.lbl_esqueci_a_senha.bind('<Enter>', lambda event: self.lbl_esqueci_a_senha.config(cursor="hand2"))
        self.lbl_esqueci_a_senha.bind('<Leave>', lambda event: self.lbl_esqueci_a_senha.config(cursor=""))

        ### Botão continuar
        self.btn_continuar = tk.Button(self.modal_login, text='Continuar', bg=constants.cores['principal'], fg=constants.cores['branco'], command=self.onContinuar)
        self.btn_continuar.grid(row=5, column=0, columnspan=3, sticky='nswe')
        # Ao clicar em "Enter" com o botão selecionado self.onContinuar() será chamado
        self.btn_continuar.bind('<Return>', lambda event: self.onContinuar())
    
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
        
        #Criptografa a senha digitada pelo usuário e compara com o hash salvo no banco de dados
        hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()

        # Senha incorreta
        if hash != usuario["senha"]:
            # tk.messagebox.showinfo("Senha incorreta", f"Senha incorreta")
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

        tk.Label(janela, text="Digite seu email ou nome de usuário:").pack(pady=10)
        entrada = tk.Entry(janela)
        entrada.pack(pady=5)
        # Ao clicar em "Enter" com o campo entrada selecionado continuar() será chamado
        entrada.bind('<Return>', lambda event: continuar())

        def continuar():
            nome = entrada.get().strip()
            if not nome:
                messagebox.showerror("Erro", "Digite um nome de usuário!")
                self.username = None
                return
            self.username = nome
            janela.destroy()  # fecha a janela e libera o fluxo

        tk.Button(janela, text="Continuar", command=continuar).pack(pady=10)

        # Bloqueia o processo até a janela ser fechada
        root.wait_window(janela)
    
    def solicitar_codigo(self):
        janela = tk.Toplevel(self.gerenciador_de_janelas.master)
        janela.title("Verificação de Código")
        janela.geometry("300x150")

        self.update_idletasks() # Garante que a janela seja desenhada
        janela.grab_set()

        tk.Label(janela, text="Digite o código enviado para seu e-mail:").pack(pady=10)
        entrada = tk.Entry(janela)
        entrada.pack(pady=5)
        # Ao clicar em "Enter" com o campo entrada selecionado confirmar() será chamado
        entrada.bind('<Return>', lambda event: confirmar())

        def confirmar():
            codigo_digitado = entrada.get().strip()
            if codigo_digitado == self.codigo_gerado:
                messagebox.showinfo("Sucesso", "Código verificado com sucesso!")
                self.codigo_confirmado = True
                janela.destroy()
            else:
                messagebox.showerror("Erro", "Código incorreto!")
                self.codigo_confirmado = False
                janela.destroy()

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)

        # Bloqueia até a janela ser fechada
        self.gerenciador_de_janelas.master.wait_window(janela)


    def redefinir_senha(self, event):
        # Solicita o usuário antes de enviar o código
        self.solicitar_usuario()

        print(f"{self.username = }")

        usuario = self.controle_usuarios.busca_usuario(self.username)

        if not usuario:
            messagebox.showerror("Erro", "Digite um email ou nome de usuário válido!")
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

        messagebox.showinfo("Enviando email", f"Um código de verificação será enviado para {email_usuario}. Por favor, aguarde.")

        try:
            print("mandando email")
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_app, senha_app)
                server.send_message(msg)
            
            print("mandou")
            self.solicitar_codigo()

        except Exception as e:
            messagebox.showerror("Erro de Conexão", f"Não foi possível enviar o e-mail de verificação. Verifique sua conexão ou tente mais tarde.\nErro: {e}")
            return # Interrompe o fluxo se não conseguir enviar
        
        if self.codigo_confirmado:
            messagebox.showinfo("Próxima etapa", "Agora você pode redefinir sua senha!")

            janela = tk.Toplevel(self.gerenciador_de_janelas.master)
            janela.title("Criação da nova senha")
            janela.geometry("300x150")

            self.update_idletasks()
            janela.grab_set()

            tk.Label(janela, text=f"Digite sua nova senha").pack(pady=10)
            entrada = tk.Entry(janela, show="*")
            entrada.pack(pady=5)
            # Ao clicar em "Enter" com o campo entrada selecionado continuar() será chamado
            entrada.bind('<Return>', lambda event: continuar())

            def continuar():

                senha = entrada.get().strip() 
                if not senha:
                    messagebox.showerror("Erro", "Digite uma senha!")
                    return
                user = self.controle_usuarios.busca_usuario(self.username)
                self.controle_usuarios.atualizar_usuario(user["id"], user["nick"], user["email"], senha, user["tipo"])
                janela.destroy()  # fecha a janela e libera o fluxo

            tk.Button(janela, text="Continuar", command=continuar).pack(pady=10)

        else:
            messagebox.showwarning("Aviso", "Verificação não concluída.")