import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.controller_base import ControllerBase
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.menus.menu_painel_de_opcoes_crud import MenuPainelDeOpcoesCRUD
from view.telas.tela_base import TelaBase

class TelaListagemBase(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, tipo_entidade: str, controle_entidade: ControllerBase , cabecalho: list[str] = [], chaves_dict: list[str] = [], larguras_colunas: list[int] = [], largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)

        #Tipo de entidade manipulada (Usuario, Escola, Fornecedor ou Insumo)
        self.tipo_entidade = tipo_entidade
        
        # Controlador da entidade
        self.controle = controle_entidade

        # Informações do treeview
        self.linhas_treeview: int = 20 # Número de linhas visíveis
        self.cabecalho: list[str] = cabecalho # Cabeçalhos das colunas
        self.chaves_dict: list[str] = chaves_dict # Chaves de acesso aos campos do dict
        self.tvw_tabela: ttk.Treeview = None
        
        ### Painel de ações
        self.painel_de_acoes = MenuPainelDeOpcoesCRUD(self, self)
        self.painel_de_acoes.mostrar()

        # Criar e exibir a listagem de usuários
        self.criar_listagem(larguras_colunas)
    
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
            case constants.ENTIDADE_ENDERECO:
                return "o", "endereco"
            case constants.ENTIDADE_ITEM:
                return "o", "item"
            case constants.ENTIDADE_MOVIMENTACAO:
                return "a", "movimentação"
            case _:
                return "", ""
    
    def definir_cabecalho(self, cabecalho: list[str], chaves_dict: list[str]):
        if len(cabecalho) != len(chaves_dict):
            raise ValueError("Defina corretamente as chaves de acesso ao atributo para cada coluna no cabeçalho.")
        self.cabecalho = cabecalho
        self.chaves_dict = chaves_dict

    def criar_listagem(self, larguras_colunas: list[int] = None):
        """
        Cria o treeview da listagem.
        
        Args:
            larguras_colunas (list[int], optional): Larguras para cada coluna do treeview. 
                Deve ter o mesmo tamanho que self.cabecalho.
                Se None, usa larguras padrão.
        """
        self.tvw_tabela = ttk.Treeview(
            self, height=self.linhas_treeview, columns=self.cabecalho, show='headings'
        )

        for idx, coluna in enumerate(self.cabecalho):
            self.tvw_tabela.heading(coluna, text=coluna)
            self.tvw_tabela.column(coluna, anchor='center')

            # Define largura
            if larguras_colunas and idx < len(larguras_colunas):
                self.tvw_tabela.column(coluna, width=larguras_colunas[idx])
            else:
                self.tvw_tabela.column(coluna)

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

    def mostrar(self):
        # Atualiza os dados
        self.atualizar_listagem()

        # Mostra o componente na tela
        self.pack(expand=True, fill='both', anchor='center')
    
    ### Controller

    def dict_to_tuple(self, obj):
        """Mapeia os campos do dicionário para uma tupla"""
        return tuple(obj[campo] for campo in self.chaves_dict)

    def atualizar_listagem(self):
        # Apaga os itens da treeview
        self.tvw_tabela.delete(*self.tvw_tabela.get_children())

        # Atualiza a treeview com os dados do banco
        resp = self.controle.listar()
        tuplas = resp.retorno if resp.ok() else []

        for item in tuplas:
            # Obtém os valores das colunas correspondentes
            value = self.dict_to_tuple(item)
            self.tvw_tabela.insert('', 'end', values=value)
        
        # Ajusta largura das colunas automaticamente
        for idx, coluna in enumerate(self.cabecalho):
            max_largura = 25
            for item_id in self.tvw_tabela.get_children():
                valor = str(self.tvw_tabela.set(item_id, coluna))
                largura_valor = max(50, len(valor) * 7)  # ajuste simples: 7 pixels por caractere
                if largura_valor > max_largura:
                    max_largura = largura_valor
            self.tvw_tabela.column(coluna, width=max_largura)
    
    def adicionar(self):
        # Chama a tela de cadastro correspondente à entidade manipulada
        self.alterar_para_a_tela(f"cadastrar-{self.tipo_entidade}")
    
    def editar(self):
        """Edita o item selecionado"""
        item_selecionado = self.tvw_tabela.selection()[0]
        valores = self.tvw_tabela.item(item_selecionado, 'values')
        item = self.controle.buscar_por_id(valores[0]).retorno
        
        if item:
            self.gerenciador_de_janelas.editar(item, self.tipo_entidade)

    def excluir(self):
        """Exclui o item selecionado"""
        item_selecionado = self.tvw_tabela.selection()[0]
        valores = self.tvw_tabela.item(item_selecionado, 'values')
        
        if valores:
            # Confirma a exclusão
            resposta = messagebox.askyesno("Confirmar Exclusão", 
                                            f"Tem certeza que deseja excluir {(lambda e: f'{e[0]} {e[1]}')(self.get_descricao_entidade())} '{valores[1]}'?")

            if resposta:
                # Chama o controller para excluir
                resp = self.controle.excluir(valores[0])
                if resp.ok():
                    # Remove o item da treeview
                    self.tvw_tabela.delete(item_selecionado)
                    messagebox.showinfo(title="Sucesso",
                                        message=(f"{(lambda e: f'{e[1].capitalize()} excluíd{e[0]}')(self.get_descricao_entidade())}"
                                                 " com sucesso!"))
                else:
                    messagebox.showerror(title="Erro", 
                                         message=f"Erro ao excluir {(lambda e: f'{e[0]} {e[1]}')(self.get_descricao_entidade())}!",
                                         detail = "{}".format("\n".join(resp.erros)))
