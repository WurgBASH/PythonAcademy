from telegram.ext import CommandHandler, MessageHandler, Filters, Updater,CallbackQueryHandler,RegexHandler,ConversationHandler
import telegram
from telegram import ReplyKeyboardMarkup
import os,sys
import apiai, json
from googletrans import Translator
import time
import requests 

TOKEN = "710118383:AAFJuBvAtwZ4yWvkjdmBGL6pZb6ocP4e0S4"
PORT = int(os.environ.get('PORT', '8443'))

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
translator = Translator()

l1_cqd = 'L1BUT'
l2_cqd = 'L2BUT'

lesson1_button = telegram.InlineKeyboardButton(text='Як встановити Python?',url="https://telegra.ph/YAk-vstanoviti-Python-05-13")
lesson2_button = telegram.InlineKeyboardButton(text='Основи Python',url="https://telegra.ph/Osnovi-Python-05-16")
lesson3_button = telegram.InlineKeyboardButton(text='Рядки в Python',url="https://telegra.ph/Ryadki-v-Python-05-16")

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
	elif update.message.text == 'Повернутися до головного меню':
		main_menu(bot, update)
	else:
		request = apiai.ApiAI('a60c7793525a40ac9b5876bfef6590d3').text_request() 
		request.lang = 'ru' 
		request.session_id = 'BatlabAIBot' 
		request.query = update.message.text 
		responseJson = json.loads(request.getresponse().read().decode('utf-8'))
		response = responseJson['result']['fulfillment']['speech']
		msg = translator.translate(response, dest='ukrainian',src='ru').text
		if response:
			bot.send_message(chat_id=update.message.chat_id, text=msg)
		else:
			bot.send_message(chat_id=update.message.chat_id, text='Я вас не розумію!')
	requests.post(url = 'https://flaskappprogram.herokuapp.com/getJSONfromBot', data = {'data':update.message.text}) 
	
def sendingAllLessons(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	buts =[[lesson1_button],[lesson2_button],[lesson3_button]]
	msg = '<b>Натисни на урок, який ти хочеш вивчити</b>\n'
	bot.send_message(chat_id=update.message.chat_id, text=msg,
							  parse_mode=telegram.ParseMode.HTML,
							  reply_markup=telegram.InlineKeyboardMarkup(buts))

	bot.send_message(chat_id=update.message.chat_id, text='Для кращого вивчення потрібно прочитати всі уроки', reply_markup=kb_markup) 


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
	#--------------------------------
	# updater.start_polling()
	# updater.idle()
	#--------------------------------
	updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
	updater.bot.set_webhook("https://python1academy.herokuapp.com/" + TOKEN)
	updater.idle()