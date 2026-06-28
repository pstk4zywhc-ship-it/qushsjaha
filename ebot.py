import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# التوكن الخاص بك
TOKEN = '8704063502:AAFkLjIbI2MuM2dk9rY0d7qP-yaav4w-w-w'
bot = telebot.TeleBot(TOKEN)

# قائمة الأزرار
def get_main_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("إنشاء رابط", callback_data="create_link"))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "أهلاً بك! استخدم الزر أدناه للبدء:", reply_markup=get_main_markup())

@bot.callback_query_handler(func=lambda call: call.data == "create_link")
def ask_text(call):
    msg = bot.send_message(call.message.chat.id, "اكتب النص الذي تريده في التنبيه:")
    bot.register_next_step_handler(msg, process_link)

def process_link(message):
    user_text = message.text
    # هذا الرابط هو الرابط الوهمي الذي يظهر للمستخدم
    fake_link = f"https://alert-bot-example.onrender.com/?msg={user_text}"
    bot.send_message(message.chat.id, f"تم إنشاء الرابط بنجاح:\n{fake_link}")

# بدء تشغيل البوت
if __name__ == "__main__":
    bot.infinity_polling()
