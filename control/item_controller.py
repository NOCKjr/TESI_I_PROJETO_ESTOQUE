from model import model_base

class ItemController:
    def __init__(self):
        self.model = model_base.ModelBase()

    def inserir_item(self, quantidade, insumo_id, movimentacao_id):
        sql = f"INSERT INTO item(itm_quantidade,. fk_itm_ins_id, fk_itm_mov_id) VALUES ({quantidade}, {insumo_id}, {movimentacao_id});"
        return self.model.insert(sql)

    def listar_item(self, movimentacao_id):
        sql = f'SELECT * FROM item WHERE fk_itm_mov_id = {movimentacao_id};'
        return self.model.get(sql)
    def excluir_item(self, id):
        sql = f'DELETE FROM item WHERE itm_id = {id}'
        return self.model.delete(sql)

    def atualizar_item(self, id, quantidade, insumo_id, movimentacao_id):
        sql = f'UPDATE item SET itm_quantidade = {quantidade}, fk_itm_ins_id = {insumo_id}, fk_itm_mov_id = {movimentacao_id} WHERE itm_id = {id};'
        return self.model.update(sql)