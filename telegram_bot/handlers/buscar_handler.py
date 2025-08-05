# telegram_bot/handlers/buscar_handler.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode
from telegram_bot.utils.tmdb import buscar_filme_tmdb

async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Por favor, digite o nome do filme após o comando.\nExemplo: /buscar matrix")
        return

    termo = " ".join(context.args)
    await update.message.reply_text(f"🔎 Buscando por *{termo}*...", parse_mode=ParseMode.MARKDOWN)

    filme = buscar_filme_tmdb(termo)
    if not filme:
        await update.message.reply_text("⚠️ Nenhum resultado encontrado. Tente outro título.")
        return

    # Botões
    botoes = [
        [
            InlineKeyboardButton("🎞️ Ver trailer", url=f"https://www.youtube.com/results?search_query={filme['titulo']}+trailer"),
            InlineKeyboardButton("🔗 Detalhes TMDb", url=f"https://www.themoviedb.org/movie/{filme['id']}"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(botoes)

    # Mensagem com pôster (se disponível)
    legenda = f"*🎬 {filme['titulo']} ({filme['ano']})*\n\n📝 {filme['descricao'] or 'Sem sinopse disponível.'}"
    if filme["poster_url"]:
        await update.message.reply_photo(photo=filme["poster_url"], caption=legenda, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)
    else:
        await update.message.reply_text(legenda, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

def get_buscar_handler():
    return CommandHandler("buscar", buscar)

