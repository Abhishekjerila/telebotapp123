# telebot_example.py
import telebot
from telebot import types

# ========== SET YOUR TOKEN ==========
TOKEN = "8220410770:AAH6bfx17hvnn8met7i1tR8oh1BAdBuH7ls"
bot = telebot.TeleBot(TOKEN)
# ====================================

# /start handler: reply keyboard with 4 options
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Reply keyboard (simple buttons)
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("⚖️ Balance")
    btn2 = types.KeyboardButton("💸 Earn money")
    btn3 = types.KeyboardButton("🎁 Bonus")
    btn4 = types.KeyboardButton("🔗 Refer and earn")
    markup.add(btn1, btn2, btn3, btn4)

    welcome_text = (
        f"👋 Hi {message.from_user.first_name}!\n\n"
        "Main aapki madad ke liye taiyar hoon.\n"
        "Niche se ek option chuniye:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Handler for text messages (button presses)
@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    text = message.text.strip().lower()

    if text == "⚖️ balance" or text == "balance":
        # Yahan real balance logic lagayein (database/API)
        bot.reply_to(message, "💰 Aapka balance: ₹0.00 (sample).")

    elif text == "💸 earn money" or text == "earn money":
        bot.reply_to(message,
                     "💡 Earn karne ke tareeke:\n"
                     "1. Daily tasks\n"
                     "2. Refer friends\n"
                     "3. Complete offers\n\n"
                     "Kisi option ke liye 'Refer and earn' chuniye ya contact karein.")

    elif text == "🎁 bonus" or text == "bonus":
        bot.reply_to(message,
                     "🎉 Aaj ka bonus: 10 coins (sample).\n"
                     "Bonus claim karne ke liye /claim likhiye (agar implemented ho).")

    elif text == "🔗 refer and earn" or text == "refer and earn":
        # Agar aap user-specific refer code chahte ho, DB se fetch karo
        user_id = message.from_user.id
        refer_code = f"REF{user_id}"  # example; replace with real logic
        bot.reply_to(message,
                     f"🔗 Aapka refer code: *{refer_code}*\n"
                     "Doston ko bhejein aur rewards paayein!",
                     parse_mode='Markdown')

    else:
        # Default fallback
        bot.reply_to(message,
                     "Maaf kijiye, mujhe samajh nahi aaya.\n"
                     "Start ke liye /start likhiye ya listed buttons use kijiye.")

# Optional: simple /balance command
@bot.message_handler(commands=['balance'])
def cmd_balance(message):
    bot.reply_to(message, "💰 Aapka balance: ₹0.00 (sample).")

# Error handling (basic)
def main():
    print("Bot started... Press Ctrl+C to stop.")
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout = 5)
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    except Exception as e:
        print("Error:", e)
        # In production, better logging + restart logic lagana chahiye

if __name__ == "__main__":
    main()
