from telegram.ext import CommandHandler, MessageHandler, Filters, Updater,CallbackQueryHandler
import os,sys

TOKEN = "710118383:AAFJuBvAtwZ4yWvkjdmBGL6pZb6ocP4e0S4"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

l1_cqd = 'L1BUT'
lesson1_button = telegram.InlineKeyboardButton(text='Як встановити Python?',callback_data=l1_cqd)

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
		sendingAllLessons(bot, update)
	elif update.message.text == 'Тестування':
		sendingTestingMenu(bot,update)
	elif update.message.text == 'Посилання на додаткові матеріали':
		sendingAdditionalLinks(bot,update)

def sendingAllLessons(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	buts =[lesson1_button]
	msg = '<b>Натисни на урок, який ти хочеш вивчити</b>\n'
	bot.send_message(chat_id=update.message.chat_id, text=msg,
							  parse_mode=telegram.ParseMode.HTML,
							  reply_markup=telegram.InlineKeyboardMarkup([buts]),
							  reply_markup=kb_markup) 


def sendingTestingMenu(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	bot.send_message(chat_id=update.message.chat_id, text='Цей модуль ще не написаний',
					reply_markup=kb_markup) 

def sendingAdditionalLinks(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	bot.send_message(chat_id=update.message.chat_id, text='Цей модуль ще не написаний',
					reply_markup=kb_markup) 


def callback_query_handler(bot, update):
	cqd = update.callback_query.data
	if cqd == l1_cqd:
		bot.send_message(chat_id=update.callback_query.message.chat_id,
					text="https://telegra.ph/YAk-vstanoviti-Python-05-13") 
		

dispatcher.add_handler(CommandHandler('start', main_menu))
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
dispatcher.add_handler(CallbackQueryHandler(callback_query_handler))
if __name__ == '__main__':
	updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
	updater.bot.set_webhook("https://python1academy.herokuapp.com/" + TOKEN)
	updater.idle()