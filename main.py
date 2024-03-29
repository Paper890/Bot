import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Fungsi untuk menangani pesan yang diterima
def handle_message(update, context):
    message = update.message.text
    response = get_response(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Fungsi untuk mendapatkan jawaban dari pertanyaan
def get_response(message):
    if message == 'Halo':
        return 'Apa kabar? [Button1](button1)'
    elif message == 'Button1':
        return 'Saya baik. Bagaimana denganmu? [Button2](button2)'
    elif message == 'Button2':
        return 'Saya juga baik. Ada yang bisa saya bantu?'
    else:
        return 'Maaf, saya tidak dapat memahami pertanyaan Anda.'

# Inisialisasi bot
bot_token = '7090457834:AAGOVODwtJrA0II6-B8tfUGrSwJAdnbl1QY'
bot = telegram.Bot(token=bot_token)

# Inisialisasi updater dan dispatcher
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# Menambahkan handler untuk menangani pesan yang diterima
handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(handler)

# Memulai bot
updater.start_polling()
updater.idle()
