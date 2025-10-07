import ttkbootstrap as ttk
import tkinter as tk

from app_context import get_context
import constants
from view.telas.gerenciador_de_janelas import GerenciadorDeJanelasBase

class TelaBase(ttk.Frame):
    """Interface que todas as telas devem implementar"""
    def __init__(self, master, gerenciador_de_janelas: GerenciadorDeJanelasBase, largura=constants.LARGURA_JANELA, altura=constants.ALTURA_JANELA):
        super().__init__(master, width=largura, height=altura)
        
        # guarda qual objeto está gerenciando a troca entre janelas
        self.gerenciador_de_janelas = gerenciador_de_janelas
    
    def mostrar(self):
        """Exibe a tela"""
        self.pack(expand=True, fill='both', anchor='center')
    
    def esconder(self):
        """Esconde a tela"""
        self.pack_forget()
    
    def alterar_para_a_tela(self, proxima_tela):
        """Chama o gerenciador de janelas para alterar entre janelas"""
        self.gerenciador_de_janelas.alterar_para_a_tela(proxima_tela)
    
    # def atualizar_fonte_widgets(self, nova_escala):
    #     """
    #     Atualiza a fonte de todos os Entry, Label, Combobox e Button
    #     com base na nova escala fornecida.
    #     """
    #     nova_fonte = ('Arial', max(int(12 * nova_escala), 1))
    #     for child in self.winfo_children():
    #         self._atualizar_fonte_recursivo(child, nova_fonte)

    def atualizar_fonte_widgets(self, nova_escala):
        """Atualiza a fonte de todos os Entry, Label, Combobox e Button."""
        for child in self.winfo_children():
            self._atualizar_fonte_recursivo(child, nova_escala)

    def _atualizar_fonte_recursivo(self, widget, nova_escala):
        """Aplica fonte escalada ao widget."""
        if isinstance(widget, (ttk.Entry, ttk.Label, ttk.Combobox, ttk.Button)):
            try:
                style_name = widget.cget('style')
            except tk.TclError:
                style_name = None

            # Fonte padrão
            nova_fonte = ('Arial', max(int(12 * nova_escala), 1))

            # Se tiver estilo personalizado, apenas reescala o tamanho
            if style_name and '.' in style_name:
                style = ttk.Style()
                try:
                    atual = style.lookup(style_name, 'font')
                    if not atual:
                        atual = ('Arial', 12)
                    if isinstance(atual, str):
                        partes = atual.split()
                        fam = partes[0]
                        tam = int(partes[1]) if len(partes) > 1 else 12
                        opts = partes[2:] if len(partes) > 2 else []
                    elif isinstance(atual, (list, tuple)):
                        fam, tam, *opts = atual
                    else:
                        fam, tam, opts = 'Arial', 12, []
                    
                    nova_fonte = (fam, max(int(tam * nova_escala), 1), *opts)
                except Exception:
                    nova_fonte = ('Arial', max(int(12 * nova_escala), 1))

            try:
                widget.configure(font=nova_fonte)
            except tk.TclError:
                pass

        # Aplica recursivamente aos filhos
        for filho in widget.winfo_children():
            self._atualizar_fonte_recursivo(filho, nova_escala)

    def find_treeviews(self, widget):
        """Gera todos os ttk.Treeview filhos (recursivo)."""
        for child in widget.winfo_children():
            if isinstance(child, ttk.Treeview):
                yield child
            yield from self.find_treeviews(child)
    
    def atualizar_altura_treeviews(self, nova_altura: int):
        """Ajusta a altura de todos os Treeviews filhos recursivamente."""
        style = ttk.Style()
        for tv in self.find_treeviews(self):
            try:
                style_name = tv.cget('style') or 'Treeview'
                style.configure(
                    style_name,
                    rowheight=nova_altura,
                    font=('Calibri', max(int(11 * get_context().escala), 1))
                )
                tv.update_idletasks()  # recalcula geometria e redesenha
            except tk.TclError:
                pass

