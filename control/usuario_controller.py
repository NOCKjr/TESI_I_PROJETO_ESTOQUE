from model import model_base
import hashlib

class UsuarioController:
    def __init__(self):
        self.model = model_base.ModelBase()

        # Mapeamento dos campos da tupla de usuário para seus índices.
        # Tupla: (id, nick, email, senha, tipo)
        # Atenção: se a estrutura do banco mudar, atualize os índices neste dicionário.
        self.indices_campos = {
            "id": 0,
            "nick": 1,
            "email": 2,
            "senha": 3,
            "tipo": 4
        }

    def inserir_usuario(self, nick='', email='', senha='', tipo='C') -> int:
        """
        Insere um usuário no banco de dados.

        Args:
            nick (str): Apelido do usuário. Padrão ''.
            email (str): Email do usuário. Padrão ''.
            senha (str): Senha do usuário. Padrão ''.
            tipo (str): Tipo de usuário. Padrão 'C'.

        Returns:
            int: Número de linhas afetadas no banco.
        """
        # criptografa a senha antes de salvá-la
        hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        # sql que será executado
        sql = f"INSERT INTO usuario(usu_nick, usu_email,usu_senha, usu_tipo) VALUES ('{nick}', '{email}', '{hash}', '{tipo}');"
        # executa o sql e retorna o número de linhas afetadas
        return self.model.insert(sql)

    def listar_usuario(self, termo_busca='') -> list[dict] | None:
        """
        Lista os usuários cujo o nick contenha um termo de busca.
        
        Args:
            termo_busca (str): Termo procurado no nick. Padrão ''
        
        Returns:
            list[dict]: Lista de dicionários com os usuários correspondentes.
        """
        # sql que será executado
        sql = f'SELECT * FROM usuario WHERE usu_nick LIKE "%{termo_busca}%";'
        # resultado da consulta (lista de tuplas)
        resultado = self.model.get(sql)
        # converter as tuplas para dict
        usuarios = list(map(lambda user: self.to_dict(user), resultado))
        # retorna a lista de usuários
        return usuarios

    def busca_usuario(self, nick_ou_email='') -> dict | None:
        """
        Retorna um usuário no o nick ou email informado.
        
        Args:
            nick_ou_email (str): String que pode ser o nick ou o email de um usuário.
        
        Returns:
            dict: O usuário correspondente.
        """
        # sql que será executado
        sql = f'SELECT * FROM usuario WHERE usu_nick LIKE "{nick_ou_email}" or usu_email LIKE "{nick_ou_email}";'
        # resultado da consulta (tupla)
        resultado = self.model.get(sql)
        if not resultado:
            return None # o usuário não existe
        # converter para dict
        usuario = self.to_dict(resultado[0])
        # retorna o usuário como dict
        return usuario

    def excluir_usuario(self, id) -> int:
        """
        Exclui do banco de dados o usuário com o id correspondente.
        
        Args:
            id (int): Identificador do usuário.
        
        Returns:
            int: Número de linhas afetadas no banco.
        """
        # sql que será executado
        sql = f'DELETE FROM usuario WHERE usu_id = {id}'
        # executa o sql e retorna o número de linhas afetadas
        return self.model.delete(sql)

    def atualizar_usuario(self, id, nick, email, senha, tipo) -> int:
        """
        Atualiza as informações do usuário com o id informado.

        Args:
            id (int): Identificador do usuário a ser atualizado.
            nick (str): Novo apelido do usuário.
            email (str): Novo email do usuário.
            senha (str): Nova senha do usuário (deve estar hashificada antes se necessário).
            tipo (str): Novo tipo do usuário (ex: 'C' para comum, 'A' para admin).

        Returns:
            int: Número de linhas afetadas no banco de dados.
        """
        # sql que será executado
        sql = f'UPDATE usuario SET usu_nick = "{nick}", usu_email = "{email}", usu_senha = "{senha}", usu_tipo = "{tipo}" WHERE usu_id = {id};'
        # atualiza o usuário
        return self.model.update(sql)


    def to_dict(self, usuario: tuple) -> dict:
        """
        Converte um registro de usuário do banco para o tipo dict.
        
        Args:
            usuario (tuple): Tupla com os campos do usuário
        
        Returns:
            dict: Mesmo usuário, mas do tipo dict.
        """
        # objeto convertido
        objeto = {
            "id": usuario[self.indices_campos["id"]],
            "nick": usuario[self.indices_campos["nick"]],
            "email": usuario[self.indices_campos["email"]],
            "senha": usuario[self.indices_campos["senha"]],
            "tipo": usuario[self.indices_campos["tipo"]],
        }
        return objeto