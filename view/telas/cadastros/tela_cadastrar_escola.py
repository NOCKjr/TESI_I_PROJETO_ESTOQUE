import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import constants

from control.endereco_controller import EnderecoController
from control.escola_controller import EscolaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.cadastros.tela_formulario_base import TelaFormularioBase

class TelaCadastrarEscola(TelaFormularioBase):
    def __init__(self, master, 
                       gerenciador_de_janelas: GerenciadorDeJanelasBase, 
                       modo_editar=False, 
                       largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, 
                         gerenciador_de_janelas, 
                         constants.ENTIDADE_ESCOLA, 
                         EscolaController(), 
                         modo_editar,
                         largura, altura)

        # Cotrnoles
        self.controle_endereco = EnderecoController()

        self.criar_campos_formulario()
    
    def criar_campos_formulario(self):
        super().criar_campos_formulario()
        
        ## Escola
        
        # Nome
        self.lbl_nome = ttk.Label(self.container_formulario, text="Nome da escola:", anchor='w')
        self.lbl_nome.grid(row=1, column=0, pady=(0,0), sticky='nsw')
        self.ent_nome = ttk.Entry(self.container_formulario)
        self.ent_nome.grid(row=2, column=0, columnspan=30, sticky='nsew')
        # Número de alunos
        self.lbl_numero_alunos = ttk.Label(self.container_formulario, text="Número de Alunos:", anchor='w')
        self.lbl_numero_alunos.grid(row=3, column=0, pady=(2,0), sticky='nsw')
        self.ent_numero_alunos = ttk.Entry(self.container_formulario)
        self.ent_numero_alunos.grid(row=4, column=0, columnspan=4, sticky='nsew')
        
        ## Endereço

        # Logradouro
        self.lbl_logradouro = ttk.Label(self.container_formulario, text="Logradouro:", anchor='w')
        self.lbl_logradouro.grid(row=7, column=0, pady=(2,0), sticky='nsw')
        self.ent_logradouro = ttk.Entry(self.container_formulario)
        self.ent_logradouro.grid(row=8, column=0, columnspan=30, sticky='nsew')
        # Bairro
        self.lbl_bairro = ttk.Label(self.container_formulario, text="Bairro:", anchor='w')
        self.lbl_bairro.grid(row=11, column=0, pady=(2,0), sticky='nsw')
        self.ent_bairro = ttk.Entry(self.container_formulario)
        self.ent_bairro.grid(row=12, column=0, columnspan=26, sticky='nsew')
        # Número
        self.lbl_numero = ttk.Label(self.container_formulario, text="Número:", anchor='w')
        self.lbl_numero.grid(row=11, column=26, pady=(2,0), sticky='nsw')
        self.ent_numero = ttk.Entry(self.container_formulario)
        self.ent_numero.grid(row=12, column=26, columnspan=4, sticky='nsew')
        # Cidade
        self.lbl_cidade = ttk.Label(self.container_formulario, text="Cidade:", anchor='w')
        self.lbl_cidade.grid(row=15, column=0, pady=(2,0), sticky='nsw')
        self.ent_cidade = ttk.Entry(self.container_formulario)
        self.ent_cidade.grid(row=16, column=0, columnspan=14, sticky='nsew')
        # Estado
        self.lbl_estado = ttk.Label(self.container_formulario, text="Estado:", anchor='w')
        self.lbl_estado.grid(row=15, column=14, pady=(2,0), sticky='nsw')
        self.ent_estado = ttk.Entry(self.container_formulario)
        self.ent_estado.grid(row=16, column=14, columnspan=6, sticky='nsew')
        # CEP
        self.lbl_cep = ttk.Label(self.container_formulario, text="CEP:", anchor='w')
        self.lbl_cep.grid(row=15, column=20, pady=(2,0), sticky='nsw')
        self.ent_cep = ttk.Entry(self.container_formulario)
        self.ent_cep.grid(row=16, column=20, columnspan=10, sticky='nsew')

    def editar_escola(self, escola):
        self.ent_nome.delete(0, 'end')
        self.ent_nome.insert(0, escola['nome'])
        self.ent_numero_alunos.delete(0, 'end')
        self.ent_numero_alunos.insert(0, escola['numero_alunos'])
        self.id_para_edicao = escola['id']
        self.preencher_campos_endereco(escola["endereco_id"])
        self.flag_editar = True

    def obter_valores_campos_formulario(self):
        # Captura os valores dos campos
        nome = self.ent_nome.get()
        alunos = self.ent_numero_alunos.get()
        campos_endereco = self.obter_campos_endereco()
        
        return (nome, alunos, campos_endereco)
    
    def onConfirmar(self):
        nome, alunos, campos_endereco = self.obter_valores_campos_formulario()

        if self.flag_editar:
            # A escola já existe e já possui um endereço
            escola = self.controle.buscar_por_id(self.id_para_edicao).retorno
            endereco_id = escola["endereco_id"]
            novo_endereco = (endereco_id, ) + campos_endereco

            # Atualiza o endereço
            self.controle_endereco.atualizar(*novo_endereco)

            # Atualiza a escola
            self.controle.atualizar(self.id_para_edicao, nome, endereco_id, alunos)
        else:
            # Chama o controller para inserir novo endereço
            endereco_id = self.controle_endereco.inserir(*campos_endereco).retorno
            self.controle.inserir(nome, endereco_id, alunos)
        
        # Reseta os valores dos campos do formulário
        self.limpar_campos()

        # Volta para a tela de listagem
        self.ir_para_tela_de_listagem()
    
    def preencher_campos_endereco(self, endereco_id):
        resposta = self.controle_endereco.buscar_endereco_por_id(endereco_id)

        endereco = resposta.retorno
        self.ent_logradouro.delete(0, 'end')
        self.ent_logradouro.insert(0, endereco['logradouro'])
        self.ent_numero.delete(0, 'end')
        self.ent_numero.insert(0, endereco['numero'])
        self.ent_bairro.delete(0, 'end')
        self.ent_bairro.insert(0, endereco['bairro'])
        self.ent_cidade.delete(0, 'end')
        self.ent_cidade.insert(0, endereco['cidade'])
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
        cidade = self.ent_cidade.get()
        estado = self.ent_estado.get()
        cep = self.ent_cep.get()

        # TO-DO: adicionar ao formulário os seguintes campos
        complemento = ''
        ponto_referencia = ''

        return (logradouro, numero, bairro, cidade, estado, cep, complemento, ponto_referencia)
