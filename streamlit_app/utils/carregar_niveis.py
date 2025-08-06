import json
import os

def carregar_niveis_de_usuarios():
    """
    Carrega os dados de níveis de usuário (gamificação) a partir de um arquivo JSON.
    Compatível com execução local e Streamlit Cloud.
    """
    # Caminho relativo à raiz do projeto
    caminho_base = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    caminho_json = os.path.join(caminho_base, "data", "usuarios", "niveis.json")

    try:
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho_json}")
        return []
    except json.JSONDecodeError:
        print(f"❌ Erro ao decodificar o JSON em: {caminho_json}")
        return []

