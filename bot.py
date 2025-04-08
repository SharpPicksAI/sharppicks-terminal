import os
from telegram.ext import ApplicationBuilder, CommandHandler

# Load your bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Basic /start command
async def start(update, context):
    await update.message.reply_text("Yo! SharpPicks.AI bot is now live and working!")

def main():
    # Build the bot app
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handler
    app.add_handler(CommandHandler("start", start))

    # Run it
    app.run_polling()

if __name__ == "__main__":
    main()
