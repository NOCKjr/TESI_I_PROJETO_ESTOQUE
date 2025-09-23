from model import fornecedor_model

class FornecedorController:
    def __init__(self):
        self.model = fornecedor_model.FornecedorModel()

    def inserir_fornecedor(self, razao_social='', contato=''):
        sql = f"INSERT INTO fornecedor(for_razao_social, for_contato) VALUES ('{razao_social}','{contato}');"
        return self.model.insert(sql)

    def listar_fornecedor(self, razao_social=''):
        sql = f'SELECT * FROM fornecedor WHERE for_razao_social LIKE "%{razao_social}%";'
        return self.model.get(sql)

    def excluir_fornecedor(self, id):
        sql = f'DELETE FROM fornecedor WHERE for_id = {id}'
        return self.model.delete(sql)

    def atualizar_fornecedor(self):
        pass

#teste = FornecedorController()
#print(teste.listar_fornecedor())