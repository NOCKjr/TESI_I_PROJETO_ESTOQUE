import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.endereco_controller import EnderecoController
from control.escola_controller import EscolaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.listagem.tela_listagem_base import TelaListagemBase

class TelaListagemEscolas(TelaListagemBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, constants.ENTIDADE_ESCOLA, EscolaController(), ['ID', 'NOME', 'ENDEREÇO', 'ALUNOS'], ['id', 'nome', 'endereco_id', 'numero_alunos'])
        
        # Controlador de endereço
        self.controle_endereco = EnderecoController()

    # Sobrescreve a função, pois uma das colunas tem tratamento diferente
    def atualizar_listagem(self):
        self.atualizar_listagem_escolas()
    
    def atualizar_listagem_escolas(self):
        """Atualiza o treeview com as escolas cadastradas"""
        # Apaga os itens da treeview
        self.tvw_tabela.delete(*self.tvw_tabela.get_children())

        # Atualiza a treeview com os dados do banco
        resp = self.controle.listar()
        tuplas = resp.retorno if resp.ok() else []
        for item in tuplas:
            value = (
                item["id"],
                item["nome"],
                self.controle_endereco.buscar_endereco_string(item["endereco_id"]),
                item["numero_alunos"],
            )
            self.tvw_tabela.insert('', 'end', values=value)
