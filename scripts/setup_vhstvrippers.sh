#!/bin/bash

echo "🛠️ Criando estrutura de pastas do projeto VHSTVRIPPERS..."

mkdir -p streamlit_app/pages
mkdir -p streamlit_app/static
mkdir -p streamlit_app/templates
mkdir -p streamlit_app/utils

mkdir -p telegram_bot/handlers
mkdir -p telegram_bot/utils

mkdir -p drive_manager
mkdir -p payment
mkdir -p database
mkdir -p shared
mkdir -p scripts

echo "📄 Criando arquivos base..."

# streamlit_app/app.py
cat <<EOF > streamlit_app/app.py
import streamlit as st

st.set_page_config(page_title="Catálogo VHSTVRIPPERS", layout="wide")
st.title("🎬 Catálogo de Filmes - VHSTVRIPPERS")

st.info("Aqui será exibido o catálogo de filmes integrado ao TheMovieDB.")
EOF

# telegram_bot/bot.py
cat <<EOF > telegram_bot/bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎥 Bem-vindo ao VHSTVRIPPERS Bot!")

app = ApplicationBuilder().token("SEU_TOKEN_AQUI").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
EOF

# shared/config.py
cat <<EOF > shared/config.py
import os
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DRIVE_FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
PIX_TOKEN = os.getenv("MERCADOPAGO_TOKEN")
EOF

# .env.example
cat <<EOF > .env.example
TMDB_API_KEY=COLE_AQUI
TELEGRAM_BOT_TOKEN=COLE_AQUI
GOOGLE_DRIVE_FOLDER_ID=COLE_AQUI
MERCADOPAGO_TOKEN=COLE_AQUI
EOF

# .gitignore
cat <<EOF > .gitignore
.env
venv_vhstvrippers/
__pycache__/
EOF

# requirements.txt
cat <<EOF > requirements.txt
streamlit
python-telegram-bot==20.3
python-dotenv
requests
pymongo
EOF

echo "✅ Estrutura criada com sucesso!"
echo "📌 Lembre-se de copiar .env.example para .env e preencher os dados."

