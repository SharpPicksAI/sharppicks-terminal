import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load your bot token securely from environment
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Responds to /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yo! SharpPicks.AI bot is now live and working!")

def main():
    # Build the Telegram bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add the /start command
    app.add_handler(CommandHandler("start", start))

    # Run the bot
    app.run_polling()

if __name__ == "__main__":
    main()
