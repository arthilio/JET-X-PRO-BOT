from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from ..config.subscription_plans import PLANS
from ..database.crud import create_subscription_request

async def show_gem_tiers(update, context):
    keyboard = [
        [InlineKeyboardButton(
            f"{plan.color_hex} {plan.name} - {plan.price_eur}€",
            callback_data=f"tier_{plan.level}"
        )] for plan in PLANS
    ]
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="💎 Choisissez votre gemme :",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_subscription_callback(update, context):
    query = update.callback_query
    tier_level = int(query.data.split("_")[1])
    selected_plan = next(p for p in PLANS if p.level == tier_level)
    
    # Sauvegarde en base
    create_subscription_request(
        user_id=query.from_user.id,
        plan=selected_plan.name,
        price=selected_plan.price_eur
    )
    
    # Notification admin
    await notify_admin(context, query.from_user, selected_plan)

async def notify_admin(context, user, plan):
    admin_msg = (
        f"🆕 Demande d'abonnement {plan.name}\n"
        f"👤 Utilisateur: {user.username}\n"
        f"💶 Montant: {plan.price_eur}€\n"
        f"⏳ Durée: {plan.duration.days} jours"
    )
    
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("✅ Approuver", callback_data=f"approve_{user.id}"),
        InlineKeyboardButton("💠 Paiement Alt.", callback_data=f"altpay_{user.id}"),
        InlineKeyboardButton("❌ Rejeter", callback_data=f"reject_{user.id}")
    ]])
    
    await context.bot.send_message(
        chat_id=os.getenv("ADMIN_CHAT_ID"),
        text=admin_msg,
        reply_markup=keyboard
    )
