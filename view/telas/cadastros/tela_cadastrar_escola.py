import tkinter as tk
import constants

from tkinter import ttk
from control.endereco_controller import EnderecoController
from control.escola_controller import EscolaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.tela_formulario_base import TelaFormularioBase

class TelaCadastrarEscola(TelaFormularioBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, modo_editar=False, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, modo_editar)

        # Se o formulário foi aberto como edição, define-se o id da escola editado
        self.id_escola_editado = None

        # Controlador de escolas
        self.controle_escolas = EscolaController()
        self.controle_endereco = EnderecoController()
        
        ## Escola
        
        # Nome
        self.lbl_nome = tk.Label(self.container_formulario, text="Nome da escola:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_nome.grid(row=1, column=0, pady=(0,0), sticky='nsw')
        self.ent_nome = tk.Entry(self.container_formulario)
        self.ent_nome.grid(row=2, column=0, columnspan=30, sticky='nsew')
        # Número de alunos
        self.lbl_numero_alunos = tk.Label(self.container_formulario, text="Número de Alunos:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_numero_alunos.grid(row=3, column=0, pady=(2,0), sticky='nsw')
        self.ent_numero_alunos = tk.Entry(self.container_formulario)
        self.ent_numero_alunos.grid(row=4, column=0, columnspan=4, sticky='nsew')
        
        ## Endereço

        # Logradouro
        self.lbl_logradouro = tk.Label(self.container_formulario, text="Logradouro:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_logradouro.grid(row=7, column=0, pady=(2,0), sticky='nsw')
        self.ent_logradouro = tk.Entry(self.container_formulario)
        self.ent_logradouro.grid(row=8, column=0, columnspan=30, sticky='nsew')
        # Bairro
        self.lbl_bairro = tk.Label(self.container_formulario, text="Bairro:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_bairro.grid(row=11, column=0, pady=(2,0), sticky='nsw')
        self.ent_bairro = tk.Entry(self.container_formulario)
        self.ent_bairro.grid(row=12, column=0, columnspan=26, sticky='nsew')
        # Número
        self.lbl_numero = tk.Label(self.container_formulario, text="Número:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_numero.grid(row=11, column=26, pady=(2,0), sticky='nsw')
        self.ent_numero = tk.Entry(self.container_formulario)
        self.ent_numero.grid(row=12, column=26, columnspan=4, sticky='nsew')
        # Estado
        self.lbl_estado = tk.Label(self.container_formulario, text="Estado:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_estado.grid(row=15, column=0, pady=(2,0), sticky='nsw')
        self.ent_estado = tk.Entry(self.container_formulario)
        self.ent_estado.grid(row=16, column=0, columnspan=20, sticky='nsew')
        # CEP
        self.lbl_cep = tk.Label(self.container_formulario, text="CEP:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_cep.grid(row=15, column=20, pady=(2,0), sticky='nsw')
        self.ent_cep = tk.Entry(self.container_formulario)
        self.ent_cep.grid(row=16, column=20, columnspan=10, sticky='nsew')

    def onConfirmar(self):
        # Captura os valores dos campos
        nome = self.ent_nome.get()
        alunos = self.ent_numero_alunos.get()
        campos_endereco = self.obter_campos_endereco()

        if self.flag_editar:
            # A escola já existe e já possui um endereço
            id_escola = self.id_escola_editado
            escola = self.controle_escolas.buscar_escola_por_id(id_escola)
            endereco_id = escola["endereco_id"]
            novo_endereco = (endereco_id, ) + campos_endereco

            # Atualiza o endereço
            self.controle_endereco.atualizar_endereco(*novo_endereco)

            # Chama o controller para atualizar a escola
            self.controle_escolas.atualizar_escola(id=id_escola, nome=nome, endereco_id=endereco_id, numero_alunos=alunos)
        else:
            # Chama o controller para inserir novo endereço
            endereco_id = self.controle_endereco.inserir_endereco(*campos_endereco)
            # Chama o controller para inserir nova escola
            escola_id = self.controle_escolas.inserir_escola(nome=nome, endereco_id=endereco_id, numero_alunos=alunos)
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()

        # Volta para a tela de listagem
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_ESCOLAS)

    def onCancelar(self):
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()

        # Volta para a tela de listagem
        self.gerenciador_de_janelas.alterar_para_a_tela(constants.TELA_LISTAGEM_ESCOLAS)

    def limpar_campos(self):
        self.ent_nome.delete(0, 'end')
        self.ent_logradouro.delete(0, 'end')
        self.ent_bairro.delete(0, 'end')
        self.ent_numero.delete(0, 'end')
        self.ent_estado.delete(0, 'end')
        self.ent_cep.delete(0, 'end')
        self.ent_numero_alunos.delete(0, 'end')
        self.flag_editar = False

    def editar_escola(self, escola):
        self.ent_nome.delete(0, 'end')
        self.ent_nome.insert(0, escola['nome'])
        self.ent_numero_alunos.delete(0, 'end')
        self.ent_numero_alunos.insert(0, escola['numero_alunos'])
        self.id_escola_editado = escola['id']
        self.preencher_campos_endereco(escola["endereco_id"])
        self.flag_editar = True
    
    def preencher_campos_endereco(self, endereco_id):
        endereco = self.controle_endereco.buscar_endereco_por_id(endereco_id)
        self.ent_logradouro.delete(0, 'end')
        self.ent_logradouro.insert(0, endereco['logradouro'])
        self.ent_numero.delete(0, 'end')
        self.ent_numero.insert(0, endereco['numero'])
        self.ent_bairro.delete(0, 'end')
        self.ent_bairro.insert(0, endereco['bairro'])
        self.ent_estado.delete(0, 'end')
        self.ent_estado.insert(0, endereco['estado'])
        self.ent_cep.delete(0, 'end')
        self.ent_cep.insert(0, endereco['cep'])
    
    def obter_campos_endereco(self) -> tuple:
        """
        Obtém os valores digitados nos campos do formulário de endereço e retorna em uma tupla.

        Returns:
            tuple: (logradouro, numero, bairro, cidade, estado, cep, complemento, ponto_referencia)
        """
        logradouro = self.ent_logradouro.get()
        numero = self.ent_numero.get()
        bairro = self.ent_bairro.get()
        estado = self.ent_estado.get()
        cep = self.ent_cep.get()

        # TO-DO: adicionar ao formulário os seguintes campos
        cidade = ''
        complemento = ''
        ponto_referencia = ''

        return (logradouro, numero, bairro, cidade, estado, cep, complemento, ponto_referencia)
