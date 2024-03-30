import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
# Fungsi untuk membaca jawaban dari file .txt
def read_answer_from_file(file_path):
    with open(file_path, 'r') as file:
        answer = file.read()
    return answer
# Fungsi untuk menangani pesan yang diterima oleh bot
def handle_message(update, context):
    message = update.message.text.lower()
    if message == "/start":
        # Membuat keyboard inline
        keyboard = [[InlineKeyboardButton("SSH", callback_data='ssh'),
                     InlineKeyboardButton("VMESS", callback_data='vmess'),
                     InlineKeyboardButton("VLESS", callback_data='vless'),
                     InlineKeyboardButton("TROJAN", callback_data='trojan')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Mengirim pesan dengan keyboard inline
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Halo selamat datang, silahkan pilih Paket nya di bawah",
                                 reply_markup=reply_markup)
# Fungsi untuk menangani tombol yang ditekan dalam keyboard inline
def handle_button(update, context):
    query = update.callback_query
    if query.data == 'ssh':
        answer = read_answer_from_file('ssh.txt')
        context.bot.send_message(chat_id=query.message.chat_id, text=answer)
    elif query.data == 'vmess':
        answer = read_answer_from_file('vmess.txt')
        context.bot.send_message(chat_id=query.message.chat_id, text=answer)
    elif query.data == 'vless':
        answer = read_answer_from_file('vless.txt')
        context.bot.send_message(chat_id=query.message.chat_id, text=answer)
    elif query.data == 'trojan':
        answer = read_answer_from_file('trojan.txt')
        context.bot.send_message(chat_id=query.message.chat_id, text=answer)
# Inisialisasi bot dan menambahkan handler untuk pesan dan tombol
bot = telegram.Bot(token='7090457834:AAGOVODwtJrA0II6-B8tfUGrSwJAdnbl1QY')
updater = Updater(bot=bot, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.dispatcher.add_handler(CallbackQueryHandler(handle_button))
# Memulai bot
updater.start_polling()
updater.idle()
