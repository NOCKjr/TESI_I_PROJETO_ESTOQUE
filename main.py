import tkinter as tk
from view.App import App
import constants

if __name__ == '__main__':
    # janela principal
    root = tk.Tk()
    root.geometry(f'{constants.LARGURA_JANELA}x{constants.ALTURA_JANELA}')
    root.minsize(width=constants.LARGURA_JANELA, height=constants.ALTURA_JANELA)
    # root.resizable(width=False, height=False)
    root.title('SIGEME - Sistema de Gerenciamento de Estoque de Merendas Escolares')

    # frame inicial
    app = App(root)
    app.pack(expand=True, fill='both', anchor='center')

    # loop principal
    root.mainloop()