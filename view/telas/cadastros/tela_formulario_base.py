import tkinter as tk
import constants

from tkinter import ttk
from control.controller_base import ControllerBase
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_base import TelaBase

class TelaFormularioBase(TelaBase):
    def __init__(self, master, 
                       gerenciador_de_janelas: GerenciadorDeJanelasBase, 
                       tipo_entidade: str, 
                       controle_entidade: ControllerBase, 
                       modo_editar=False, 
                       largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, largura, altura)

        # Tipo da entidade manipulada
        self.tipo_entidade = tipo_entidade

        # Controlador da entidade
        self.controle = controle_entidade

        # Para saber se o formulário foi aberto para inserir ou editar
        self.flag_editar = modo_editar

        # ID do item para quando a tela está no modo de edição
        self.id_para_edicao = None

        # Largura do formulário em colunas
        self.numero_colunas_formulario = 30
        
        ### Container com o formulário de cadastro
        self.container_formulario = tk.Frame(self, bg=constants.cores['cinza'], padx=10, pady=10)
        self.container_formulario.place(anchor='center', relx=0.5, rely=0.5)

        for c in range(self.numero_colunas_formulario):
            self.container_formulario.columnconfigure(c, minsize=10)
    
    def criar_campos_formulario(self):
        ### Botões Confirmar e Cancelar
        self.btn_confirmar = tk.Button(self.container_formulario, text="Confirmar", bg=constants.cores['verde'], command=self.onConfirmar)
        self.btn_confirmar.grid(row=60, column=0, sticky='nswe', pady=(10,0))

        self.btn_cancelar = tk.Button(self.container_formulario, text="Cancelar", bg=constants.cores['vermelho'], command=self.onCancelar)
        self.btn_cancelar.grid(row=60, column=2, columnspan=10, sticky='nswe', pady=(10,0))

    def ir_para_tela_de_listagem(self):
        self.gerenciador_de_janelas.alterar_para_a_tela(f'listagem-{self.tipo_entidade}')

    def get_campos_formulario(self, frame):
        """Retorna todos os widgets interativos de um frame (preenchíveis pelo usuário)."""
        tipos = (
            tk.Entry, ttk.Entry,
            tk.Text,
            tk.Spinbox, ttk.Spinbox,
            ttk.Combobox,
            tk.Checkbutton, ttk.Checkbutton,
            tk.Radiobutton, ttk.Radiobutton,
            tk.Scale, ttk.Scale,
            tk.OptionMenu, ttk.OptionMenu,
        )

        campos = []
        for w in frame.winfo_children():
            if isinstance(w, tipos):
                campos.append(w)
            # se quiser incluir widgets dentro de subframes:
            campos.extend(self.get_campos_formulario(w))
        return campos
    
    def limpar_campos(self):
        """Limpa todos os campos preenchíveis do formulário"""

        self.flag_editar = False
        
        for campo in self.get_campos_formulario(self.container_formulario):
            # Entry e ttk.Entry
            if isinstance(campo, (tk.Entry, ttk.Entry)):
                campo.delete(0, tk.END)

            # Text (multilinha)
            elif isinstance(campo, tk.Text):
                campo.delete("1.0", tk.END)

            # Combobox
            elif isinstance(campo, ttk.Combobox):
                campo.set('')

            # Spinbox
            elif isinstance(campo, (tk.Spinbox, ttk.Spinbox)):
                try:
                    campo.delete(0, tk.END)
                    campo.insert(0, campo.cget("from"))  # opcional: volta pro valor mínimo
                except Exception:
                    campo.delete(0, tk.END)

            # Checkbutton
            elif isinstance(campo, (tk.Checkbutton, ttk.Checkbutton)):
                var = campo.cget('variable')
                if var:
                    campo._root().setvar(var, 0)

            # Radiobutton
            elif isinstance(campo, (tk.Radiobutton, ttk.Radiobutton)):
                var = campo.cget('variable')
                if var:
                    campo._root().setvar(var, '')

            # Scale
            elif isinstance(campo, (tk.Scale, ttk.Scale)):
                campo.set(campo.cget('from'))

            # OptionMenu
            elif isinstance(campo, (tk.OptionMenu, ttk.OptionMenu)):
                var = campo.cget('textvariable')
                if var:
                    campo._root().setvar(var, '')

    def set_flag_edicao(self, valor_flag=True):
        self.flag_editar = valor_flag

    def set_id_usuario_edicao(self, valor_id=None):
        self.id_para_edicao = valor_id
    
    def obter_valores_campos_formulario(self):
        return ()
    
    def onConfirmar(self):
        args = self.obter_valores_campos_formulario()
        
        if self.flag_editar:
            args = (self.id_para_edicao,) + args
            self.controle.atualizar(*args)
        else:
            self.controle.inserir(*args)
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()
        
        # Volta para a tela de listagem
        self.ir_para_tela_de_listagem()

    def onCancelar(self):
        self.limpar_campos()
        self.ir_para_tela_de_listagem()
