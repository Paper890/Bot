from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

TOKEN = "6474341901:AAFlu-jiIXzz_4nESufZ7E1ZkkSkJTYkoNg"
REGISTERED_IDS_FILE = "registered_ids.txt"

# Fungsi untuk membaca file teks dan mengembalikan daftar ID chat yang terdaftar
def read_registered_ids():
    registered_ids = []
    with open(REGISTERED_IDS_FILE, "r") as file:
        for line in file:
            registered_ids.append(line.strip())
    return registered_ids

# Fungsi untuk menambahkan ID chat ke file teks
def add_registered_id(id_chat):
    with open(REGISTERED_IDS_FILE, "a") as file:
        file.write(str(id_chat) + "\n")

# Fungsi untuk menangani perintah /start
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("DASBOARD", callback_data='dashboard')],
        [InlineKeyboardButton("ORDER", callback_data='order')],
        [InlineKeyboardButton("ID CHAT", callback_data='id_chat')],
        [InlineKeyboardButton("KONTAK ADMIN", callback_data='kontak_admin')],
        [InlineKeyboardButton("Tambah Izin ID", callback_data='add_permission')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Silakan pilih opsi di bawah ini:', reply_markup=reply_markup)

# Fungsi untuk menangani callback dari tombol yang ditekan
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'order':
        keyboard = [
            [InlineKeyboardButton("LITE", callback_data='lite'),
             InlineKeyboardButton("BASIC", callback_data='basic'),
             InlineKeyboardButton("XTRA", callback_data='xtra')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Pilih paket yang diinginkan:", reply_markup=reply_markup)
    elif query.data == 'id_chat':
        query.edit_message_text(text=f"ID Chat Anda: {query.message.chat_id}")
    elif query.data == 'kontak_admin':
        query.edit_message_text(text="Kontak Admin: admin@example.com")
    elif query.data == 'dashboard':
        registered_ids = read_registered_ids()
        if str(query.message.chat_id) in registered_ids:
            query.edit_message_text(text="Anda memiliki akses ke Dashboard.")
        else:
            query.edit_message_text(text="Anda tidak memiliki akses ke Dashboard.")
    elif query.data == 'add_permission':
        query.edit_message_text(text="Silakan kirimkan ID chat yang ingin ditambahkan melalui pesan teks.")

    elif query.data in ['lite', 'basic', 'xtra']:
        id_chat = query.message.chat_id
        jenis_paket = query.data.upper()
        price = get_price(jenis_paket)  # Fungsi untuk mendapatkan harga berdasarkan jenis paket
        message = f"""MENGATUR PESANAN UNTUK ID: {id_chat}
PRICE: {price}
JENIS: {jenis_paket}

Salin Chat ini Dan kirim ke Admin @Sanmaxx"""
        query.edit_message_text(text=message)

# Fungsi untuk menangani pesan teks yang mengandung ID chat yang ingin ditambahkan
def add_permission(update: Update, context: CallbackContext):
    id_chat = update.message.text.strip()
    add_registered_id(id_chat)
    update.message.reply_text("ID chat telah ditambahkan.")

def get_price(paket):
    # Fungsi untuk mendapatkan harga berdasarkan jenis paket
    if paket == 'LITE':
        return "3000"
    elif paket == 'BASIC':
        return "5000"
    elif paket == 'XTRA':
        return "10000"
    else:
        return "Harga paket belum ditentukan"

def main():
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, add_permission))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
