# telegram_bot/utils/tmdb.py

import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do .env
load_dotenv()

# Variáveis do .env
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = os.getenv("TMDB_BASE_URL", "https://api.themoviedb.org/3")
TMDB_IMAGE_URL = os.getenv("TMDB_IMAGE_URL", "https://image.tmdb.org/t/p/w500")
TMDB_LANG = os.getenv("TMDB_LANG", "pt-BR")

def buscar_filme_tmdb(titulo: str):
    url = f"{TMDB_BASE_URL}/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": titulo,
        "language": TMDB_LANG
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None

    resultados = response.json().get("results")
    if not resultados:
        return None

    filme = resultados[0]  # Pega o primeiro resultado
    return {
        "titulo": filme.get("title"),
        "ano": filme.get("release_date", "")[:4],
        "descricao": filme.get("overview"),
        "poster_url": f"{TMDB_IMAGE_URL}{filme.get('poster_path')}" if filme.get("poster_path") else None,
        "id": filme.get("id")
    }

