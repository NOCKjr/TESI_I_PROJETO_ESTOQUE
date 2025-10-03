import tkinter as tk
import constants

from control.usuario_controller import UsuarioController

def iniciar_janela():
    root = tk.Tk()

    # Pega dimensões do monitor
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Define a proporção desejada (ex: 80% da tela)
    proporcao = 0.8
    largura_janela = int(largura_tela * proporcao)
    altura_janela = int(altura_tela * proporcao)

    # Calcula posição centralizada
    pos_x = 0#(largura_tela - largura_janela) // 2
    pos_y = 0#(altura_tela - altura_janela) // 4

    print(f"""
monitor: {largura_tela}x{altura_tela}
janela: {largura_janela}x{altura_janela}
pos: ({pos_x}, {pos_y})
""")

    # Define tamanho e posição
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    root.title("Janela com escala dinâmica")
    root.mainloop()
# 
# iniciar_janela()


# Excluir os usuários admin repetidos por causa de um bug
# controle = UsuarioController()
# admins = controle.listar_usuario('admin')

# print(*admins, sep='\n')

# for adm in admins:
#     if adm['id'] != 7:
#         controle.excluir_usuario(adm['id'])
# admins = controle.listar_usuario('admin')
# print(*admins, sep='\n')



# uc = UsuarioController()
# uc.inserir_usuario(nick='alonso', senha='admin', email='alonso', tipo='A')


# print(*uc.listar_usuario(), sep='\n')

# def t(tipo_entidade):
#     match tipo_entidade:
#         case constants.ENTIDADE_USUARIO:
#             return "o", "usuário"
#         case constants.ENTIDADE_ESCOLA:
#             return "a", "escola"
#         case constants.ENTIDADE_FORNECEDOR:
#             return "o", "fornecedor"
#         case constants.ENTIDADE_INSUMO:
#             return "o", "insumo"
#         case _:
#             return "", ""

# nome = 'alonso'
# # print(f'excluir {t(constants.ENTIDADE_USUARIO)}')
# print(f"Tem certeza que deseja excluir {(lambda e: f"{e[0]} {e[1]}")(t(constants.ENTIDADE_USUARIO))} '{nome}'?")



class ControlBase:
    def __init__(self):
        pass

    def inserir(self, *args, **kwargs):
        """Método base de inserção (pode ser sobrescrito)."""
        print("Inserir no base:", args, kwargs)


class ControlUsuario(ControlBase):
    def __init__(self):
        super().__init__()

    def inserir_usuario(self, nome, senha):
        """Insere um usuário com nome e senha."""
        print(f"Inserindo usuário: nome={nome}, senha={senha}")

    def inserir(self, *args, **kwargs):  # sobrescrevendo
        """Sobrescreve e aceita tanto posicional quanto nomeado."""
        if args and not kwargs:
            # chamada posicional: inserir('alonso', '123')
            self.inserir_usuario(*args)
        elif kwargs and not args:
            # chamada nomeada: inserir(nome='alonso', senha='123')
            self.inserir_usuario(**kwargs)
        else:
            raise TypeError("Use apenas argumentos posicionais OU apenas nomeados.")


if __name__ == '__main__':
    c = ControlUsuario()
    c.inserir('alonso', '123')                     # posicional
    c.inserir(nome='Admin', senha='Admin')         # nomeado
