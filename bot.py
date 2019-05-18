from telegram.ext import CommandHandler, MessageHandler, Filters, Updater,CallbackQueryHandler,RegexHandler,ConversationHandler
import telegram
from telegram import ReplyKeyboardMarkup
import threading,os,sys,socket
import apiai, json
from googletrans import Translator
import time
from flask import Flask, Response, redirect, request, url_for

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

app = Flask(__name__)
text12 ='Начало'

@app.route('/')
def index():
	if request.headers.get('accept') == 'text/event-stream':
		time.sleep(2)
		def events():
			global text12
			if text12 != 'None':
				yield "data: %s\n\n" % (text12)
				text12='None'
		return Response(events(), content_type='text/event-stream')
	return redirect(url_for('static', filename='index.html'))

def main_menu(bot, update):
	kb = [[telegram.KeyboardButton('Список уроків')],
			[telegram.KeyboardButton('Тестування')],
			[telegram.KeyboardButton('Посилання на додаткові матеріали')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)

	bot.send_message(chat_id=update.message.chat_id,
					text="Ти хочеш вивчачи Python?",
					reply_markup=kb_markup) 

def handle_message(bot, update):
	global text12
	global_id=1
	text12=update.message.chat.first_name+": "+update.message.text
	print(text12)
	if update.message.text == 'Список уроків':
		sendingAllLessons(bot, update)
		index()
	elif update.message.text == 'Тестування':
		sendingTestingMenu(bot,update)
		index()
	elif update.message.text == 'Посилання на додаткові матеріали':
		sendingAdditionalLinks(bot,update)
		index()
	elif update.message.text == 'Повернутися до головного меню':
		main_menu(bot, update)
		index()
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
			index()
		else:
			bot.send_message(chat_id=update.message.chat_id, text='Я вас не розумію!')
			index()
		

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

# def parsering():
# 	app.run()

# def sending():
# 	updater.start_polling()
# 	#updater.idle()

if __name__ == '__main__':
	#--------------------------------
	# t1 = threading.Thread(target=sending)
	# t2 = threading.Thread(target=parsering)
	# t1.start()
	# t2.start()
	
	
	#--------------------------------
	updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
	updater.bot.set_webhook("https://python1academy.herokuapp.com/" + TOKEN)
	updater.idle()
	app.run()