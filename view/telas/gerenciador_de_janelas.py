import tkinter as tk
import abc

from view.telas.tela_interface import TelaInterface

class GerenciadorDeJanelasBase(tk.Frame, abc.ABC):
    def __init__(self, master):
        super().__init__(master)
        self.tela_atual: TelaInterface | None = None
    
    @abc.abstractmethod
    def get_tela(self, nome_tela: str) -> tk.Frame:
        """Deve retornar a referência de um tkinter.Frame."""
        pass
    
    def alterar_para_a_tela(self, proxima_tela: str):
        tela_anterior = self.tela_atual
        self.tela_atual = self.get_tela(proxima_tela)

        if tela_anterior is not None:
            tela_anterior.pack_forget()
        
        self.tela_atual.mostrar()
