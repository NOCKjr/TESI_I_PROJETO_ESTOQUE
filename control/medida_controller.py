from model import model_base

class MedidaController:
    def __init__(self):
        self.model = model_base.ModelBase()

    def inserir_medida(self, unidade):
        sql = f"INSERT INTO medida(med_unidade) VALUES ('{unidade}');"
        return self.model.insert(sql)

    def listar_medida(self, unidade=''):
        sql = f'SELECT * FROM medida WHERE med_unidade LIKE "%{unidade}%";'
        return self.model.get(sql)

    def excluir_medida(self, id):
        sql = f'DELETE FROM medida WHERE med_id = {id}'
        return self.model.delete(sql)

    def atualizar_medida(self, id, unidade):
        sql = f"UPDATE medida SET med_unidade = '{unidade}' WHERE med_id = {id};"
        return self.model.update(sql)