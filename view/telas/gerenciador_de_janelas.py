import tkinter as tk
import constants

class GerenciadoDeJanelasInterface(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.tela_atual: tk.Frame = None
    
    def getTela(self, nome_tela: str):
        """Deve retornar a referência de um tkinter.Frame."""
        pass
    
    def alterarParaATela(self, proxima_tela: str):
        
        # altera a referência da anterior e da tela atual
        tela_anterior: tk.Frame = self.tela_atual
        self.tela_atual = self.getTela(proxima_tela)

        # esconde a tela anterior
        if tela_anterior is not None:
            tela_anterior.pack_forget()
        
        # mostra a nova tela
        self.tela_atual.pack()
        
