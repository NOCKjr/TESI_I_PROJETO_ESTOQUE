from model import model_base

class MovimentacaoController:
    def __init__(self):
        self.model = model_base.ModelBase()

    def inserir_movimentacao(self, data, tipo, usuario_id, fornecedor_id, escola_id):
        sql = f"INSERT INTO movimentacao(mov_data, mov_tipo,fk_mov_usu_id, fk_mov_for_id, fk_mov_esc_id) VALUES ('{data}', '{tipo}', {usuario_id}, {fornecedor_id}, {escola_id});"
        return self.model.insert(sql)

    def listar_movimentacao(self, unidade=''):
        sql = f'SELECT * FROM medida WHERE med_unidade LIKE "%{unidade}%";'
        return self.model.get(sql)

    def excluir_movimentacao(self, id):
        sql = f'DELETE FROM medida WHERE med_id = {id}'
        return self.model.delete(sql)

    def atualizar_movimentacao(self, id, unidade):
        sql = f"UPDATE medida SET med_unidade = '{unidade}' WHERE med_id = {id};"
        return self.model.update(sql)