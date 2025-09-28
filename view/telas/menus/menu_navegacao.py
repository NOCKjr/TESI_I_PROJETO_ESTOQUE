import tkinter as tk
import constants

class MenuNavegacao(tk.Frame):
    def __init__(self, master, gerenciador_de_janelas):
        super().__init__(master)

        # Gerenciador de janela
        self.gerenciador_de_janelas = gerenciador_de_janelas

        # Aba atual selecionada
        self.aba_atual = ""
    
        # Dicionário de abas
        self.abas = {
            "Movimentações": constants.TELA_MOVIMENTACOES,
            "Usuários": constants.TELA_LISTAGEM_USUARIOS,
            "Escolas": constants.TELA_LISTAGEM_ESCOLAS,
            "Fornecedores": constants.TELA_LISTAGEM_FORNECEDORES,
            "Insumos": constants.TELA_LISTAGEM_INSUMOS,
            "Sair": constants.TELA_LOGIN
        }

        # Botões do "menu"
        self.botoes: dict[str, tk.Button] = {}
        # self.botoes["Sair"] = tk.Button(self, text="Sair", command=lambda: self.abrir_aba(aba))
        # self.botoes["Sair"].pack(side='right')
        for aba in self.abas:
            btn = tk.Button(self, text=aba, command=lambda aba=aba: self.abrir_aba(aba))
            if aba == 'Sair':
                btn.pack(side="right", padx=1, pady=2)
            else:
                btn.pack(side="left", padx=1, pady=2)
            self.botoes[aba] = btn
    
    def abrir_aba(self, nome):
        # Atualizar a refência da aba atual selecionada
        self.aba_atual = self.abas[nome]

        # Alterar o visual do botão selecionado
        for botao in self.botoes.values():
            botao.config(bg=constants.Cores.CINZA.value, fg=constants.Cores.PRETO.value)
        if nome != 'Sair': # destaca o botão se não for o de sair
            self.botoes[nome].config(bg=constants.Cores.PRINCIPAL.value, fg=constants.Cores.BRANCO.value)

        # Carregar a tela relacioada à aba selecionada
        self.gerenciador_de_janelas.alterar_para_a_tela(self.aba_atual)
    
    def exibir(self):
        self.pack(side='top', fill='x')
    
    def esconder(self):
        self.pack_forget()