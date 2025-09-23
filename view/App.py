import tkinter as tk
import constants

from view.telas.tela_interface import TelaInterface
from view.telas.tela_login import TelaLogin
from view.telas.tela_menu_principal import TelaMenuPrincipal
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase

class App(GerenciadorDeJanelasBase):
    def __init__(self, master):
        super().__init__(master)

        # Referências das telas usadas
        self.telas: dict[str, TelaInterface] = {
            "login": TelaLogin(self, self), # Tela de login
            "menu": TelaMenuPrincipal(self, self) # Tela de menu principal
        }
        
        # Inicia na tela de login
        self.alterar_para_a_tela("login")
    
    def get_tela(self, nome_tela: str):
        return self.telas[nome_tela]
        
