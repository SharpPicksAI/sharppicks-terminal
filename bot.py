import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Replace this before deploying

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to SharpPicks.AI — type /buildai to start building your own system!")

async def buildai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Let’s build your custom AI betting assistant! Coming soon to your account...")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buildai", buildai))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
