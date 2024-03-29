import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Fungsi untuk menangani pesan "/start"
def start_command(update, context):
    keyboard = [
        [KeyboardButton('/start')],
        [KeyboardButton('Halo')],
        [KeyboardButton('1'), KeyboardButton('2')],
        [KeyboardButton('3'), KeyboardButton('4')]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Halo! Pilih salah satu opsi berikut:', reply_markup=reply_markup)

# Fungsi untuk menangani pesan yang diterima
def handle_message(update, context):
    message = update.message.text
    response = get_response(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Fungsi untuk mendapatkan jawaban dari pertanyaan atau opsi button
def get_response(message):
    if message == 'Halo':
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
bot_token = '7090457834:AAGOVODwtJrA0II6-B8tfUGrSwJAdnbl1QY'
bot = telegram.Bot(token=bot_token)

# Inisialisasi updater dan dispatcher
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

# Menambahkan handler untuk perintah "/start"
start_handler = CommandHandler('start', start_command)
dispatcher.add_handler(start_handler)

# Menambahkan handler untuk menangani pesan yang diterima
message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(message_handler)

# Memulai bot
updater.start_polling()
updater.idle()
