from model import model_base
from model.model_base import ResponseQuery

class EnderecoController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de endereço para seus índices.
        self.indices_campos = {
            "id": 0,
            "logradouro": 1,
            "numero": 2,
            "bairro": 3,
            "cidade": 4,
            "estado": 5,
            "cep": 6,
            "complemento": 7,
            "ponto_referencia": 8,
        }

    def inserir_endereco(self, logradouro: str, numero: str, bairro: str, cidade: str, estado: str, cep: str, complemento: str = '', ponto_referencia: str = '') -> ResponseQuery:
        """
        Insere um endereço no banco.

        Args:
            logradouro (str): Nome da rua.
            numero (str): Número do endereço.
            bairro (str): Bairro.
            cidade (str): Cidade.
            estado (str): Estado.
            cep (str): CEP.
            complemento (str): Complemento. Padrão ''.
            ponto_referencia (str): Ponto de referência. Padrão ''.

        Returns:
            ResponseQuery:
                - `retorno`: ID do endereço inserido.
                - `erros`: lista de erros em caso de falha.
        """
        sql = (
            "INSERT INTO endereco(end_logradouro, end_numero, end_bairro, end_cidade, end_estado, end_cep, end_complemento, end_ponto_referencia) "
            f"VALUES ('{logradouro}', '{numero}', '{bairro}', '{cidade}', '{estado}', '{cep}', '{complemento}', '{ponto_referencia}');"
        )
        return self.model.insert(sql)

    def listar_endereco(self) -> ResponseQuery:
        """
        Lista todos os endereços.

        Returns:
            ResponseQuery:
                - `retorno`: lista de endereços como dicionários.
                - `erros`: lista de erros em caso de falha.
        """
        sql = 'SELECT * FROM endereco;'
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = [self.to_dict(e) for e in resp.retorno]
        return resp

    def excluir_endereco(self, id: int) -> ResponseQuery:
        """
        Exclui um endereço pelo ID.

        Args:
            id (int): ID do endereço.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f'DELETE FROM endereco WHERE end_id = {id};'
        return self.model.delete(sql)

    def atualizar_endereco(self, id: int, logradouro: str, numero: str, bairro: str, cidade: str, estado: str, cep: str, complemento: str = '', ponto_referencia: str = '') -> ResponseQuery:
        """
        Atualiza os dados de um endereço.

        Args:
            id (int): ID do endereço.
            logradouro (str): Novo logradouro.
            numero (str): Novo número.
            bairro (str): Novo bairro.
            cidade (str): Nova cidade.
            estado (str): Novo estado.
            cep (str): Novo CEP.
            complemento (str): Novo complemento. Padrão ''.
            ponto_referencia (str): Novo ponto de referência. Padrão ''.

        Returns:
            ResponseQuery:
                - `retorno`: número de linhas afetadas.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"""UPDATE endereco 
                    SET end_logradouro = '{logradouro}', 
                        end_numero = '{numero}', 
                        end_bairro = '{bairro}',
                        end_cidade = '{cidade}',
                        end_estado = '{estado}',
                        end_cep = '{cep}',
                        end_complemento = '{complemento}',
                        end_ponto_referencia = '{ponto_referencia}'
                    WHERE end_id = {id};"""
        return self.model.update(sql)

    def buscar_endereco_string(self, id: int) -> ResponseQuery:
        """
        Busca um endereço pelo ID e retorna como string formatada.

        Args:
            id (int): ID do endereço.

        Returns:
            ResponseQuery:
                - `retorno`: string do endereço ou None se não encontrado.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"SELECT * FROM endereco WHERE end_id = {id};"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        if not resp.retorno:
            resp.retorno = None
            return resp

        endereco = resp.retorno[0]
        partes = [
            f"{endereco[self.indices_campos['logradouro']]}, ",
            f"Nº {endereco[self.indices_campos['numero']]} - ",
            f"{endereco[self.indices_campos['bairro']]}. ",
            f"{endereco[self.indices_campos['cidade']]} - ",
            f"{endereco[self.indices_campos['estado']]}. ",
            f"CEP {endereco[self.indices_campos['cep']]}. "
        ]
        complemento = endereco[self.indices_campos['complemento']]
        ponto_ref = endereco[self.indices_campos['ponto_referencia']]
        if complemento:
            partes.append(f"Complemento: {complemento}.")
        if ponto_ref:
            partes.append(f"Ponto de referência: {ponto_ref}.")
        resp.retorno = "".join(partes)
        return resp

    def buscar_endereco_por_id(self, id: int) -> ResponseQuery:
        """
        Busca um endereço pelo ID e retorna como dicionário.

        Args:
            id (int): ID do endereço.

        Returns:
            ResponseQuery:
                - `retorno`: dicionário do endereço ou None se não encontrado.
                - `erros`: lista de erros em caso de falha.
        """
        sql = f"SELECT * FROM endereco WHERE end_id = {id};"
        resp = self.model.get(sql)
        if not resp.ok():
            return resp
        resp.retorno = self.to_dict(resp.retorno[0]) if resp.retorno else None
        return resp

    def to_dict(self, endereco: tuple) -> dict:
        """Converte uma tupla de endereço em dicionário."""
        return {
            "id": endereco[self.indices_campos["id"]],
            "logradouro": endereco[self.indices_campos["logradouro"]],
            "numero": endereco[self.indices_campos["numero"]],
            "bairro": endereco[self.indices_campos["bairro"]],
            "cidade": endereco[self.indices_campos["cidade"]],
            "estado": endereco[self.indices_campos["estado"]],
            "cep": endereco[self.indices_campos["cep"]],
            "complemento": endereco[self.indices_campos["complemento"]],
            "ponto_referencia": endereco[self.indices_campos["ponto_referencia"]],
        }
