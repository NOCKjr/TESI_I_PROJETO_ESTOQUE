from model import model_base

class EnderecoController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de endereço para seus índices.
        # Tupla: (id, logradouro, numero, bairro, cidade, estado, cep, complemento, ponto_referencia)
        # Atenção: se a estrutura do banco mudar, atualize os índices neste dicionário.
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

    def inserir_endereco(self, logradouro: str, numero: str, bairro: str, cidade: str, estado: str, cep: str, complemento: str = '', ponto_referencia: str = '') -> int:
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
            int: Número de linhas afetadas.
        """
        sql = (
            "INSERT INTO endereco(end_logradouro, end_numero, end_bairro, end_cidade, end_estado, end_cep, end_complemento, end_ponto_referencia) "
            f"VALUES ('{logradouro}', '{numero}', '{bairro}', '{cidade}', '{estado}', '{cep}', '{complemento}', '{ponto_referencia}');"
        )
        return self.model.insert(sql)

    def listar_endereco(self) -> list[dict]:
        """
        Lista todos os endereços.

        Returns:
            list[dict]: Lista de endereços como dicionários.
        """
        sql = 'SELECT * FROM endereco;'
        resultado = self.model.get(sql)
        return [self.to_dict(e) for e in resultado] if resultado else []

    def excluir_endereco(self, id: int) -> int:
        """
        Exclui um endereço pelo ID.

        Args:
            id (int): ID do endereço.

        Returns:
            int: Número de linhas afetadas.
        """
        sql = f'DELETE FROM endereco WHERE end_id = {id};'
        return self.model.delete(sql)

    def atualizar_endereco(self, id: int, logradouro: str, numero: str, bairro: str, cidade: str, estado: str, cep: str, complemento: str = '', ponto_referencia: str = '') -> int:
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
            int: Número de linhas afetadas.
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

    def to_dict(self, endereco: tuple) -> dict:
        """
        Converte uma tupla de endereço em dicionário.

        Args:
            endereco (tuple): Tupla com os campos do endereço.

        Returns:
            dict: Endereço no formato dicionário.
        """
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
