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

LS1_TEST1, LS1_TEST2, LS1_TEST3, LS1_TEST4 = range(4)

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

lesson2_test_button = telegram.InlineKeyboardButton(text='Основи Python',callback_data='l2tb')
lesson3_test_button = telegram.InlineKeyboardButton(text='Списки в Python',callback_data='l3tb')
lesson4_test_button = telegram.InlineKeyboardButton(text='Кортежі в Python',callback_data='l4tb')
lesson5_test_button = telegram.InlineKeyboardButton(text='Цикл for і оператори розгалуження в Python',callback_data='l5tb')
lesson6_test_button = telegram.InlineKeyboardButton(text='Словники в Python',callback_data='l6tb')
lesson7_test_button = telegram.InlineKeyboardButton(text='Цикл while. Switch, Continue і Вreak в Python',callback_data='l7tb')
lesson8_test_button = telegram.InlineKeyboardButton(text='Робота з форматами типів даних, або що таке %s, %d і т.д. в Python',callback_data='l8tb')
lesson9_test_button = telegram.InlineKeyboardButton(text='Функції в Python',callback_data='l9tb')
lesson10_test_button = telegram.InlineKeyboardButton(text='Функціональне програмування. Лямбда функції.',callback_data='l10tb')
lesson11_test_button = telegram.InlineKeyboardButton(text='Робота з файлами',callback_data='l11tb')
lesson12_test_button = telegram.InlineKeyboardButton(text='Об\'єктно-орієнтоване програмування',callback_data='l12tb')
lesson13_test_button = telegram.InlineKeyboardButton(text='ООП. Спадкування',callback_data='l13tb')
lesson14_test_button = telegram.InlineKeyboardButton(text='Вийнятки в Python',callback_data='l14tb')
lesson15_test_button = telegram.InlineKeyboardButton(text='Перехід на python 3. Установка мови і вибір IDE',callback_data='l15tb')
lesson16_test_button = telegram.InlineKeyboardButton(text='Робота з базою даних SQLIte',callback_data='l16tb')


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

	buts =[[lesson2_test_button],[lesson3_test_button],[lesson4_test_button],[lesson5_test_button],[lesson6_test_button],
	[lesson7_test_button],[lesson8_test_button],[lesson9_test_button],[lesson10_test_button],[lesson11_test_button],[lesson12_test_button],
	[lesson13_test_button],[lesson14_test_button],[lesson15_test_button],[lesson16_test_button]]

	msg = '<b>Натисни на тест, який ти хочеш пройти</b>\n'
	bot.send_message(chat_id=update.message.chat_id, text=msg,
							  parse_mode=telegram.ParseMode.HTML,
							  reply_markup=telegram.InlineKeyboardMarkup(buts))

	bot.send_message(chat_id=update.message.chat_id, text='Ми робимо все можливе, щоб покращити цей розділ.', reply_markup=kb_markup) 
	tmp = update
	tmp.message.text= 'Відправив меню тестів'
	sendJSON(tmp,True)

def sendingAdditionalLinks(bot,update):
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	links1_button = telegram.InlineKeyboardButton(text='ПИТОНТЬЮТОР',url='http://pythontutor.ru/')
	links2_button = telegram.InlineKeyboardButton(text='Python. Youtube курс.',url='https://www.youtube.com/playlist?list=PL-_cKNuVAYAXkJLFpu-dq3nphjftOOR6C')
	links3_button = telegram.InlineKeyboardButton(text='Python.org',url='https://www.python.org/')

	buts =[[links1_button],[links2_button],[links3_button]]

	msg = '<b>Корисні посилання</b>\n'
	bot.send_message(chat_id=update.message.chat_id, text=msg,
							  parse_mode=telegram.ParseMode.HTML,
							  reply_markup=telegram.InlineKeyboardMarkup(buts))

	bot.send_message(chat_id=update.message.chat_id, text='Цей розділ буде доповнюватися', reply_markup=kb_markup) 
	tmp = update
	tmp.message.text= 'Відправив посилання'
	sendJSON(tmp,True)

def lesson2_testing(bot,update):
	button_list = [
        [telegram.InlineKeyboardButton("Інтерпретована мова", callback_data="r_l2t11"),
         telegram.InlineKeyboardButton("Компільована мова", callback_data="f_l2t11")]]
	update.effective_message.reply_text('Python - це?',reply_markup=telegram.InlineKeyboardMarkup(button_list))

	return LS1_TEST1

def lesson2_test_handler(bot,update,user_data):
	query_data = update.callback_query.data
	button_list = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l2t11"),
         telegram.InlineKeyboardButton("Ні", callback_data="f_l2t11")]]
	if query_data == 'r_l2t11':
		update.effective_message.reply_text('Ви відповили вірно \nЧи потрібно вказувати тип даних при створенні змінної?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
	elif query_data == 'f_l2t11':
		update.effective_message.reply_text('Ви відповили невірно \nЧи потрібно вказувати тип даних при створенні змінної?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
	user_data['selection'] = query_data
	return LS1_TEST2

def cancel_testing(bot,update):
	update.effective_message.reply_text('Тест завершено')
	return ConversationHandler.END

def callback_query_handler(bot, update):
	cqd = update.callback_query.data
	if cqd == 'l2tb':
		button_list = [
        [telegram.InlineKeyboardButton("Інтерпретована мова", callback_data="r_l2t11"),
         telegram.InlineKeyboardButton("Компільована мова", callback_data="f_l2t11")]]
		update.effective_message.reply_text('Python - це?',reply_markup=telegram.InlineKeyboardMarkup(button_list))

		return LS1_TEST1
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass
	elif cqd == 'l3tb':
		pass


test2_conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(callback_query_handler)],
        states={
            LS1_TEST1: [CallbackQueryHandler(lesson2_test_handler, pass_user_data=True)],
            LS1_TEST2: [CallbackQueryHandler(lesson2_test_handler, pass_user_data=True)],
        },
        fallbacks=[CommandHandler('cancel_testing', cancel_testing)]
)


dispatcher.add_handler(test2_conv_handler)
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