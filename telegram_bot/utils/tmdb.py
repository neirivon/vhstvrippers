# telegram_bot/utils/tmdb.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def buscar_filme_tmdb(titulo: str):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": titulo,
        "language": "pt-BR"
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
        "poster_url": f"https://image.tmdb.org/t/p/w500{filme.get('poster_path')}" if filme.get("poster_path") else None,
        "id": filme.get("id")
    }

