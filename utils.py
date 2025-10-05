import tkinter as tk

from tkinter import ttk
from datetime import datetime

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

class DateEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="DD/MM/YYYY", **kwargs):
        super().__init__(master, **kwargs)
        
        self.placeholder = placeholder
        self._placeholder_on = True
        self.insert(0, self.placeholder)
        self.config(foreground="grey")
        
        # Eventos para placeholder
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        
        # Evento para formatação dinâmica
        self.bind("<KeyRelease>", self._format_date)

    def _on_focus_in(self, event=None):
        if self._placeholder_on:
            self.delete(0, tk.END)
            self.config(foreground="black")
            self._placeholder_on = False

    def _on_focus_out(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(foreground="grey")
            self._placeholder_on = True

    def _format_date(self, event=None):
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
        """
        Retorna a data no formato DD/MM/YYYY.
        Retorna None se estiver vazia ou placeholder ativo.
        """
        if self._placeholder_on or not self.get():
            return None
        return self.get()
