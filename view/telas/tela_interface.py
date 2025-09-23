import abc
import tkinter as tk

class TelaInterface(abc.ABC, tk.Frame):
    """Interface que todas as telas devem implementar"""
    
    @abc.abstractmethod
    def mostrar(self):
        """Exibe a tela"""
        pass
    
    @abc.abstractmethod
    def esconder(self):
        """Esconde a tela"""
        pass
