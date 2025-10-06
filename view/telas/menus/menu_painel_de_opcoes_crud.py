import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import constants

class MenuPainelDeOpcoesCRUD(ttk.Frame):
    def __init__(self, master, tela_associada):
        super().__init__(master)
        self.tela_associada = tela_associada

        # Container com as ações disponíveis
        self.container_acoes = ttk.Frame(self)
        self.container_acoes.pack()
        
        # Adicionar
        self.btn_adicionar = ttk.Button(self.container_acoes, text="Adicionar", bootstyle="success", command=self.adicionar)
        self.btn_adicionar.pack(side='left', padx=5)

        # Editar
        self.btn_editar = ttk.Button(self.container_acoes, text="Editar", bootstyle="primary", state='disabled', command=self.editar)
        self.btn_editar.pack(side='left', padx=5)

        # Excluir
        self.btn_excluir = ttk.Button(self.container_acoes, text="Excluir", bootstyle="danger", state='disabled', command=self.excluir)
        self.btn_excluir.pack(side='left', padx=5)
    
    def mostrar(self):
        self.pack(side='bottom')
    
    def esconder(self):
        self.pack_forget()

    def adicionar(self):
        self.tela_associada.adicionar()

    def editar(self):
        self.tela_associada.editar()

    def excluir(self):
        self.tela_associada.excluir()

        