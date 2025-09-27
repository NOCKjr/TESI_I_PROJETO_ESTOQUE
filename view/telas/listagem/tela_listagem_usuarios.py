import tkinter as tk
from tkinter import ttk, messagebox
import constants

from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.menus.menu_painel_de_opcoes_crud import MenuPainelDeOpcoesCRUD
from view.telas.tela_interface import TelaInterface
from control.usuario_controller import UsuarioController

class TelaListagemUsuarios(TelaInterface):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura, bg='#ffffff')

        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas

        # Controlador de usuários
        self.controle_usuarios = UsuarioController()

        ### Logo
        self.lbl_sigeme = tk.Label(self, text='SIGEME', bg=self.cores['branco'])
        self.lbl_sigeme.pack(side='top')

        ### Voltar ao menu
        self.btn_logoff = tk.Button(self, text="Voltar", command=lambda: self.alterar_para_a_tela(constants.TELA_CONSULTAS))
        self.btn_logoff.place(anchor='ne', x=largura - 5, y=5)

        ### Painel de ações
        self.painel_de_acoes = MenuPainelDeOpcoesCRUD(self, self)
        self.painel_de_acoes.mostrar()

        # Criar e exibir a listagem de usuários
        self.criar_listagem_usuarios()

    def criar_listagem_usuarios(self):
        colunas = ['ID', 'LOGIN', 'SENHA', 'TIPO']
        self.tvw_usuarios = ttk.Treeview(self, height=5, columns=colunas, show='headings')
        tuplas = self.controle_usuarios.listar_usuario()

        self.tvw_usuarios.heading('ID', text='ID')
        self.tvw_usuarios.column('ID', width=20, anchor='center')

        self.tvw_usuarios.heading('LOGIN', text='LOGIN')
        self.tvw_usuarios.column('LOGIN', width=200, anchor='center')

        self.tvw_usuarios.heading('SENHA', text='SENHA')
        self.tvw_usuarios.column('SENHA', width=200, anchor='center')

        self.tvw_usuarios.heading('TIPO', text='TIPO')
        self.tvw_usuarios.column('TIPO', width=20, anchor='center')

        for item in tuplas:
            self.tvw_usuarios.insert('', 'end', values=item)
        
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
    
    def atualizar_listagem_usuarios(self):
        # Apaga os itens da treeview
        self.tvw_usuarios.delete(*self.tvw_usuarios.get_children())

        # Atualiza a treeview com os dados do banco
        tuplas = self.controle_usuarios.listar_usuario()
        for item in tuplas:
            self.tvw_usuarios.insert('', 'end', values=item)

    def criar_menu_contexto(self):
        """Cria o menu de contexto com opções de editar e excluir"""
        self.menu_contexto = tk.Menu(self, tearoff=0)
        self.menu_contexto.add_command(label="Editar", command=self.editar_usuario)
        self.menu_contexto.add_command(label="Excluir", command=self.excluir_usuario)

    def abrir_menu_contexto(self, event):
        """Abre o menu de contexto quando clica com botão direito"""
        # Seleciona o item clicado
        item = self.tvw_usuarios.identify_row(event.y)
        if item:
            self.tvw_usuarios.selection_set(item)
            self.tvw_usuarios.focus(item)
            # Mostra o menu de contexto na posição do mouse
            self.menu_contexto.post(event.x_root, event.y_root)

    def editar_usuario(self):
        """Edita o usuário selecionado"""
        item_selecionado = self.tvw_usuarios.selection()[0]
        valores = self.tvw_usuarios.item(item_selecionado, 'values')
        
        if valores:
            self.gerenciador_de_janelas.editar_usuario(valores)
            
            # Aqui você pode implementar uma janela de edição ou navegar para uma tela de edição
            print(f"Editando usuário: ID={valores[0]}, LOGIN={valores[1]}")
            # Por enquanto, apenas mostra uma mensagem
            # tk.messagebox.showinfo("Editar", f"Função de edição será implementada para o usuário: {valores[1]}")

    def excluir_usuario(self):
        """Exclui o usuário selecionado"""
        item_selecionado = self.tvw_usuarios.selection()[0]
        valores = self.tvw_usuarios.item(item_selecionado, 'values')
        
        if valores:
            # Confirma a exclusão
            resposta = tk.messagebox.askyesno("Confirmar Exclusão", 
                                            f"Tem certeza que deseja excluir o usuário '{valores[1]}'?")
            if resposta:
                # Chama o controller para excluir
                resultado = self.controle_usuarios.excluir_usuario(valores[0])
                if resultado:
                    # Remove o item da treeview
                    self.tvw_usuarios.delete(item_selecionado)
                    tk.messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
                else:
                    tk.messagebox.showerror("Erro", "Erro ao excluir o usuário!")

    def mostrar(self):
        # Atualiza os dados
        self.atualizar_listagem_usuarios()

        # Mostra o componente na tela
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        self.pack_forget()
    
    def alterar_para_a_tela(self, tela):
        self.gerenciador_de_janelas.alterar_para_a_tela(tela)
    
    def adicionar(self):
        self.alterar_para_a_tela(constants.TELA_CADASTRAR_USUARIO)
    
    def editar(self):
        self.editar_usuario()
    
    def excluir(self):
        self.excluir_usuario()