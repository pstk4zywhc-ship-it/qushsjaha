import telebot
from telebot import types
import base64

# توكن البوت الخاص بك
bot = telebot.TeleBot("8704063502:AAFkLjIbI2MuM2dk9rY0d7qP-yaav4w-w-w")

# رابط صفحتك
BASE_URL = "https://pstk4zywhc-ship-it.github.io/qushsjaha/"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("إنشاء رابط", callback_data="create_link")
    markup.add(btn)
    bot.send_message(message.chat.id, "أهلاً بك! اختر من القائمة:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "create_link":
        bot.send_message(call.message.chat.id, "اكتب النص الذي تريده أن يظهر في التنبيه:")
        bot.register_next_step_handler(call.message, get_text)

def get_text(message):
    # تشفير النص
    user_text_bytes = message.text.encode('utf-8')
    encoded_text = base64.b64encode(user_text_bytes).decode('utf-8')
    
    # الرابط الجديد
    final_link = f"{BASE_URL}?msg={encoded_text}"
    bot.send_message(message.chat.id, f"تم إنشاء الرابط:\n{final_link}")

if __name__ == "__main__":
    bot.infinity_polling()
