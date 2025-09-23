import abc
import tkinter as tk

class TelaInterface(abc.ABC, tk.Frame):
    """Interface que todas as telas devem implementar"""

    cores = {
        "principal": '#075F8B',
        "secundario": '#87C5FF',
        "cinza": "#d9d9d9",
        'branco': '#ffffff'
    }
    
    @abc.abstractmethod
    def mostrar(self):
        """Exibe a tela"""
        pass
    
    @abc.abstractmethod
    def esconder(self):
        """Esconde a tela"""
        pass
