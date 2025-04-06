from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from utils.database import check_coupon_eligibility, update_coupons, check_payment_status, validate_payment

# Fonction pour démarrer le bot
def start(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    
    eligible, coupons_left_or_price = check_coupon_eligibility(user_id)
    
    if eligible:
        update.message.reply_text(f"Bienvenue ! Vous avez 10 coupons gratuits aujourd'hui. Il vous en reste {coupons_left_or_price}.")
    else:
        # Si le paiement est validé
        if coupons_left_or_price == 'validated':
            update.message.reply_text(f"Les coupons gratuits sont maintenant épuisés. Vous avez maintenant accès à des coupons payants pour 200 F CFA chacun.")
        else:
            update.message.reply_text(f"Votre paiement est en attente de validation. Veuillez me contacter directement.")

# Fonction pour utiliser un coupon (gratuit ou payant)
def use_coupon(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    
    eligible, coupons_left_or_price = check_coupon_eligibility(user_id)
    
    if eligible:
        if coupons_left_or_price > 0:
            # Utilisation d'un coupon gratuit
            update_coupons(user_id, coupons_left_or_price - 1)
            update.message.reply_text(f"Coupon utilisé avec succès ! Il vous reste {coupons_left_or_price - 1} coupons gratuits.")
        else:
            update.message.reply_text("Vous n'avez plus de coupons gratuits aujourd'hui.")
    else:
        if check_payment_status(user_id):
            update_coupons(user_id, coupons_left_or_price)  # Coupon payant validé
            update.message.reply_text(f"Coupon payant validé et utilisé !")
        else:
            update.message.reply_text("Les coupons sont désormais payants. Veuillez me contacter pour valider votre paiement.")

# Fonction pour valider un paiement manuellement
def validate(update: Update, context: CallbackContext) -> None:
    if context.args:
        user_id = context.args[0]  # ID de l'utilisateur pour validation manuelle
        validate_payment(user_id)
        update.message.reply_text(f"Le paiement de l'utilisateur {user_id} a été validé. Il peut maintenant utiliser des coupons payants.")

# Configuration du bot Telegram
def main():
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("use_coupon", use_coupon))
    dispatcher.add_handler(CommandHandler("validate", validate, pass_args=True))  # Commande pour validation manuelle
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
