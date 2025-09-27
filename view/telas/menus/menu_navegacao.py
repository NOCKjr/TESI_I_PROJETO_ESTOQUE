import tkinter as tk
import constants

class MenuNavegacao(tk.Frame):
    def __init__(self, master, gerenciador_de_janelas):
        super().__init__(master)

        # Gerenciador de janela
        self.gerenciador_de_janelas = gerenciador_de_janelas
    
        # Dicionário de abas
        self.abas = {
            "Movimentações": constants.TELA_MOVIMENTACOES,
            "Usuários": constants.TELA_LISTAGEM_USUARIOS,
            "Escolas": constants.TELA_CADASTRAR_ESCOLA,
            "Fornecedores": constants.TELA_CADASTRAR_FORNECEDOR,
            "Insumos": constants.TELA_CADASTRAR_INSUMO
        }

        # Botões do "menu"
        self.botoes = {}
        for aba in self.abas:
            btn = tk.Button(self, text=aba, command=lambda tela=aba: self.gerenciador_de_janelas.alterar_para_a_tela(self.abas[tela]))
            btn.pack(side="left", padx=1, pady=2)
            self.botoes[aba] = btn
    
    def exibir(self):
        self.pack(side='top', fill='x')
    
    def esconder(self):
        self.pack_forget()