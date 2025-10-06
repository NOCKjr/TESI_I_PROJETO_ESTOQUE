import tkinter as tk
import constants

from tkinter import ttk
from control.insumo_controller import InsumoController
from control.medida_controller import MedidaController
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase
from view.telas.cadastros.tela_formulario_base import TelaFormularioBase

class TelaCadastrarInsumo(TelaFormularioBase):
    def __init__(self, master, 
                       gerenciador_de_janelas: GerenciadorDeJanelasBase, 
                       modo_editar=False, 
                       largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, 
                         gerenciador_de_janelas, 
                         constants.ENTIDADE_INSUMO, 
                         InsumoController(), 
                         modo_editar,
                         largura, altura)

        # Controles
        self.controle_medidas = MedidaController()

        # Rótulos para os valores na coluna de medida
        # self.rotulos_de_medidas = ["Quilograma", "Miligrama", "Litros"]
        self.rotulos_de_medidas = [medida["unidade"] for medida in self.controle_medidas.listar().retorno]


        self.criar_campos_formulario()
    
    def criar_campos_formulario(self):
        super().criar_campos_formulario()

        # Nome/descrição
        self.lbl_nome = tk.Label(self.container_formulario, text="Nome/descrição:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_nome.grid(row=1, column=0, pady=(0,0), sticky='nsw')
        self.ent_nome = tk.Entry(self.container_formulario)
        self.ent_nome.grid(row=2, column=0, columnspan=30, sticky='nsew')

        # Média de consumo
        self.lbl_media_consumo = tk.Label(self.container_formulario, text="Média de consumo/aluno por mês:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_media_consumo.grid(row=5, column=0, pady=(2,0), sticky='nsw')
        self.ent_media_consumo = tk.Entry(self.container_formulario)
        self.ent_media_consumo.grid(row=6, column=0, columnspan=5, sticky='nsew')
        
        # Unidade de media
        self.lbl_unidade_medida = tk.Label(self.container_formulario, text="Unidade de medida:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_unidade_medida.grid(row=9, column=0, pady=(0,0), sticky='nsw')
                # Rótulos para os valores na coluna de medida
        self.cmb_unidade_medida = ttk.Combobox(self.container_formulario, values=self.rotulos_de_medidas, state="readonly")
        self.cmb_unidade_medida.grid(row=10, column=0, columnspan=5, sticky='nsew')

        # Quantidade em estoque
        self.lbl_estoque = tk.Label(self.container_formulario, text="Quantidade em estoque:", anchor='w', bg=constants.cores['cinza'])
        self.lbl_estoque.grid(row=13, column=0, pady=(2,0), sticky='nsw')
        self.ent_estoque = tk.Entry(self.container_formulario)
        self.ent_estoque.grid(row=14, column=0, columnspan=5, sticky='nsew')

    def editar_insumo(self, insumo):
        self.ent_nome.delete(0, 'end')
        self.ent_nome.insert(0, insumo['nome'])
        self.ent_media_consumo.delete(0, 'end')
        self.ent_media_consumo.insert(0, insumo['media-consumo'])
        self.ent_estoque.delete(0, 'end')
        self.ent_estoque.insert(0, insumo['estoque'])
        self.cmb_unidade_medida.delete(0, 'end')
        self.cmb_unidade_medida.insert(0, insumo['medida'])
        self.id_para_edicao = insumo['id']
        self.flag_editar = True
    
    def obter_valores_campos_formulario(self):
        # Captura os valores dos campos
        nome = self.ent_nome.get()
        media_consumo = self.ent_media_consumo.get()
                # Rótulos para os valores na coluna de medida
        unidade_medida_id = self.rotulos_de_medidas.index(self.cmb_unidade_medida.get()) + 1
        estoque = self.ent_estoque.get()
        
        return (nome, media_consumo, estoque, unidade_medida_id)
