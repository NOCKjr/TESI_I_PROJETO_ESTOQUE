import ttkbootstrap as ttk
import constants

class MenuNavegacao(ttk.Frame):
    def __init__(self, master, gerenciador_de_janelas):
        super().__init__(master)

        # Gerenciador de janela
        self.gerenciador_de_janelas = gerenciador_de_janelas

        # Aba atual selecionada
        self.aba_atual = ""
    
        # Dicionário de abas
        self.abas = {
            "Movimentações": constants.TELA_LISTAGEM_MOVIMENTACOES,
            "Escolas": constants.TELA_LISTAGEM_ESCOLAS,
            "Fornecedores": constants.TELA_LISTAGEM_FORNECEDORES,
            "Insumos": constants.TELA_LISTAGEM_INSUMOS,
            "Usuários": constants.TELA_LISTAGEM_USUARIOS,
            "Sair": constants.TELA_LOGIN
        }

        # Botões do "menu"
        self.botoes: dict[str, ttk.Button] = {}
        for aba in self.abas:
            estilo = "primary" if aba != "Sair" else "danger"
            btn = ttk.Button(self, text=aba, command=lambda aba=aba: self.abrir_aba(aba), bootstyle=estilo)
            if aba == 'Sair':
                btn.pack(side="right", padx=1, pady=2)
            else:
                btn.pack(side="left", padx=1, pady=2)
            self.botoes[aba] = btn
    
    def abrir_aba(self, nome):
        # Atualizar a refência da aba atual selecionada
        self.aba_atual = self.abas[nome]
        
        self.gerenciador_de_janelas.alterar_para_a_tela(self.aba_atual)
    
    def exibir(self):
        usuario = getattr(self.gerenciador_de_janelas, 'usuario_logado', None)
        if usuario and usuario.get('tipo') != 'A':
            self.botoes['Usuários'].pack_forget()
        else:
            self.botoes['Usuários'].pack(side='left', padx=1, pady=2)
        self.pack(side='top', fill='x')
    
    def esconder(self):
        self.pack_forget()