import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.endereco_controller import EnderecoController
from control.escola_controller import EscolaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.menus.menu_painel_de_opcoes_crud import MenuPainelDeOpcoesCRUD
from view.telas.tela_base import TelaBase

class TelaListagemEscolas(TelaBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas)
        
        # Controlador de usuários
        self.controle_escolas = EscolaController()
        self.controle_endereco = EnderecoController()

        ### Painel de ações
        self.painel_de_acoes = MenuPainelDeOpcoesCRUD(self, self)
        self.painel_de_acoes.mostrar()

        # Criar e exibir a listagem de usuários
        self.criar_listagem_escolas()

    def criar_listagem_escolas(self):
        colunas = ['ID', 'NOME', 'ENDEREÇO', 'ALUNOS']
        self.tvw_usuarios = ttk.Treeview(self, height=5, columns=colunas, show='headings')
        tuplas = self.controle_escolas.listar_escola()

        self.tvw_usuarios.heading('ID', text='ID')
        self.tvw_usuarios.column('ID', width=10, anchor='center')

        self.tvw_usuarios.heading('NOME', text='NOME')
        self.tvw_usuarios.column('NOME', width=150, anchor='center')

        self.tvw_usuarios.heading('ENDEREÇO', text='ENDEREÇO')
        self.tvw_usuarios.column('ENDEREÇO', width=200, anchor='center')

        self.tvw_usuarios.heading('ALUNOS', text='ALUNOS')
        self.tvw_usuarios.column('ALUNOS', width=20, anchor='center')

        # Insere os itens no treeview
        self.atualizar_listagem_escolas()
        
        # Bind do botão direito para abrir o menu de contexto
        self.tvw_usuarios.bind("<Button-3>", self.abrir_menu_contexto)

        self.tvw_usuarios.bind("<<TreeviewSelect>>", self.item_selecionado)
        
        self.tvw_usuarios.pack(pady=17, padx=10, fill='x', expand=False)

        # Criar menu de contexto
        self.criar_menu_contexto()
    
    def item_selecionado(self, event):
        selecao = self.tvw_usuarios.selection()

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
    
    def atualizar_listagem_escolas(self):
        """Atualiza o treeview com as escolas cadastradas"""
        # Apaga os itens da treeview
        self.tvw_usuarios.delete(*self.tvw_usuarios.get_children())

        # Atualiza a treeview com os dados do banco
        escolas = self.controle_escolas.listar_escola()
        for escola in escolas:
            item = (
                escola["id"],
                escola["nome"],
                self.controle_endereco.buscar_endereco_string(escola["endereco_id"]),
                escola["numero_alunos"],
            )
            self.tvw_usuarios.insert('', 'end', values=item)

    def criar_menu_contexto(self):
        """Cria o menu de contexto com opções de editar e excluir"""
        self.menu_contexto = tk.Menu(self, tearoff=0)
        self.menu_contexto.add_command(label="Editar", command=self.editar_escola)
        self.menu_contexto.add_command(label="Excluir", command=self.excluir_escola)

    def abrir_menu_contexto(self, event):
        """Abre o menu de contexto quando clica com botão direito"""
        # Seleciona o item clicado
        item = self.tvw_usuarios.identify_row(event.y)
        if item:
            self.tvw_usuarios.selection_set(item)
            self.tvw_usuarios.focus(item)
            # Mostra o menu de contexto na posição do mouse
            self.menu_contexto.post(event.x_root, event.y_root)

    def editar_escola(self):
        """Edita a escola selecionada"""
        item_selecionado = self.tvw_usuarios.selection()[0]
        valores = self.tvw_usuarios.item(item_selecionado, 'values')
        escola = self.controle_escolas.buscar_escola_por_id(valores[0])
        
        if escola:
            self.gerenciador_de_janelas.editar_escola(escola)

    def excluir_escola(self):
        """Exclui a escola selecionada"""
        item_selecionado = self.tvw_usuarios.selection()[0]
        valores = self.tvw_usuarios.item(item_selecionado, 'values')
        
        if valores:
            # Confirma a exclusão
            resposta = tk.messagebox.askyesno("Confirmar Exclusão", 
                                            f"Tem certeza que deseja excluir a escola '{valores[1]}'?")
            if resposta:
                # Chama o controller para excluir
                resultado = self.controle_escolas.excluir_escola(valores[0])
                if resultado:
                    # Remove o item da treeview
                    self.tvw_usuarios.delete(item_selecionado)
                    tk.messagebox.showinfo("Sucesso", "Escola excluída com sucesso!")
                else:
                    tk.messagebox.showerror("Erro", "Erro ao excluir a escola!")

    def mostrar(self):
        # Atualiza os dados
        self.atualizar_listagem_escolas()

        # Mostra o componente na tela
        self.pack(expand=True, fill='both', anchor='center')
    
    def adicionar(self):
        self.alterar_para_a_tela(constants.TELA_CADASTRAR_ESCOLA)
    
    def editar(self):
        self.editar_escola()
    
    def excluir(self):
        self.excluir_escola()