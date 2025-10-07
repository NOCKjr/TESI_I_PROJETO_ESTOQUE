#from PIL import ImageTk
import tkinter as tk
import ttkbootstrap as ttk
from app_context import get_context
import constants
from view.App import App
from model import init_db
from control.usuario_controller import UsuarioController

def configurar_janela(root: tk.Tk):
    """Define as configurações iniciais da janela tkinter"""

    # Pega dimensões do monitor
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Define a proporção desejada
    proporcao = get_context().proporcao
    largura_janela = int(largura_tela * proporcao)
    altura_janela = int(altura_tela * proporcao)

    # Calcula posição centralizada
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 4

    # root.geometry(f'{constants.LARGURA_JANELA}x{constants.ALTURA_JANELA}')
    root.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')
    root.minsize(width=600, height=400)
    # root.resizable(width=False, height=False)
    root.title('SIGEME - Sistema de Gerenciamento de Estoque de Merendas Escolares')

if __name__ == '__main__':

    #cria o banco de dados ao instalar o executável
    init_db.create_db()
    
    # janela principal
    root = ttk.Window(themename="cosmo")

    # configura a janela
    configurar_janela(root)

    # frame inicial
    app = App(root)
    app.pack(expand=True, fill='both', anchor='center')

    # loop principal
    root.mainloop()

