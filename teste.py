import tkinter as tk
from tkinter import messagebox

def novo():
    messagebox.showinfo("Novo", "Novo arquivo criado!")

def abrir():
    messagebox.showinfo("Abrir", "Abrindo arquivo...")

def sair():
    root.quit()

def sobre():
    messagebox.showinfo("Sobre", "Exemplo de uso do Menu no Tkinter")

# janela principal
root = tk.Tk()
root.title("Exemplo Menu")
root.geometry("400x300")

# cria a barra de menu
menubar = tk.Menu(root)

# menu "Arquivo"
menu_arquivo = tk.Menu(menubar, tearoff=0)   # tearoff=0 remove a linha tracejada no topo
menu_arquivo.add_command(label="Novo", command=novo)
menu_arquivo.add_command(label="Abrir", command=abrir)
menu_arquivo.add_separator()  # linha separadora
menu_arquivo.add_command(label="Sair", command=sair)
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)

# menu "Ajuda"
menu_ajuda = tk.Menu(menubar, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=sobre)
menubar.add_cascade(label="Ajuda", menu=menu_ajuda)

# aplica o menu na janela principal
root.config(menu=menubar)

root.mainloop()
