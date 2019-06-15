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

lessons_url = ['https://telegra.ph/YAk-vstanoviti-Python-05-13',
'https://telegra.ph/Osnovi-Python-05-16',
'https://telegra.ph/Spiski-v-Python-05-17',
'https://telegra.ph/Kortezh%D1%96-v-Python-05-17',
'https://telegra.ph/Cikl-for-%D1%96-operatori-rozgaluzhennya-v-Python-05-17',
'https://telegra.ph/Slovniki-v-Python-05-17',
'https://telegra.ph/Cikl-while-Switch-Continue-%D1%96-Vreak-v-Python-05-17',
'https://telegra.ph/Robota-z-formatami-tip%D1%96v-danih-abo-shcho-take--s-d-%D1%96-td-v-Python-05-17',
'https://telegra.ph/Funkc%D1%96i-v-Python-06-15',
'https://telegra.ph/Funkc%D1%96onalne-programuvannya-Lyambda-funkc%D1%96i-06-15',
'https://telegra.ph/Robota-z-fajlami-06-15',
'https://telegra.ph/Obyektno-or%D1%96yentovane-programuvannya-06-15',
'https://telegra.ph/OOP-Spadkuvannya-06-15',
'https://telegra.ph/Vinyatki-v-Python-06-15',
'https://telegra.ph/Pereh%D1%96d-na-python-3-Ustanovka-movi-%D1%96-vib%D1%96r-IDE-06-15',
'https://telegra.ph/Robota-z-bazoyu-danih-SQLIte-06-15'
]

lesson1_button = telegram.InlineKeyboardButton(text='Як встановити Python?',url=lessons_url[0])
lesson2_button = telegram.InlineKeyboardButton(text='Основи Python',url=lessons_url[1])
lesson3_button = telegram.InlineKeyboardButton(text='Списки в Python',url=lessons_url[2])
lesson4_button = telegram.InlineKeyboardButton(text='Кортежі в Python',url=lessons_url[3])
lesson5_button = telegram.InlineKeyboardButton(text='Цикл for і оператори розгалуження в Python',url=lessons_url[4])
lesson6_button = telegram.InlineKeyboardButton(text='Словники в Python',url=lessons_url[5])
lesson7_button = telegram.InlineKeyboardButton(text='Цикл while. Switch, Continue і Вreak в Python',url=lessons_url[6])
lesson8_button = telegram.InlineKeyboardButton(text='Робота з форматами типів даних, або що таке %s, %d і т.д. в Python',url=lessons_url[7])
lesson9_button = telegram.InlineKeyboardButton(text='Функції в Python',url=lessons_url[8])
lesson10_button = telegram.InlineKeyboardButton(text='Функціональне програмування. Лямбда функції.',url=lessons_url[9])
lesson11_button = telegram.InlineKeyboardButton(text='Робота з файлами',url=lessons_url[10])
lesson12_button = telegram.InlineKeyboardButton(text='Об\'єктно-орієнтоване програмування',url=lessons_url[11])
lesson13_button = telegram.InlineKeyboardButton(text='ООП. Спадкування',url=lessons_url[12])
lesson14_button = telegram.InlineKeyboardButton(text='Вийнятки в Python',url=lessons_url[13])
lesson15_button = telegram.InlineKeyboardButton(text='Перехід на python 3. Установка мови і вибір IDE',url=lessons_url[14])
lesson16_button = telegram.InlineKeyboardButton(text='Робота з базою даних SQLIte',url=lessons_url[15])



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

	buts =[[lesson1_button],[lesson2_button],[lesson3_button],[lesson4_button],[lesson5_button],[lesson6_button],
	[lesson7_button],[lesson8_button],[lesson9_button],[lesson10_button],[lesson11_button],[lesson12_button],
	[lesson13_button],[lesson14_button],[lesson15_button],[lesson16_button]]

	msg = '<b>Натисни на урок, який ти хочеш вивчити</b>\n'
	bot.send_message(chat_id=update.message.chat_id, text=msg,
							  parse_mode=telegram.ParseMode.HTML,
							  reply_markup=telegram.InlineKeyboardMarkup(buts))

	bot.send_message(chat_id=update.message.chat_id, text='Для кращого вивчення потрібно прочитати всі уроки', reply_markup=kb_markup) 
	tmp = update
	tmp.message.text= 'Відправив меню уроків'
	sendJSON(tmp,True)


def sendingTestingMenu(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	bot.send_message(chat_id=update.message.chat_id, text='Цей модуль ще не написаний',
					reply_markup=kb_markup) 
	tmp = update
	tmp.message.text= 'Відправив меню тестів'
	sendJSON(tmp,True)

def sendingAdditionalLinks(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	bot.send_message(chat_id=update.message.chat_id, text='Цей модуль ще не написаний',
					reply_markup=kb_markup) 
	tmp = update
	tmp.message.text= 'Відправив посилання'
	sendJSON(tmp,True)


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
руддщ	# updater.idle()
	#--------------------------------
	updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
	updater.bot.set_webhook("https://python1academy.herokuapp.com/" + TOKEN)
	updater.idle()