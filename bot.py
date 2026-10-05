import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name or "Friend"

    bot.send_message(
        message.chat.id,
        f"🎉 Welcome to Earningv5, {name}!\n\n"
        "💰 Complete tasks and earn money.\n"
        "👥 Invite friends and earn referral bonuses.\n"
        "💳 Withdraw your available balance.\n\n"
        "🚀 Your Earningv5 dashboard is coming soon!"
    )


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "🆘 Earningv5 Help\n\n"
        "• /start — Start the bot\n"
        "• /help — Get help\n\n"
        "💡 More features are coming soon!"
    )


print("Earningv5 Bot is running...")

bot.infinity_polling()
