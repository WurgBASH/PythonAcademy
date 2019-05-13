from telegram.ext import CommandHandler, MessageHandler, Filters, Updater,CallbackQueryHandler
import telegram
import datetime
from datetime import timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os,sys

TOKEN = "710118383:AAFJuBvAtwZ4yWvkjdmBGL6pZb6ocP4e0S4"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def main_menu(bot, update):
	kb = [[telegram.KeyboardButton('Список уроків')],
			[telegram.KeyboardButton('Тестування')],
			[telegram.KeyboardButton('Посилання на додаткові матеріали')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)

	bot.send_message(chat_id=update.message.chat_id,
					text="Ти хочеш вивчачи Python?",
					reply_markup=kb_markup) 

def handle_message(bot, update):
	if update.message.text == 'Список уроків':
		
	elif update.message.text == 'Тестування':

	elif update.message.text == 'Посилання на додаткові матеріали':

	elif update.message.text == 'Тестування':

dispatcher.add_handler(CommandHandler('start', main_menu))
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

if __name__ == '__main__':
	updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
	updater.bot.set_webhook("https://python1academy.herokuapp.com/" + TOKEN)
	updater.idle()