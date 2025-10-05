from enum import Enum

# Dimensões padrão da janela
LARGURA_JANELA = 800
ALTURA_JANELA = 450

# Nome das telas
TELA_LOGIN = "login"
TELA_MENU_PRINCIPAL = "menu"
TELA_MENU_CADASTROS = "cadastros"
TELA_MOVIMENTACOES = "movimentacoe"
TELA_FORMULARIO_MOVIMENTACOES = "formulario-movimentacoe"
TELA_HISTORICO = "historico"
TELA_CADASTRAR_USUARIO = "cadastrar-usuario"
TELA_CADASTRAR_ESCOLA = "cadastrar-escola"
TELA_CADASTRAR_FORNECEDOR = "cadastrar-fornecedor"
TELA_CADASTRAR_INSUMO = "cadastrar-insumo"
TELA_CADASTRAR_MOVIMENTACAO = "cadastrar-movimentacao"
TELA_CONSULTAS = "consulta"
TELA_LISTAGEM_USUARIOS = "listagem-usuario"
TELA_LISTAGEM_ESCOLAS = "listagem-escola"
TELA_LISTAGEM_FORNECEDORES = "listagem-fornecedor"
TELA_LISTAGEM_MOVIMENTACOES = "listagem-movimentacao"
TELA_LISTAGEM_INSUMOS = "listagem-insumo"
TELA_EDITAR_USUARIO = "editar-usuario"
TELA_EDITAR_ESCOLA = "editar-escola"
TELA_EDITAR_FORNECEDOR = "editar-fornecedor"
TELA_EDITAR_INSUMO = "editar-insumo"

#Caminho onde ficará o banco de dados
DB_PATH = "banco/banco.db"

#Tipos de entidades
ENTIDADE_USUARIO = "usuario"
ENTIDADE_ESCOLA = "escola"
ENTIDADE_FORNECEDOR = "fornecedor"
ENTIDADE_INSUMO = "insumo"
ENTIDADE_ENDERECO = "endereco"
ENTIDADE_ITEM = "item"
ENTIDADE_MOVIMENTACAO = "movimentacao"

class Cores(Enum):
    PRINCIPAL = '#075F8B'
    SECUNDARIO = '#87C5FF'
    CINZA = '#d9d9d9'
    BRANCO = '#ffffff'
    PRETO = '#000000'
    VERDE = '#3AB800'
    VERMELHO = '#FF0000'

# Cores
cores = {
    "principal": '#075F8B',
    "secundario": '#87C5FF',
    "cinza": '#d9d9d9',
    'branco': '#ffffff',
    'verde': '#3AB800',
    'vermelho': "#FF0000",
}