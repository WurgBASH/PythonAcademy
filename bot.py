from telegram.ext import CommandHandler, MessageHandler, Filters, Updater,CallbackQueryHandler,RegexHandler,ConversationHandler
import telegram
from telegram import ReplyKeyboardMarkup
import os,sys
import apiai, json
from googletrans import Translator
import time
import requests 
import testing
import lessons_data

TOKEN = "710118383:AAFJuBvAtwZ4yWvkjdmBGL6pZb6ocP4e0S4"
PORT = int(os.environ.get('PORT', '8443'))

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
translator = Translator()


def main_menu(bot, update):
	kb = [[telegram.KeyboardButton('Список уроків')],
			[telegram.KeyboardButton('Тестування')],
			[telegram.KeyboardButton('Посилання на додаткові матеріали')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)

	bot.send_message(chat_id=update.message.chat_id,
					text="Ти хочеш вивчачи Python?",
					reply_markup=kb_markup)
	tmp = update
	tmp.message.text= 'Відправив головне меню'
	sendJSON(tmp,True) 

def handle_message(bot, update):
	if update.message.text == 'Список уроків':
		sendJSON(update,False)
		sendingAllLessons(bot, update)
	elif update.message.text == 'Тестування':
		sendJSON(update,False)
		sendingTestingMenu(bot,update)
	elif update.message.text == 'Посилання на додаткові матеріали':
		sendJSON(update,False)
		sendingAdditionalLinks(bot,update)
	elif update.message.text == 'Повернутися до головного меню':
		sendJSON(update,False)
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
			sendJSON(update,False)
			tmp = update
			tmp.message.text= msg
			sendJSON(tmp,True)
		else:
			bot.send_message(chat_id=update.message.chat_id, text='Я вас не розумію!')
			sendJSON(update,False)
			tmp = update
			tmp.message.text= 'Я вас не розумію!'
			sendJSON(tmp,True)

def sendJSON(update, bot):
	if bot:
		data = {'bot_bool':'bot','user_id':update.message.chat_id,'user_nick':update.message.chat.username,'user_name': update.message.chat.first_name, 'message_text': update.message.text}
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(url = 'https://flaskappprogram.herokuapp.com/getJSONBOTfromBot', data=json.dumps(data), headers=headers)	
	else:
		data = {'user_id':update.message.chat_id,'user_nick':update.message.chat.username,'user_name': update.message.chat.first_name, 'message_text': update.message.text}
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		r = requests.post(url = 'https://flaskappprogram.herokuapp.com/getJSONfromBot', data=json.dumps(data), headers=headers)

def sendingAllLessons(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	msg = '<b>Натисни на урок, який ти хочеш вивчити</b>\n'
	bot.send_message(chat_id=update.message.chat_id, text=msg,
							  parse_mode=telegram.ParseMode.HTML,
							  reply_markup=telegram.InlineKeyboardMarkup(lessons_data.lessons_buts))

	bot.send_message(chat_id=update.message.chat_id, text='Для кращого вивчення потрібно прочитати всі уроки', reply_markup=kb_markup) 
	tmp = update
	tmp.message.text= 'Відправив меню уроків'
	sendJSON(tmp,True)


def sendingTestingMenu(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	msg = '<b>Натисни на тест, який ти хочеш пройти</b>\n'
	bot.send_message(chat_id=update.message.chat_id, text=msg,
							  parse_mode=telegram.ParseMode.HTML,
							  reply_markup=telegram.InlineKeyboardMarkup(lessons_data.test_buts))

	bot.send_message(chat_id=update.message.chat_id, text='Ми робимо все можливе, щоб покращити цей розділ.', reply_markup=kb_markup) 
	tmp = update
	tmp.message.text= 'Відправив меню тестів'
	sendJSON(tmp,True)

def sendingAdditionalLinks(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	

	msg = '<b>Корисні посилання</b>\n'
	bot.send_message(chat_id=update.message.chat_id, text=msg,
							  parse_mode=telegram.ParseMode.HTML,
							  reply_markup=telegram.InlineKeyboardMarkup(lessons_data.link_buts))

	bot.send_message(chat_id=update.message.chat_id, text='Цей розділ буде доповнюватися', reply_markup=kb_markup) 
	tmp = update
	tmp.message.text= 'Відправив посилання'
	sendJSON(tmp,True)

def lessons_query_handler(bot, update):
	pass


dispatcher.add_handler(testing.test2_conv_handler)
dispatcher.add_handler(CommandHandler('start', main_menu))
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
dispatcher.add_handler(CallbackQueryHandler(lessons_query_handler))
dispatcher.add_handler(CallbackQueryHandler(testing.callback_query_handler))
if __name__ == '__main__':
	#--------------------------------
	# updater.start_polling()
	# updater.idle()
	#--------------------------------
	updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
	updater.bot.set_webhook("https://python1academy.herokuapp.com/" + TOKEN)
	updater.idle()