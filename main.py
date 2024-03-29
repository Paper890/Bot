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
        return 'Apa kabar?'

    # Jika pertanyaan tidak ada dalam daftar jawaban yang telah diatur sebelumnya, dapat dikembalikan pesan default
    return 'Maaf, saya tidak dapat memahami pertanyaan Anda.'

# Inisialisasi bot
bot_token = '7146022048:AAFICwF67YtFwgWprOcABj9fDYhxpGQ3yU0'
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
