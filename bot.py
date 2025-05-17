import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from testbook_mock import get_mock_test_html, get_analysis_html

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Download Mock Test", callback_data='download')],
        [InlineKeyboardButton("Download Analysis", callback_data='analysis')],
    ]
    await update.message.reply_text("Welcome to Testbook Mock Bot!", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'download':
        file_path = get_mock_test_html()
        await context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_path, 'rb'))
    elif query.data == 'analysis':
        file_path = get_analysis_html()
        await context.bot.send_document(chat_id=update.effective_chat.id, document=open(file_path, 'rb'))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_button))

if __name__ == "__main__":
    app.run_polling()