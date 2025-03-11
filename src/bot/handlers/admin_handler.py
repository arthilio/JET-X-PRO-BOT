from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from ..database.crud import approve_subscription, log_admin_action

async def handle_admin_actions(update, context):
    query = update.callback_query
    action, user_id = query.data.split("_")[1:3]
    
    if action == "approve":
        await approve_subscription(user_id)
        await send_user_confirmation(context, user_id)
        log_admin_action("APPROVE", user_id)
        
    elif action == "altpay":
        await propose_alt_payment(context, user_id)
        log_admin_action("ALT_PAYMENT", user_id)

async def propose_alt_payment(context, user_id):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("Crypto", callback_data=f"setpay_{user_id}_crypto"),
        InlineKeyboardButton("Virement", callback_data=f"setpay_{user_id}_wire")
    ]])
    
    await context.bot.send_message(
        chat_id=os.getenv("ADMIN_CHAT_ID"),
        text="🔧 Choisissez un mode de paiement alternatif :",
        reply_markup=keyboard
    )

async def send_user_confirmation(context, user_id):
    await context.bot.send_message(
        chat_id=user_id,
        text="🎉 Votre abonnement premium a été activé !\n"
             "Accédez à vos privilèges exclusifs dès maintenant."
    )
