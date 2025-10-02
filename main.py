import tkinter as tk
import ttkbootstrap as ttk
from view.App import App
import constants
from model import init_db
from control.usuario_controller import UsuarioController

if __name__ == '__main__':

    #cria o banco de dados ao instalar o executável
    init_db.create_db()

    #cria o usuário padrão de primeiro acesso (nome 'admin' e senha 'admin')
    controle_usuario = UsuarioController()
    controle_usuario.inserir_usuario(nick='admin', senha='admin', tipo='A') 
    
    # janela principal
    root = ttk.Window(themename="cosmo")
    root.geometry(f'{constants.LARGURA_JANELA}x{constants.ALTURA_JANELA}')
    root.minsize(width=constants.LARGURA_JANELA, height=constants.ALTURA_JANELA)
    root.resizable(width=False, height=False)
    root.title('SIGEME - Sistema de Gerenciamento de Estoque de Merendas Escolares')

    # frame inicial
    app = App(root)
    app.pack(expand=True, fill='both', anchor='center')

    # loop principal
    root.mainloop()