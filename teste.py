import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu Simulado com Frame")
        self.geometry("400x300")

        # menu superior
        self.menu_frame = tk.Frame(self, bg="#ddd")
        self.menu_frame.pack(side="top", fill="x")

        # área de conteúdo (onde as telas aparecem)
        self.content_frame = tk.Frame(self, bg="white")
        self.content_frame.pack(fill="both", expand=True)

        # dicionário de telas
        self.frames = {
            "Tela 1": self._criar_tela("Tela 1", "lightblue"),
            "Tela 2": self._criar_tela("Tela 2", "lightgreen"),
            "Tela 3": self._criar_tela("Tela 3", "lightyellow"),
        }

        # botões do "menu"
        self.botoes = {}
        for nome in self.frames:
            btn = ttk.Button(self.menu_frame, text=nome,
                             command=lambda n=nome: self.mostrar_tela(n))
            btn.pack(side="left", padx=2, pady=2)
            self.botoes[nome] = btn

        # mostrar tela inicial
        self.mostrar_tela("Tela 1")

    def _criar_tela(self, nome, cor):
        """Cria um frame de exemplo para cada tela"""
        frame = tk.Frame(self.content_frame, bg=cor)
        label = tk.Label(frame, text=nome, font=("Arial", 16), bg=cor)
        label.pack(expand=True)
        return frame

    def mostrar_tela(self, nome):
        """Exibe o frame selecionado e destaca o botão"""
        # esconde todos os frames
        for f in self.frames.values():
            f.pack_forget()
        # mostra o selecionado
        self.frames[nome].pack(fill="both", expand=True)

        # reseta estilo dos botões
        for b in self.botoes.values():
            b.state(["!pressed"])
        # destaca o botão ativo
        self.botoes[nome].state(["pressed"])

if __name__ == "__main__":
    App().mainloop()
