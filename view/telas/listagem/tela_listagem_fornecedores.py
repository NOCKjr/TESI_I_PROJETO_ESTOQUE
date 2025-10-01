import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.fornecedor_controller import FornecedorController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.menus.menu_painel_de_opcoes_crud import MenuPainelDeOpcoesCRUD
from view.telas.tela_base import TelaBase

class TelaListagemFornecedores(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)
        
        # Controlador de fornecedors
        self.controle_fornecedores = FornecedorController()

        ### Painel de ações
        self.painel_de_acoes = MenuPainelDeOpcoesCRUD(self, self)
        self.painel_de_acoes.mostrar()

        # Criar e exibir a listagem de fornecedors
        self.criar_listagem_fornecedores()

    def criar_listagem_fornecedores(self):
        colunas = ['ID', 'RAZÃO SOCIAL', 'CONTATO']
        self.tvw_fornecedores = ttk.Treeview(self, height=5, columns=colunas, show='headings')
        tuplas = self.controle_fornecedores.listar_fornecedor()

        self.tvw_fornecedores.heading('ID', text='ID')
        self.tvw_fornecedores.column('ID', width=20, anchor='center')

        self.tvw_fornecedores.heading('RAZÃO SOCIAL', text='RAZÃO SOCIAL')
        self.tvw_fornecedores.column('RAZÃO SOCIAL', width=200, anchor='center')

        self.tvw_fornecedores.heading('CONTATO', text='CONTATO')
        self.tvw_fornecedores.column('CONTATO', width=200, anchor='center')
        
        # Insere os fornecedores no treeview
        self.atualizar_listagem_fornecedores()
        
        # Bind do botão direito para abrir o menu de contexto
        self.tvw_fornecedores.bind("<Button-3>", self.abrir_menu_contexto)

        self.tvw_fornecedores.bind("<<TreeviewSelect>>", self.item_selecionado)
        
        self.tvw_fornecedores.pack(pady=17, padx=10, fill='x', expand=False)

        # Criar menu de contexto
        self.criar_menu_contexto()
    
    def item_selecionado(self, event):
        selecao = self.tvw_fornecedores.selection()

        # Só edita/exclui se houver apenas uma opção selecionada
        # [adicionar selectmode="browse" no treeview pode ser uma opção]
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
    
    def atualizar_listagem_fornecedores(self):
        """Atualiza o treeview com os fornecedores cadastrados"""
        # Apaga os itens da treeview
        self.tvw_fornecedores.delete(*self.tvw_fornecedores.get_children())

        # Atualiza a treeview com os dados do banco
        fornecedores = self.controle_fornecedores.listar_fornecedor()
        for fornecedor in fornecedores:
            item = (
                fornecedor["id"],
                fornecedor["razao_social"],
                fornecedor["contato"],
            )
            self.tvw_fornecedores.insert('', 'end', values=item)

    def criar_menu_contexto(self):
        """Cria o menu de contexto com opções de editar e excluir"""
        self.menu_contexto = tk.Menu(self, tearoff=0)
        self.menu_contexto.add_command(label="Editar", command=self.editar_fornecedor)
        self.menu_contexto.add_command(label="Excluir", command=self.excluir_fornecedor)

    def abrir_menu_contexto(self, event):
        """Abre o menu de contexto quando clica com botão direito"""
        # Seleciona o item clicado
        item = self.tvw_fornecedores.identify_row(event.y)
        if item:
            self.tvw_fornecedores.selection_set(item)
            self.tvw_fornecedores.focus(item)
            # Mostra o menu de contexto na posição do mouse
            self.menu_contexto.post(event.x_root, event.y_root)

    def editar_fornecedor(self):
        """Edita o fornecedor selecionado"""
        item_selecionado = self.tvw_fornecedores.selection()[0]
        valores = self.tvw_fornecedores.item(item_selecionado, 'values')
        
        if valores:
            self.gerenciador_de_janelas.editar_fornecedor(valores)
            
            # Aqui você pode implementar uma janela de edição ou navegar para uma tela de edição
            print(f"Editando fornecedor: ID={valores[0]}, RAZÃO SOCIAL={valores[1]}")

    def excluir_fornecedor(self):
        """Exclui o fornecedor selecionado"""
        item_selecionado = self.tvw_fornecedores.selection()[0]
        valores = self.tvw_fornecedores.item(item_selecionado, 'values')
        
        if valores:
            # Confirma a exclusão
            resposta = tk.messagebox.askyesno("Confirmar Exclusão", 
                                            f"Tem certeza que deseja excluir o fornecedor '{valores[1]}'?")
            if resposta:
                # Chama o controller para excluir
                resultado = self.controle_fornecedores.excluir_fornecedor(valores[0])
                if resultado:
                    # Remove o item da treeview
                    self.tvw_fornecedores.delete(item_selecionado)
                    tk.messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
                else:
                    tk.messagebox.showerror("Erro", "Erro ao excluir o fornecedor!")

    def mostrar(self):
        # Atualiza os dados
        self.atualizar_listagem_fornecedores()

        # Mostra o componente na tela
        self.pack(expand=True, fill='both', anchor='center')
    
    def adicionar(self):
        self.alterar_para_a_tela(constants.TELA_CADASTRAR_FORNECEDOR)
    
    def editar(self):
        self.editar_fornecedor()
    
    def excluir(self):
        self.excluir_fornecedor()