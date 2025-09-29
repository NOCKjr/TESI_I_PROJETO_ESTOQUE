from model import model_base

class EnderecoController:
    def __init__(self):
        self.model = model_base.ModelBase()

    def inserir_endereco(self, logradouro, numero, bairro, cidade, estado, cep, complemento='', ponto_referencia=''):
        sql = f"INSERT INTO endereco(end_logradouro, end_numero, end_bairro, end_cidade, end_estado, end_cep, end_complemento, end_ponto_referencia) VALUES ('{logradouro}', '{numero}', '{bairro}', '{cidade}', '{estado}', '{cep}','{complemento}', '{ponto_referencia}');"
        return self.model.insert(sql)

    def listar_endereco(self):
        sql = f'SELECT * FROM endereco'
        return self.model.get(sql)

    def excluir_endereco(self, id):
        pass

    def atualizar_endereco(self, id, logradouro, numero, bairro, cidade, estado, cep, complemento='', ponto_referencia=''):
        sql = f"""UPDATE endereco 
        SET end_logradouro = '{logradouro}', 
            end_numero = {numero}, 
            end_bairro = '{bairro}',
            end_cidade = '{cidade}',
            end_estado = '{estado}',
            end_cep = '{cep}',
            end_complemento = '{complemento}',
            end_ponto_referencia = '{ponto_referencia}'
            WHERE end_id = {id};"""
        return self.model.update(sql)