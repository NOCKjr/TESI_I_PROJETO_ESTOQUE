from model import escola_model

class EscolaController:
    def __init__(self):
        self.model = escola_model.EscolaModel()

    def inserir_escola(self, nome='', endereco='', numero_alunos=0):
        sql = f"INSERT INTO escola(esc_nome, esc_endereco, esc_numero_alunos) VALUES ('{nome}', '{endereco}', '{numero_alunos}');"
        return self.model.insert(sql)

    def listar_escola(self, nome=''):
        sql = f'SELECT * FROM escola WHERE esc_nome LIKE "%{nome}%";'
        return self.model.get(sql)

    def excluir_escola(self, id):
        sql = f'DELETE FROM escola WHERE esc_id = {id}'
        return self.model.delete(sql)

    def atualizar_escola(self):
        pass