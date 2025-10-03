import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.escola_controller import EscolaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.menus.menu_painel_de_opcoes_crud import MenuPainelDeOpcoesCRUD
from view.telas.tela_base import TelaBase

class TelaListagemBase(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, tipo_entidade, controle_entidade , largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        #Tipo de entidade manipulada (Usuario, Escola, Fornecedor ou Insumo)
        self.tipo_entidade = tipo_entidade
        
        # Controlador da entidade
        self.controle = controle_entidade

        # Informações do treeview
        self.linhas_treeview = 20 # Número de linhas visíveis
        self.colunas = [] # Cabeçalhos das colunas
        self.dados = [] # Dados que preencherão a tabela
        
        ### Painel de ações
        self.painel_de_acoes = MenuPainelDeOpcoesCRUD(self, self)
        self.painel_de_acoes.mostrar()

        # Criar e exibir a listagem de usuários
        self.criar_listagem()
    
    def get_descricao_entidade(self):
        match self.tipo_entidade:
            case constants.ENTIDADE_USUARIO:
                return "o", "usuário"
            case constants.ENTIDADE_ESCOLA:
                return "a", "escola"
            case constants.ENTIDADE_FORNECEDOR:
                return "o", "fornecedor"
            case constants.ENTIDADE_INSUMO:
                return "o", "insumo"
            case _:
                return "", ""

    def criar_listagem(self):
        self.tvw_tabela = ttk.Treeview(self, height=self.linhas_treeview, columns=self.colunas, show='headings')

        self.tvw_tabela.bind("<<TreeviewSelect>>", self.item_selecionado)

        self.tvw_tabela.pack(pady=17, padx=10, fill='x', expand=False)

    def item_selecionado(self, event):
        selecao = self.tvw_tabela.selection()

        # Só edita/exclui se houver apenas uma opção selecionada
        if len(selecao) == 1:
            self.habilitar_botao_de_editar()
            self.habilitar_botao_de_excluir()
        else:
            self.desabilitar_botao_de_editar()
            self.desabilitar_botao_de_excluir()
        
    # Botões do painel
    def habilitar_botao_de_editar(self):
        self.painel_de_acoes.btn_editar.config(state='normal')
    
    def desabilitar_botao_de_editar(self):
        self.painel_de_acoes.btn_editar.config(state='disabled')
    
    def habilitar_botao_de_excluir(self):
        self.painel_de_acoes.btn_excluir.config(state='normal')
    
    def desabilitar_botao_de_excluir(self):
        self.painel_de_acoes.btn_excluir.config(state='disabled')
    
    ###

    def buscar_tuplas(self):
        # adicionar o listar do controller respectivo
        # self.controle.listar()
        return []

    def atualizar_listagem(self):
        # Apaga os itens da treeview
        self.tvw_tabela.delete(*self.tvw_tabela.get_children())

        # Atualiza a treeview com os dados do banco
        tuplas = self.buscar_tuplas()
        for item in tuplas:
            self.tvw_tabela.insert('', 'end', values=item)

    def editar_item(self):
        """Edita o item selecionado"""
        item_selecionado = self.tvw_tabela.selection()[0]
        valores = self.tvw_tabela.item(item_selecionado, 'values')
        item = self.controle.buscar_por_id(valores[0])
        
        if item:
            self.gerenciador_de_janelas.editar(item, self.tipo_entidade)

    def excluir_item(self):
        """Exclui o item selecionado"""
        item_selecionado = self.tvw_tabela.selection()[0]
        valores = self.tvw_tabela.item(item_selecionado, 'values')
        
        if valores:
            # Confirma a exclusão
            resposta = tk.messagebox.askyesno("Confirmar Exclusão", 
                                            f"Tem certeza que deseja excluir {(lambda e: f"{e[0]} {e[1]}")(self.get_descricao_entidade())} '{valores[1]}'?")
            if resposta:
                # Chama o controller para excluir
                resultado = self.controle.excluir(valores[0])
                if resultado:
                    # Remove o item da treeview
                    self.tvw_tabela.delete(item_selecionado)
                    tk.messagebox.showinfo("Sucesso",(
                                           f"{(lambda e: f'{e[1].capitalize()} excluíd{e[0]}')(self.get_descricao_entidade())}"
                                           " com sucesso!"))
                else:
                    tk.messagebox.showerror("Erro", f"Erro ao excluir {(lambda e: f"{e[0]} {e[1]}")(self.get_descricao_entidade())}!")

    def mostrar(self):
        # Atualiza os dados
        self.atualizar_listagem()

        # Mostra o componente na tela
        self.pack(expand=True, fill='both', anchor='center')
    
    def adicionar(self):
        # Chama a tela de cadastro correspondente à entidade manipulada
        tela_cadastro = f"cadastrar-{self.tipo_entidade}"
        self.alterar_para_a_tela(tela_cadastro)
    
    def editar(self):
        """Edita o item selecionado"""
        item_selecionado = self.tvw_tabela.selection()[0]
        valores = self.tvw_tabela.item(item_selecionado, 'values')
        item = self.controle.buscar_por_id(valores[0])
        
        if item:
            self.gerenciador_de_janelas.editar(item)
    
    def excluir(self):
        pass