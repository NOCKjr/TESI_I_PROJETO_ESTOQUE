import ttkbootstrap as ttk

import constants
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase

class TelaBase(ttk.Frame):
    """Interface que todas as telas devem implementar"""
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura)
        
        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas
    
    def mostrar(self):
        """Exibe a tela"""
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        """Esconde a tela"""
        self.pack_forget()
    
    def alterar_para_a_tela(self, proxima_tela):
        """Chama o gerenciador de janelas para alterar entre janelas"""
        self.gerenciador_de_janelas.alterar_para_a_tela(proxima_tela)
