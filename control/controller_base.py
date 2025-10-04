from model.model_base import ModelBase, ResponseQuery

class ControllerBase:
    def __init__(self):
        """
        Base para controller responsável por intermediar operações 
        entre a aplicação e o banco de dados.
        """
        
        self.model = ModelBase()

        # Mapeamento dos campos da tupla de usuário para seus índices.
        self.indices_campos = dict()

        # Funções de callback para operações CRUD 
        # (preencha todas ao criar uma classe que herde de ControllerBase)
        self.funcao_inserir_item = None
        self.funcao_listar_item = None
        self.funcao_buscar_item = None
        self.funcao_buscar_item_por_id = None
        self.funcao_excluir_item = None
        self.funcao_atualizar_item = None
        self.funcao_to_dict_item = None

    def inserir(self, *args, **kwargs) -> ResponseQuery:
        """
        Aceita tanto forma posicional quanto nomeada.
        """
        if args and not kwargs:
            return self.funcao_inserir_item(*args)
        elif kwargs and not args:
            return self.funcao_inserir_item(**kwargs)
        else:
            raise TypeError("Use apenas argumentos posicionais OU apenas nomeados.")

    def listar(self, termo_busca: str = '') -> ResponseQuery:
        return self.funcao_listar_item(termo_busca)

    def buscar(self, *args, **kwargs) -> ResponseQuery:
        """
        Aceita tanto forma posicional quanto nomeada.
        """
        if args and not kwargs:
            return self.funcao_buscar_item(*args)
        elif kwargs and not args:
            return self.funcao_buscar_item(**kwargs)
        else:
            raise TypeError("Use apenas argumentos posicionais OU apenas nomeados.")

    def buscar_por_id(self, *args, **kwargs) -> ResponseQuery:
        """
        Aceita tanto forma posicional quanto nomeada.
        """
        if args and not kwargs:
            return self.funcao_buscar_item_por_id(*args)
        elif kwargs and not args:
            return self.funcao_buscar_item_por_id(**kwargs)
        else:
            raise TypeError("Use apenas argumentos posicionais OU apenas nomeados.")

    def excluir(self, *args, **kwargs) -> ResponseQuery:
        """
        Aceita tanto forma posicional quanto nomeada.
        """
        if args and not kwargs:
            return self.funcao_excluir_item(*args)
        elif kwargs and not args:
            return self.funcao_excluir_item(**kwargs)
        else:
            raise TypeError("Use apenas argumentos posicionais OU apenas nomeados.")

    def atualizar(self, *args, **kwargs) -> ResponseQuery:
        """
        Aceita tanto forma posicional quanto nomeada.
        """
        if args and not kwargs:
            return self.funcao_atualizar_item(*args)
        elif kwargs and not args:
            return self.funcao_atualizar_item(**kwargs)
        else:
            raise TypeError("Use apenas argumentos posicionais OU apenas nomeados.")

    def to_dict(self, *args, **kwargs) -> dict:
        """
        Aceita tanto forma posicional quanto nomeada.
        """
        if args and not kwargs:
            return self.funcao_to_dict_item(*args)
        elif kwargs and not args:
            return self.funcao_to_dict_item(**kwargs)
        else:
            raise TypeError("Use apenas argumentos posicionais OU apenas nomeados.")
