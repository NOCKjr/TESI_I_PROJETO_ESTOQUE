import ttkbootstrap as ttk
import constants
import abc

from view.telas.menus.menu_navegacao import MenuNavegacao

class GerenciadorDeJanelasBase(ttk.Frame, abc.ABC):
    def __init__(self, master):
        super().__init__(master)
        self.tela_atual = None
        self.usuario_logado = None

        ### Menu superior de navegação
        self.container_menu = ttk.Frame(self)
        self.container_menu.pack(side='top', fill='x')
        self.menu_navegacao = MenuNavegacao(self.container_menu, self)
        self.menu_navegacao.exibir()

        # Scrollbar lateral
        self.scb_scroller = ttk.Scrollbar(self)
        self.scb_scroller.pack(side='right', fill='y')

        # Área de conteúdo da tela em exibição
        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(fill="both", expand=True)
    
    @abc.abstractmethod
    def get_tela(self, nome_tela: str) -> ttk.Frame:
        """Deve retornar a referência de um ttk.Frame."""
        pass
    
    def alterar_para_a_tela(self, proxima_tela: str):
        tela = self.get_tela(proxima_tela)

        # só troca de tela se a próxima tela é uma referência válida
        # (sugestão: trocar depois para lançar uma exceção?)
        if tela is not None:
            
            # muda a referência da tela atual
            tela_anterior = self.tela_atual
            self.tela_atual = tela

            # esconde a tela anterior
            if tela_anterior is not None:
                tela_anterior.pack_forget()
            
            # mostra a nova tela
            self.tela_atual.mostrar()
        
        else:
            print(f'GerenciadorDeJanelas: Erro! A tela {proxima_tela} não foi encontrada.')
