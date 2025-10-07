import ttkbootstrap as ttk
import tkinter as tk

from tkinter import ttk
from datetime import datetime

def tratar_data_sql(data_str: str) -> str:
    if not data_str:
        return None
    data_str = data_str.strip()
    
    # Formatos com e sem hora
    formatos = [
        "%d/%m/%Y %H:%M:%S",
        "%d/%m/%Y %H:%M",
        "%d/%m/%Y",
        "%d-%m-%Y %H:%M:%S",
        "%d-%m-%Y %H:%M",
        "%d-%m-%Y",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M",
        "%Y/%m/%d",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d"
    ]
    
    for f in formatos:
        try:
            dt = datetime.strptime(data_str, f)
            # Retorna no formato SQL com hora, se não houver hora adiciona 00:00:00
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    return None

class DateEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="DD/MM/YYYY", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self._placeholder_on = False
        
        # Armazena data e hora separadas
        self.data = datetime.now().date()
        self.hora = datetime.now().time().replace(microsecond=0)
        
        # Mostra apenas data no Entry
        self.set_today()
        
        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)
        self.bind("<KeyRelease>", self._format_date)

    def set_today(self):
        """Define a data atual no campo (apenas DD/MM/YYYY)."""
        self.data = datetime.now().date()
        self.hora = datetime.now().time().replace(microsecond=0)
        hoje = self.data.strftime("%d/%m/%Y")
        self.delete(0, tk.END)
        self.insert(0, hoje)
        self.config(foreground="black")
        self._placeholder_on = False

    def _on_focus_in(self, event=None):
        if self._placeholder_on:
            self.delete(0, tk.END)
            self.config(foreground="black")
            self._placeholder_on = False

    def _on_focus_out(self, event=None):
        if not self.get().strip() or self._placeholder_on:
            self.set_today()

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

    def update_datetime(self):
        """Atualiza os atributos self.data e self.hora com base no Entry."""
        s = self.get().strip()
        if not s:
            self.set_today()
            return

        try:
            dt = datetime.strptime(s, "%d/%m/%Y")
            self.data = dt.date()
            # Mantém a hora atual
            self.hora = datetime.now().time().replace(microsecond=0)
        except ValueError:
            # Se não for uma data válida, mantém valores antigos
            pass

    def get_date(self) -> str:
        """Retorna apenas a data no formato DD/MM/YYYY"""
        self.update_datetime()
        return self.data.strftime("%d/%m/%Y")

    def get_time(self) -> str:
        """Retorna apenas a hora no formato HH:MM:SS"""
        self.update_datetime()
        return self.hora.strftime("%H:%M:%S")

    def get_datetime(self) -> str:
        """Retorna data e hora juntos: DD/MM/YYYY HH:MM:SS"""
        self.update_datetime()
        return f"{self.get_date()} {self.get_time()}"

def print_response_query(resp):
    print(f'resposta: ok?{resp.ok()} | erros: {resp.erros} | retorno: {resp.retorno}')
