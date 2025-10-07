import json
import os

class AppContext:
    _instance = None
    _file_path = os.path.expanduser("~/.app_context.json")  # arquivo para persistência opcional

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.usuario_logado = None
            cls._instance.escala = 1.0
            cls._instance._carregar()
        return cls._instance

    def salvar(self):
        """Salva o contexto atual em um arquivo JSON (opcional)."""
        data = {
            "usuario_logado": self.usuario_logado,
            "escala": self.escala,
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
            except Exception:
                # Arquivo corrompido ou ilegível — ignora
                pass


# Função de acesso global
def get_context() -> AppContext:
    """Retorna a instância global única do contexto da aplicação."""
    return AppContext()
