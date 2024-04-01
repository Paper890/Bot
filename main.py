from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext
# Fungsi untuk membaca token bot dari file teks
def read_token_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
# Fungsi untuk menangani perintah /start
def start(update: Update, context: CallbackContext):
    # Opsi menu yang akan ditampilkan dalam format 2x2
    menu = [
        [
            InlineKeyboardButton("SSH", callback_data='menu1'),
            InlineKeyboardButton("VMESS", callback_data='menu2')
        ],
        [
            InlineKeyboardButton("VLESS", callback_data='menu3'),
            InlineKeyboardButton("TROJAN", callback_data='menu4')
        ]
    ]
    # Membuat markup keyboard untuk menampilkan opsi menu
    reply_markup = InlineKeyboardMarkup(menu)
    update.message.reply_text("───────────────────────\n"
                              "       🤖 Bot Massage By SAN 🤖\n"
                              "───────────────────────\n"
                              "Silahkan Pilih akun Kamu Di Bawah :)",
                              reply_markup=reply_markup)
# Fungsi untuk menangani pemrosesan ketika opsi menu dipilih
def menu_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    # Memproses opsi menu yang dipilih
    if query.data == 'menu1':
        menu1_text = get_text_from_file("sanvpn.txt")
        query.edit_message_text(text=menu1_text)
    elif query.data == 'menu2':
        menu2_text = get_text_from_file("vmess.txt")
        query.edit_message_text(text=menu4_text)
    elif query.data == 'menu3':
        menu3_text = get_text_from_file("vless.txt")
        query.edit_message_text(text=menu2_text)
    elif query.data == 'menu4':
        menu4_text = get_text_from_file("trojan.txt")
        query.edit_message_text(text=menu4_text)
def get_text_from_file(filename):
    with open(filename, "r") as file:
        text = file.read()
    return text
def main():
    # Membaca token bot dari file teks
    token = read_token_from_file('token_bot.txt')
    # Token bot Telegram yang diperoleh dari file teks
    updater = Updater(token, use_context=True)
    # Mendapatkan dispatcher untuk mendaftarkan handler
    dp = updater.dispatcher
    # Menambahkan handler untuk perintah /start
    dp.add_handler(CommandHandler("start", start))
    # Menambahkan handler untuk pemrosesan opsi menu
    dp.add_handler(CallbackQueryHandler(menu_callback))
    # Memulai bot
    updater.start_polling()
    # Menunggu bot berjalan hingga dihentikan secara manual
    updater.idle()
if __name__ == '__main__':
    main()
