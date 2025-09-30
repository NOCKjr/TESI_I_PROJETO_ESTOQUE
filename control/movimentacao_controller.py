from model import model_base

class MovimentacaoController:
    def __init__(self):
        self.model = model_base.ModelBase()

    def inserir_movimentacao(self, data, tipo, usuario_id, fornecedor_id, escola_id):
        sql = f"INSERT INTO movimentacao(mov_data, mov_tipo,fk_mov_usu_id, fk_mov_for_id, fk_mov_esc_id) VALUES ('{data}', '{tipo}', {usuario_id}, {fornecedor_id}, {escola_id});"
        return self.model.insert(sql)

    def listar_movimentacao(self):
        sql = f"SELECT * FROM movimentacao ORDER BY mov_data DESC;"
        return self.model.get(sql)

    def listar_movimentacao_por_fornecedor(self, fornecedor_id):
        sql = f"SELECT * FROM movimentacao WHERE fk_mov_for_id = {fornecedor_id} ORDER BY mov_data DESC;"
        return self.model.get(sql)

    def listar_movimentacao_por_escola(self, escola_id):
        sql = f"SELECT * FROM movimentacao WHERE fk_mov_esc_id = {escola_id} ORDER BY mov_data DESC;"
        return self.model.get(sql)

    def excluir_movimentacao(self, id):
        pass

    def atualizar_movimentacao(self, id, unidade):
        pass

#teste = MovimentacaoController()
#print(teste.listar_movimentacao_por_escola(3))