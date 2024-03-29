import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, MessageHandler, Filters

# Fungsi untuk menangani pesan yang diterima
def handle_message(update, context):
    message = update.message.text
    response = get_response(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Fungsi untuk mendapatkan jawaban dari pertanyaan atau opsi button
def get_response(message):
    if message == '/start':
        return 'Halo! Pilih salah satu opsi berikut:'
    elif message == 'Halo':
        return 'Apa kabar?'
    elif message == '1':
        return 'Anda memilih opsi 1'
    elif message == '2':
        return 'Anda memilih opsi 2'
    elif message == '3':
        return 'Anda memilih opsi 3'
    elif message == '4':
        return 'Anda memilih opsi 4'
    else:
        return 'Maaf, saya tidak dapat memahami pertanyaan atau opsi Anda.'

# Inisialisasi bot
bot_token = 'TOKEN_BOT_TELEGRAM_ANDA'
bot = telegram.Bot(token=bot_token)

# Inisialisasi updater dan dispatcher
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# Menambahkan handler untuk menangani pesan yang diterima
handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(handler)

# Menambahkan opsi button
keyboard = [
    [KeyboardButton('Halo')],
    [KeyboardButton('1'), KeyboardButton('2')],
    [KeyboardButton('3'), KeyboardButton('4')]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Memulai bot dan mengirim pesan pertama dengan opsi button
updater.start_polling()
bot.send_message(chat_id=CHAT_ID_ANDA, text='Halo! Pilih salah satu opsi berikut:', reply_markup=reply_markup)
updater.idle()
