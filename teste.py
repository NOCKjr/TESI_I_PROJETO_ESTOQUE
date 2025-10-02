import tkinter as tk

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

iniciar_janela()
