import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext
)
from core.prediction import generate_prediction
from core.risk import check_risk
from utils.database import Database

# Configuration initiale
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class JetXBot:
    def __init__(self):
        self.db = Database(os.getenv("DATABASE_URL"))
        self.app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
        
        # Handlers
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def start(self, update: Update, context: CallbackContext):
        user = update.effective_user
        self.db.create_user(user.id)
        await update.message.reply_text(f"🛡️ Bienvenue {user.first_name} !\nLimite de perte quotidienne : 15 000 FCFA")

    async def handle_message(self, update: Update, context: CallbackContext):
        user_id = update.effective_user.id
        prediction = generate_prediction(user_id)
        
        if check_risk(user_id):
            await update.message.reply_text(f"🎯 Prédiction : {prediction['multiplier']}x | Confiance : {prediction['confidence']}%")
        else:
            await update.message.reply_text("🚨 Limite de risque atteinte ! Consultez /stats")

if __name__ == '__main__':
    bot = JetXBot()
    bot.app.run_polling()
