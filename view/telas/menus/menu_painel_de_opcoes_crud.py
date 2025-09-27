import tkinter as tk
import constants

class MenuPainelDeOpcoesCRUD(tk.Frame):
    def __init__(self, master, tela_associada):
        super().__init__(master)
        self.tela_associada = tela_associada

        # Container com as ações disponíveis
        self.container_acoes = tk.Frame(self)
        self.container_acoes.pack()
        
        # Adicionar
        self.btn_adicionar = tk.Button(self.container_acoes, text="Adicionar", bg=constants.cores['secundario'], command=self.adicionar)
        self.btn_adicionar.pack(side='left')

        # Editar
        self.btn_editar = tk.Button(self.container_acoes, text="Editar", bg=constants.cores['secundario'], state='disabled', command=self.editar)
        self.btn_editar.pack(side='left')

        # Excluir
        self.btn_excluir = tk.Button(self.container_acoes, text="Excluir", bg=constants.cores['secundario'], state='disabled', command=self.excluir)
        self.btn_excluir.pack(side='left')

    
    def mostrar(self):
        self.pack(side='bottom')

    def adicionar(self):
        self.tela_associada.adicionar()

    def editar(self):
        self.tela_associada.editar()

    def excluir(self):
        self.tela_associada.excluir()

        