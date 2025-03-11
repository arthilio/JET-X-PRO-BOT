import os
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from .handlers import subscription_handler, admin_handler
from .database import init_db

async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🌟 Bienvenue au Club des Gemmes Précieuses 🌟"
    )

def main():
    # Initialisation
    init_db()
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(subscription_handler.handle_subscription_callback))
    app.add_handler(CallbackQueryHandler(admin_handler.handle_admin_actions))
    
    app.run_polling()

if __name__ == "__main__":
    main()
