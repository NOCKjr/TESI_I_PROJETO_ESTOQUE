import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.insumo_controller import InsumoController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.menus.menu_painel_de_opcoes_crud import MenuPainelDeOpcoesCRUD
from view.telas.tela_base import TelaBase

class TelaListagemInsumos(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)
        
        # Controlador de insumos
        self.controle_insumos = InsumoController()

        ### Painel de ações
        self.painel_de_acoes = MenuPainelDeOpcoesCRUD(self, self)
        self.painel_de_acoes.mostrar()

        # Criar e exibir a listagem de insumos
        self.criar_listagem_insumos()

    def criar_listagem_insumos(self):
        colunas = ['ID', 'NOME', 'ESTOQUE', 'MÉDIA CONSUMIDA', 'UNIDADE']
        self.tvw_insumos = ttk.Treeview(self, height=5, columns=colunas, show='headings')
        tuplas = self.controle_insumos.listar_insumo()

        self.tvw_insumos.heading('ID', text='ID')
        self.tvw_insumos.column('ID', width=10, anchor='center')

        self.tvw_insumos.heading('NOME', text='NOME')
        self.tvw_insumos.column('NOME', width=70, anchor='center')

        self.tvw_insumos.heading('ESTOQUE', text='ESTOQUE')
        self.tvw_insumos.column('ESTOQUE', width=10, anchor='center')

        self.tvw_insumos.heading('MÉDIA CONSUMIDA', text='MÉDIA CONSUMIDA')
        self.tvw_insumos.column('MÉDIA CONSUMIDA', width=40, anchor='center')

        self.tvw_insumos.heading('UNIDADE', text='UNIDADE')
        self.tvw_insumos.column('UNIDADE', width=20, anchor='center')

        for item in tuplas:
            self.tvw_insumos.insert('', 'end', values=item)
        
        # Bind do botão direito para abrir o menu de contexto
        self.tvw_insumos.bind("<Button-3>", self.abrir_menu_contexto)

        self.tvw_insumos.bind("<<TreeviewSelect>>", self.item_selecionado)

        self.tvw_insumos.pack(pady=17, padx=10, fill='x', expand=False)

        # Criar menu de contexto
        self.criar_menu_contexto()
    
    def item_selecionado(self, event):
        selecao = self.tvw_insumos.selection()

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
    
    def atualizar_listagem_insumos(self):
        # Apaga os itens da treeview
        self.tvw_insumos.delete(*self.tvw_insumos.get_children())

        # Atualiza a treeview com os dados do banco
        tuplas = self.controle_insumos.listar_insumo()
        for item in tuplas:
            self.tvw_insumos.insert('', 'end', values=item)

    def criar_menu_contexto(self):
        """Cria o menu de contexto com opções de editar e excluir"""
        self.menu_contexto = tk.Menu(self, tearoff=0)
        self.menu_contexto.add_command(label="Editar", command=self.editar_insumo)
        self.menu_contexto.add_command(label="Excluir", command=self.excluir_insumo)

    def abrir_menu_contexto(self, event):
        """Abre o menu de contexto quando clica com botão direito"""
        # Seleciona o item clicado
        item = self.tvw_insumos.identify_row(event.y)
        if item:
            self.tvw_insumos.selection_set(item)
            self.tvw_insumos.focus(item)
            # Mostra o menu de contexto na posição do mouse
            self.menu_contexto.post(event.x_root, event.y_root)

    def editar_insumo(self):
        """Edita o insumo selecionado"""
        item_selecionado = self.tvw_insumos.selection()[0]
        valores = self.tvw_insumos.item(item_selecionado, 'values')
        
        if valores:
            self.gerenciador_de_janelas.editar_insumo(valores)
            
            # Aqui você pode implementar uma janela de edição ou navegar para uma tela de edição
            print(f"Editando insumo: ID={valores[0]}, NOME={valores[1]}")

    def excluir_insumo(self):
        """Exclui o insumo selecionado"""
        item_selecionado = self.tvw_insumos.selection()[0]
        valores = self.tvw_insumos.item(item_selecionado, 'values')
        
        if valores:
            # Confirma a exclusão
            resposta = tk.messagebox.askyesno("Confirmar Exclusão", 
                                            f"Tem certeza que deseja excluir o insumo '{valores[1]}'?")
            if resposta:
                # Chama o controller para excluir
                resultado = self.controle_insumos.excluir_insumo(valores[0])
                if resultado:
                    # Remove o item da treeview
                    self.tvw_insumos.delete(item_selecionado)
                    tk.messagebox.showinfo("Sucesso", "Insumo excluído com sucesso!")
                else:
                    tk.messagebox.showerror("Erro", "Erro ao excluir o insumo!")

    def mostrar(self):
        # Atualiza os dados
        self.atualizar_listagem_insumos()

        # Mostra o componente na tela
        self.pack(expand=True, fill='both', anchor='center')
    
    def adicionar(self):
        self.alterar_para_a_tela(constants.TELA_CADASTRAR_INSUMO)
    
    def editar(self):
        self.editar_insumo()
    
    def excluir(self):
        self.excluir_insumo()