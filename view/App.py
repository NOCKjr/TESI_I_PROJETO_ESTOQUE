import tkinter as tk
from view.telas.tela_login import TelaLogin
from view.telas.tela_menu_principa import TelaMenuPrincipal
from view.telas.gerenciador_de_janelas import GerenciadoDeJanelasInterface
import constants

class App(GerenciadoDeJanelasInterface):
    def __init__(self, master):
        super().__init__(master)

        # Referências das telas usadas
        self.telas: dict[tk.Frame] = {
            "login": TelaLogin(self, self), # Tela de login
            "menu": TelaMenuPrincipal(self) # Tela de menu principal
        }
        
        # Inicia na tela de login
        self.alterarParaATela("login")
    
    def getTela(self, nome_tela: str):
        return self.telas[nome_tela]
        
