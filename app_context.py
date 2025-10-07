import json
import os
from tkinter import font

class AppContext:
    _instance = None
    _file_path = os.path.expanduser("~/.app_context.json")  # caminho do arquivo de configuração

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.usuario_logado = None
            cls._instance.proporcao = 0.75
            cls._instance.escala = 1.0
            cls._instance._font_family = "Arial"
            cls._instance._font_size = int(12 * cls._instance.escala)
            cls._instance.entry_font = font.Font(family=cls._instance._font_family,
                                                 size=cls._instance._font_size)
            cls._instance._carregar()
            cls._instance.atualizar_fonte(cls._instance.escala)
        return cls._instance

    def salvar(self):
        """Salva o contexto atual em um arquivo JSON."""
        data = {
            "usuario_logado": self.usuario_logado,
            "escala": self.escala,
            "proporcao": self.proporcao,
            "font_family": self.entry_font.cget("family"),
            "font_size": self.entry_font.cget("size"),
        }
        with open(self._file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def _carregar(self):
        """Carrega o contexto salvo anteriormente, se existir."""
        if os.path.exists(self._file_path):
            try:
                with open(self._file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                self.usuario_logado = data.get("usuario_logado")
                self.escala = data.get("escala", 1.0)
                self.proporcao = data.get("proporcao", 0.75)

                # Lê os dados da fonte, se existirem
                self._font_family = data.get("font_family", "Arial")
                self._font_size = data.get("font_size", int(12 * self.escala))

                # Cria a fonte compartilhada
                self.entry_font = font.Font(family=self._font_family,
                                            size=self._font_size)
            except Exception as e:
                print(f"Erro ao carregar contexto: {e}")

    def atualizar_fonte(self, escala: float = None):
        """Atualiza a fonte conforme a escala atual ou informada."""
        if escala is not None:
            self.escala = escala
        novo_tamanho = max(int(12 * self.escala), 1)
        self.entry_font.configure(size=novo_tamanho)
        self.salvar()


# Função global
def get_context() -> AppContext:
    """Retorna a instância global única do contexto da aplicação."""
    return AppContext()
