import tkinter as tk

from tkinter import ttk
from datetime import datetime

from model.model_base import ResponseQuery

def tratar_data_sql(data_str: str) -> str:
    if not data_str:
        return None
    data_str = data_str.strip()
    formatos = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d"]
    for f in formatos:
        try:
            dt = datetime.strptime(data_str, f)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None

import tkinter as tk
import ttkbootstrap as ttk
from datetime import datetime

class DateEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="DD/MM/YYYY", **kwargs):
        super().__init__(master, **kwargs)
        
        self.placeholder = placeholder
        self._placeholder_on = False  # agora começa com uma data válida
        
        # Define a data atual como valor padrão
        self.set_today()
        
        # Eventos para placeholder e formatação
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        self.bind("<KeyRelease>", self._format_date)

    def set_today(self):
        """Define a data atual no campo."""
        hoje = datetime.now().strftime("%d/%m/%Y")
        self.delete(0, ttk.END)
        self.insert(0, hoje)
        self.config(foreground="black")
        self._placeholder_on = False

    def _on_focus_in(self, event=None):
        """Remove o texto cinza do placeholder ao focar."""
        if self._placeholder_on:
            self.delete(0, tk.END)
            self.config(foreground="black")
            self._placeholder_on = False

    def _on_focus_out(self, event=None):
        """Se o campo estiver vazio, insere a data atual."""
        if not self.get().strip() or self._placeholder_on:
            self.set_today()

    def _format_date(self, event=None):
        """Formata dinamicamente a entrada de data (DD/MM/YYYY)."""
        if self._placeholder_on:
            return
        
        s = self.get()
        digits = [c for c in s if c.isdigit()]
        new_s = ""
        
        for i, d in enumerate(digits):
            if i == 2 or i == 4:
                new_s += "/"
            new_s += d
            if i >= 7:
                break
        self.delete(0, tk.END)
        self.insert(0, new_s)

    def get_date(self):
        """Retorna a data no formato DD/MM/YYYY."""
        if self._placeholder_on or not self.get().strip():
            return datetime.now().strftime("%d/%m/%Y")
        return self.get()

def print_response_query(resp: ResponseQuery):
    print(f'resposta: ok?{resp.ok()} | erros: {resp.erros} | retorno: {resp.retorno}')
