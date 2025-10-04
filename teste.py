import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zoom com Ctrl + e Ctrl -")
        self.geometry("400x250")

        # Escala inicial
        self.escala = 1.0

        # Fonte base
        self.fonte_base = ("Arial", 12)

        # Widgets de exemplo
        self.lbl = ttk.Label(self, text="Use Ctrl + e Ctrl - para ajustar a escala", font=self.fonte_base)
        self.lbl.pack(pady=20)

        self.btn = ttk.Button(self, text="Botão de teste")
        self.btn.pack()

        self.txt = tk.Text(self, height=5, width=30)
        self.txt.pack(pady=10)

        # Bind dos atalhos
        self.bind_all("<Control-plus>", self.aumentar_escala)
        self.bind_all("<Control-minus>", self.diminuir_escala)
        self.bind_all("<Control-=>", self.aumentar_escala)  # em alguns teclados o '+' requer '='

    def aplicar_escala(self):
        """Aplica o fator de escala atual à interface."""
        self.tk.call('tk', 'scaling', self.escala)  # ajusta DPI geral (afeta fontes)
        nova_fonte = (self.fonte_base[0], int(self.fonte_base[1] * self.escala))
        self.lbl.configure(font=nova_fonte)
        print(f'escala = {self.escala}, fonte = {nova_fonte}')
        # Se quiser aplicar a todos, pode percorrer self.winfo_children()

    def aumentar_escala(self, event=None):
        self.escala = min(round(self.escala + 0.1, 1), 2.0)
        self.aplicar_escala()

    def diminuir_escala(self, event=None):
        self.escala = max(round(self.escala - 0.1, 1), 0.75)
        self.aplicar_escala()


if __name__ == "__main__":
    App().mainloop()
