import tkinter as tk
from view.tela_login import TelaLogin
import constants

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.telaLogin = TelaLogin(self)

        # A tela inicial é a de login
        self.telaAtual = self.telaLogin

        self.telaAtual.pack(fill='both', expand=True)
