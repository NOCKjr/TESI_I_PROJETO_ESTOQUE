from model import insumo_model

class InsumoController:
    def __init__(self):
        self.model = insumo_model.InsumoModel()

    def inserir_insumo(self, nome, media_consumida, quantidade_estoque, medida_id):
        sql = f"INSERT INTO insumo(ins_nome, ins_media_consumida, ins_quantidade_estoque, ins_med_id) VALUES ('{nome}',{media_consumida}, {quantidade_estoque}, {medida_id});"
        return self.model.insert(sql)

    def listar_insumo(self, nome=''):
        sql = f'SELECT * FROM insumo WHERE ins_nome LIKE "%{nome}%";'
        return self.model.get(sql)

    def excluir_insumo(self, id):
        sql = f'DELETE FROM insumo WHERE ins_id = {id}'
        return self.model.delete(sql)

    def atualizar_insumo(self, id, nome, media_consumida, quantidade_estoque, medida_id):
        sql = f'UPDATE insumo SET ins_nome = "{nome}", ins_media_consumida = {media_consumida}, ins_quantidade_estoque = {quantidade_estoque}, ins_med_id = {medida_id} WHERE ins_id = {id};'
        return self.model.update(sql)