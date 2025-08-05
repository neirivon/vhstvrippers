# telegram_bot/bot.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from shared.config import TELEGRAM_TOKEN

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Bem-vindo ao bot VHSTVRIPPERS!\n\nUse o comando /buscar <nome do filme> para encontrar um título.")

# Comando /buscar <nome>
async def buscar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Por favor, forneça o nome do filme.\nExemplo: /buscar matrix")
        return

    termo = " ".join(context.args)
    await update.message.reply_text(f"🔍 Buscando: *{termo}*...\n(Em breve: resultado real via TMDb ou Plex)", parse_mode="Markdown")

# Iniciar o bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buscar", buscar))
    print("🤖 Bot VHSTVRIPPERS está rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()

