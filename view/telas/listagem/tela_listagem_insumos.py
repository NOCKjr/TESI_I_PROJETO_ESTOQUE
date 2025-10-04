import tkinter as tk
from tkinter import ttk, messagebox
import constants

from control.insumo_controller import InsumoController
from control.medida_controller import MedidaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.listagem.tela_listagem_base import TelaListagemBase
from view.telas.menus.menu_painel_de_opcoes_crud import MenuPainelDeOpcoesCRUD

class TelaListagemInsumos(TelaListagemBase):
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, gerenciador_de_janelas, constants.ENTIDADE_INSUMO, InsumoController(), ['ID', 'NOME', 'ESTOQUE', 'MÉDIA CONSUMIDA', 'UNIDADE'], ['id', 'nome', 'quantidade_estoque', 'media_consumida', 'medida_id'])

        # Controlador de unidade de medida
        self.controle_unidade_medida = MedidaController()

    # Sobrescreve a função, pois uma das colunas tem tratamento diferente
    def atualizar_listagem(self):
        self.atualizar_listagem_insumos()
    
    def atualizar_listagem_insumos(self):
        # Apaga os itens da treeview
        self.tvw_tabela.delete(*self.tvw_tabela.get_children())

        # Atualiza a treeview com os dados do banco
        resp = self.controle.listar()
        tuplas = resp.retorno if resp.ok else []
        for item in tuplas:
            value = (
                item["id"],
                item["nome"],
                item["quantidade_estoque"],
                item["media_consumida"],
                self.controle_unidade_medida.buscar_medida(item["medida_id"])["unidade"],
            )
            self.tvw_tabela.insert('', 'end', values=value)
