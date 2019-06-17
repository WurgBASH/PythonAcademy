from telegram.ext import CommandHandler, MessageHandler, Filters, Updater,CallbackQueryHandler,RegexHandler,ConversationHandler,InlineQueryHandler
import telegram
from telegram import ReplyKeyboardMarkup
import requests 
import json

LS1_TEST1, LS1_TEST2, LS1_TEST3 = 1,2,3
LS2_TEST1, LS2_TEST2, LS2_TEST3, LS2_TEST4 = 4,5,6,7
LS3_TEST1, LS3_TEST2, LS3_TEST3, LS3_TEST4 = 8,9,10,11
LS4_TEST1, LS4_TEST2, LS4_TEST3, LS4_TEST4 = 12,13,14,15
LS5_TEST1, LS5_TEST2, LS5_TEST3, LS5_TEST4 = 16,17,18,19

LS6_TEST1, LS6_TEST2, LS6_TEST3, LS6_TEST4 = 20,21,22,23
LS7_TEST1, LS7_TEST2, LS7_TEST3, LS7_TEST4 = 24,25,26,27
LS8_TEST1, LS8_TEST2, LS8_TEST3, LS8_TEST4 = 28,29,30,31
LS9_TEST1, LS9_TEST2, LS9_TEST3, LS9_TEST4 = 32,33,34,35
LS10_TEST1, LS10_TEST2, LS10_TEST3, LS10_TEST4 = 36,37,38,39

LS11_TEST1, LS11_TEST2, LS11_TEST3, LS11_TEST4 = 40,41,42,43
LS12_TEST1, LS12_TEST2, LS12_TEST3, LS12_TEST4 = 44,45,46,47
LS13_TEST1, LS13_TEST2, LS13_TEST3, LS13_TEST4 = 48,49,50,51
LS14_TEST1, LS14_TEST2, LS14_TEST3, LS14_TEST4 = 52,53,54,55
LS15_TEST1, LS15_TEST2, LS15_TEST3, LS15_TEST4 = 56,57,58,59

def sendStatisticJSON(lesson):
	data = {'lesson_id':lesson}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url = 'https://flaskappprogram.herokuapp.com/getJSONLessons', data=json.dumps(data), headers=headers)	

def checkingWrite3(user_data):
	s = ''
	if (user_data['1'] and user_data['2'] and user_data['3']):
		s='Ви відповили вірно на всі питання в тесті.\nДякуємо за вашу уважність!'
	if (not user_data['1'] and not user_data['2'] and not user_data['3']):
		s='Ви відповили невірно на всі питання в тесті.\nПрочитайте 2 урок знову!'
	elif (user_data['1'] and user_data['2'] and not user_data['3']):
		s='Ви відповили вірно лише на перше та друге питання.\nВи молодець!'
	elif (user_data['1'] and user_data['3'] and not user_data['2']):
		s='Ви відповили вірно лише на перше та третє питання.\nВи молодець!'
	elif (user_data['2'] and user_data['3'] and not user_data['1']):
		s='Ви відповили вірно лише на друге та третє питання.\nВи молодець!'
	elif (user_data['1']):
		s='Ви відповили вірно лише на перше питання.\nПрочитайте 2 урок знову!'
	elif (user_data['2']):
		s='Ви відповили вірно лише на друге питання.\nПрочитайте 2 урок знову!'
	elif (user_data['3']):
		s='Ви відповили вірно лише на третє питання.\nПрочитайте 2 урок знову!'
	return s

def checkingWrite4(user_data, lesson):
	s = ''
	if (user_data['1'] and user_data['2'] and user_data['3'] and user_data['4']):
		s='Ви відповили вірно на всі питання в тесті.\nДякуємо за вашу уважність!'
	elif(not user_data['1'] and not user_data['2'] and not user_data['3'] and not user_data['4']):
		s='Ви відповили невірно на всі питання в тесті.\nПрочитайте '+str(lesson)+' урок знову!'
	elif(user_data['1'] and user_data['2'] and user_data['3'] and not user_data['4']):
		s='Ви відповили вірно на 1,2,3 питання в тесті.\nВи молодець!'
	elif (user_data['2'] and user_data['3'] and user_data['4'] and not user_data['1']):
		s='Ви відповили вірно на 2,3,4 питання в тесті.\nВи молодець!'
	elif (user_data['3'] and user_data['4'] and user_data['1'] and not user_data['2']):
		s='Ви відповили вірно на 1,3,4 питання в тесті.\nВи молодець!'
	elif(user_data['1'] and user_data['2'] and user_data['4'] and not user_data['3']):
		s='Ви відповили вірно на 1,2,4 питання в тесті.\nВи молодець!'
	elif (user_data['1'] and user_data['2'] and not user_data['3'] and not user_data['4']):
		s='Ви відповили вірно на перше та друге питання в тесті.\nЦе непоганий результат!'
	elif (user_data['3'] and user_data['4'] and not user_data['1'] and not user_data['2']):
		s='Ви відповили вірно на третє та четверте питання в тесті.\nЦе непоганий результат!'
	elif (user_data['3'] and user_data['1'] and not user_data['4'] and not user_data['2']):
		s='Ви відповили вірно на перше та третє питання в тесті.\nЦе непоганий результат!'
	elif (user_data['4'] and user_data['1'] and not user_data['3'] and not user_data['2']):
		s='Ви відповили вірно на перше та четверте питання в тесті.\nЦе непоганий результат!'
	elif (user_data['2'] and user_data['4'] and not user_data['1'] and not user_data['3']):
		s='Ви відповили вірно на друге та четверте питання в тесті.\nЦе непоганий результат!'
	elif (user_data['3'] and user_data['2'] and not user_data['1'] and not user_data['4']):
		s='Ви відповили вірно на друге та третє питання в тесті.\nЦе непоганий результат!'
	elif (user_data['1'] and not user_data['2'] and not user_data['3'] and not user_data['4']):
		s='Ви відповили вірно лише на перше питання в тесті.\nПрочитайте '+str(lesson)+' урок знову!'
	elif (user_data['2'] and not user_data['3'] and not user_data['4'] and not user_data['1']):
		s='Ви відповили вірно лише на друге питання в тесті.\nПрочитайте '+str(lesson)+' урок знову!'
	elif (user_data['3'] and not user_data['4'] and not user_data['1'] and not user_data['2']):
		s='Ви відповили вірно лише на третє питання в тесті.\nПрочитайте '+str(lesson)+' урок знову!'
	elif (user_data['4'] and not user_data['1'] and not user_data['2'] and not user_data['3']):
		s='Ви відповили вірно лише на четверте питання в тесті.\nПрочитайте '+str(lesson)+' урок знову!'
	return s

#-------------------Основи-------------
def lesson2_test_handler(bot,update,user_data):
	query_data = update.callback_query.data
	button_list1 = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l2t2"),
         telegram.InlineKeyboardButton("Ні", callback_data="f_l2t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list2 = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l2t3"),
         telegram.InlineKeyboardButton("Ні", callback_data="f_l2t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l2t1':
		update.effective_message.reply_text('Ви відповили вірно \nЧи потрібно вказувати тип даних при створенні змінної?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS1_TEST2
	elif query_data == 'f_l2t1':
		update.effective_message.reply_text('Ви відповили невірно \nЧи потрібно вказувати тип даних при створенні змінної?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS1_TEST2
	elif query_data == 'r_l2t2':
		update.effective_message.reply_text('Ви відповили вірно \nЧи можна множити рядки в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS1_TEST3
	elif query_data == 'f_l2t2':
		update.effective_message.reply_text('Ви відповили невірно \nЧи можна множити рядки в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS1_TEST3
	elif query_data == 'r_l2t3':
		user_data['3'] = True
		update.effective_message.reply_text(checkingWrite3(user_data))
		return ConversationHandler.END
	elif query_data == 'f_l2t3':
		user_data['3'] = False
		update.effective_message.reply_text(checkingWrite3(user_data))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END


#-------------------Список-------------
def lesson3_test_handler(bot,update,user_data):
	query_data = update.callback_query.data
	button_list1 = [
        [telegram.InlineKeyboardButton("reverse()", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("count()", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("find()", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list2 = [
        [telegram.InlineKeyboardButton("Всі елементи, крім останнього", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Останній елемент списку", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("\'список\' стане першим елементом списку", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Кожен символ стане елементом списку", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Буде помилка", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЯкий із цих методів не є базовим для списку?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS2_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЯкий із цих методів не є базовим для списку?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS2_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЩо виведе даний код print(list[:-1]), list-це створений список?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS2_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЩо виведе даний код print(list[:-1]), list-це створений список?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS2_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЩо буде в результаті виконання list(\'список\')?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS2_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЩо буде в результаті виконання list(\'список\')?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS2_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END
	
#-------------------Кортеж-------------
def lesson4_test_handler(bot,update,user_data):
	query_data = update.callback_query.data
	button_list2 = [
        [telegram.InlineKeyboardButton("create()", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("tuple()", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("cortege()", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list1 = [
        [telegram.InlineKeyboardButton("Список", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Кортеж", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Кортеж перетвориться на список", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("Нічого не відбудеться", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Буде помилка", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЩо займає менше пам\'яті?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS3_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЩо займає менше пам\'яті?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS3_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЯка функція є аналогом list() для кортежу?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS3_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЯка функція є аналогом list() для кортежу?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS3_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЩо буде, якщо передати в list() кортеж?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS3_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЩо буде, якщо передати в list() кортеж?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS3_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END


#-------------Цикл for і оператори розгалуження-------------
def lesson5_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("Створює список розміром 4 ", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Виводить зі списку 4 значення", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("for x in list", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("foreach x in list", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("for (var x; x != list.end(); x++)", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("efil", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("elif", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("if else", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЩо робить функція range(4)?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS4_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЩо робить функція range(4)?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS4_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЯк перебрати список в циклі?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS4_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЯк перебрати список в циклі?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS4_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЯкий аналог else if в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS4_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЯкий аналог else if в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS4_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#-------------Словники-------------
def lesson6_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("HASH-таблицях", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("RSA-шифрі", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Видаляє", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Добавляє", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Створює словник", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("select", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("in", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("fromkeys", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nНа чому реалізовані словники?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS5_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nНа чому реалізовані словники?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS5_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЩо робить функція pop()?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS5_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЩо робить функція pop()?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS5_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЗа допомогою якого оператора можно перевірити чи є в словнику ключ?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS5_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЗа допомогою якого оператора можно перевірити чи є в словнику ключ?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS5_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------Цикл while. Switch, Continue і Вreak в Python-------------
def lesson7_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("Завершує цикл", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Пропускає ітерацію", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Використання elif", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Використання While", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Використання For", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Генерує числа", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("Перебирає масив", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Створює список", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЩо робить оператор Break?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS6_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЩо робить оператор Break?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS6_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЩо замінив Switch?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS6_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЩо замінив Switch?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS6_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЩо виконує цикл for i in range(3,7)?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS6_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЩо виконує цикл for i in range(3,7)?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS6_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------Робота з форматами типів даних-------------
def lesson8_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("\'d\'", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("\'i\'", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("hi, Max", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("hi, User=Max", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("hi, \"Max\"", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Зліва заповнює пробілами", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("Справа заповнює пробілами", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Добавляє пробіли в середину", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЯкий новий аналог \'u\'?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS7_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЯкий новий аналог \'u\'?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS7_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЩо виведе User = "Max" print(\'hi, %s!\' % \'User\')?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS7_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЩо виведе User = "Max" print(\'hi, %s!\' % \'User\')?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS7_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nДля чого потрібен прапор "+"?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS7_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nДля чого потрібен прапор "+"?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS7_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------Функції в Python-------------
def lesson9_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("def", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("function", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Опис функції", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Строка в функції", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Тип даних в Python", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Функції є об'єктами", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Функції є процедурами", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("У функцій є параметри", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЯке ключове слово функції?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS8_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЯке ключове слово функції?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS8_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЩо таке докстрока?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS8_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЩо таке докстрока?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS8_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЯке із тверджень не є вірним?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS8_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЯке із тверджень не є вірним?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS8_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------Функціональне програмування-------------
def lesson10_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Ні", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Приймають інші функції", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Повертають кілька значень", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Не мають return", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("functools", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("functions", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("maxfunc", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nLambda функція не вимагає return?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS9_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nLambda функція не вимагає return?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS9_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nФункції вищих порядків...',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS9_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nФункції вищих порядків...',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS9_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЯкий модуль є модулем фунцій вищих порядків?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS9_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЯкий модуль є модулем фунцій вищих порядків?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS9_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------Робота з файлами-------------
def lesson11_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("Відкриває та записує файл", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Відкриває та повертає потік", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Відносний", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Простий", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Відносний і Абсолютний", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Режим відкриття файла", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("Просто набір букв", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Типи даних", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЩо робить функція open(file, mode = \'r\', buffering = None, encoding = None, errors = None, newline = None, closefd = True)?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS10_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЩо робить функція open(file, mode = \'r\', buffering = None, encoding = None, errors = None, newline = None, closefd = True)?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS10_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЯкий буває шлях до файлу?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS10_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЯкий буває шлях до файлу?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS10_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЩо означає r,w,x,a,b,t,+?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS10_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЩо означає r,w,x,a,b,t,+?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS10_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------Об'єктно-орієнтоване програмування-------------
def lesson12_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("Ні", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("2", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("3", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("4", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Типу", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Пам\'яті", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Значення", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЧи можна привласнити глобальній змінній всередині функції?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS11_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЧи можна привласнити глобальній змінній всередині функції?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS11_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nСкільки є принципів ООП?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS11_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nСкільки є принципів ООП?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS11_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nКожен об\'єкт має все, ОКРІМ',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS11_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nКожен об\'єкт має все, ОКРІМ',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS11_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------ООП. Спадкування-------------
def lesson13_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Ні", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Ні", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Лише деякі", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Два", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("Жодного", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Три", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЧи треба явно вказувати імя класу для доступу до методу батька?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS12_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЧи треба явно вказувати імя класу для доступу до методу батька?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS12_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЧи є всі методи віртуальними?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS12_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЧи є всі методи віртуальними?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS12_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nСкільки параметрів приймає функція super?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS12_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nСкільки параметрів приймає функція super?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS12_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------Винятки в Python-------------
def lesson14_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Ні", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Завершує свое виконання", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Продовжує роботу", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Виводить повідомлення і продовжує роботу", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Типи помилок", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("Помилки", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Кількість помилок", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЧи потрібно обробляти всі винятки?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS13_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЧи потрібно обробляти всі винятки?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS13_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nУ момент появи синтаксичної помилки програма?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS13_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nУ момент появи синтаксичної помилки програма?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS13_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЩо перераховується в блоці except?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LLS13_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЩо перераховується в блоці except?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS13_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#----------Перехід на python 3-------------
def lesson15_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("3", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("2", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Так", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Ні", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("print \"Hi\"", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("print(\"Hi\")", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("print Hi", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЯка з гілок мови Pyton зараз набирає популярність?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS14_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЯка з гілок мови Pyton зараз набирає популярність?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS14_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЧи було введено багато синтаксичних змін в  Pyton3?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS14_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЧи було введено багато синтаксичних змін в  Pyton3?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS14_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЯкий із цих синтаксисів вірний в Python 3?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS14_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЯкий із цих синтаксисів вірний в Python 3?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS14_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END

#-------Робота з базою даних SQLIte-------------
def lesson16_test_handler(bot,update,user_data):
	query_data = update.callback_query.data

	button_list1 = [
        [telegram.InlineKeyboardButton("Без логіна і пароля", callback_data="r_l3t2")],
        [telegram.InlineKeyboardButton("Через логін і пароль", callback_data="f_l3t2")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
	
	button_list2 = [
        [telegram.InlineKeyboardButton("Назву файлу", callback_data="f_l3t3")],
        [telegram.InlineKeyboardButton("Розташування файлу", callback_data="r_l3t3")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	button_list3 = [
        [telegram.InlineKeyboardButton("Нічого не відбудеться", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Автоматично створиться", callback_data="r_l3t4")],
        [telegram.InlineKeyboardButton("Буде помилка", callback_data="f_l3t4")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]

	if query_data == 'r_l3t1':
		update.effective_message.reply_text('Ви відповили вірно \nЯк підключитися до баз даних SQLite?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = True
		return LS15_TEST2
	elif query_data == 'f_l3t1':
		update.effective_message.reply_text('Ви відповили невірно \nЯк підключитися до баз даних SQLite?',reply_markup=telegram.InlineKeyboardMarkup(button_list1))
		user_data['1'] = False
		return LS15_TEST2
	elif query_data == 'r_l3t2':
		update.effective_message.reply_text('Ви відповили вірно \nЩо треба вказати для підключення до файлу з даними бази?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = True
		return LS15_TEST3
	elif query_data == 'f_l3t2':
		update.effective_message.reply_text('Ви відповили невірно \nЩо треба вказати для підключення до файлу з даними бази?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS15_TEST3
	elif query_data == 'r_l3t3':
		update.effective_message.reply_text('Ви відповили вірно \nЯкщо немає бази даних до якої ми звертаємося, то?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = True
		return LS15_TEST4
	elif query_data == 'f_l3t3':
		update.effective_message.reply_text('Ви відповили невірно \nЯкщо немає бази даних до якої ми звертаємося, то?',reply_markup=telegram.InlineKeyboardMarkup(button_list3))
		user_data['3'] = False
		return LS15_TEST4
	elif query_data == 'r_l3t4':
		user_data['4'] = True
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'f_l3t4':
		user_data['4'] = False
		update.effective_message.reply_text(checkingWrite4(user_data,3))
		return ConversationHandler.END
	elif query_data == 'testend':
		update.effective_message.reply_text('Тест завершено')
		return ConversationHandler.END


def cancel_testing(bot,update):
	update.effective_message.reply_text('Тест завершено')
	return ConversationHandler.END

def callback_query_handler(bot, update):
	cqd = update.callback_query.data
	kb = [[telegram.KeyboardButton('Повернутися до головного меню')]]
	kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)
	msg = '⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠\n<b>Ви розпочали тестування, будьте уважними, на кожний тест відведено 120 секунд.</b>\n⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠\nЯкщо ви не завершили тест, введіть команду /stop_testing'
	if cqd == 'l2tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Інтерпретована мова", callback_data="r_l2t1")],
        [telegram.InlineKeyboardButton("Компільована мова", callback_data="f_l2t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Python - це?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(1)
		return LS1_TEST1
	elif cqd == 'l3tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t1"),
        telegram.InlineKeyboardButton("Ні", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Список може зберігати різні типи данних?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(2)
		return LS2_TEST1
	elif cqd == 'l4tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Незмінний список", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("Незмінний массив", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Кортеж це?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(3)
		return LS3_TEST1
	elif cqd == 'l5tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("if", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("else if", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("elif", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Якого оператора розгалуження не існує в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(4)
		return LS4_TEST1
	elif cqd == 'l6tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t1"),
        telegram.InlineKeyboardButton("Ні", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Словник може зберігати вкладені словники?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(5)
		return LS5_TEST1
	elif cqd == 'l7tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Пропускає певну ділянку коду", callback_data="r_l3t1"),
        telegram.InlineKeyboardButton("Продовжує цикл з наступної ітерації", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Навіщо потрібен в циклі оператор - continue?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(6)
		return LS6_TEST1
	elif cqd == 'l8tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Конвертує об\'єкт в число", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Конвертує об\'єкт в рядок", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("Конвертує об\'єкт в символ", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Що означає оператор \'s\'?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(7)
		return LS7_TEST1
	elif cqd == 'l9tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t1"),
        telegram.InlineKeyboardButton("Ні", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('В Python є процедура?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(8)
		return LS8_TEST1
	elif cqd == 'l10tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Функція без назви", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("Процедура в Python", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("Функція, яка повертає 1 символ", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Що таке лямбда функція?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(9)
		return LS9_TEST1
	elif cqd == 'l11tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("\'x\'", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("\'rt\'", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("\'t\'", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Який за замовчуванням режим при відкритті файлів?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(10)
		return LS10_TEST1
	elif cqd == 'l12tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("3", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("6", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("2", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Скільки областей видимості існує?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(11)
		return LS11_TEST1
	elif cqd == 'l13tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Основи об'єктного програмування", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Об'єктно-орієнтоване проектування", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Об'єктно-орієнтоване програмування", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('ООП - це?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(12)
		return LS12_TEST1
	elif cqd == 'l14tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Тип даних", callback_data="r_l3t1")],
        [telegram.InlineKeyboardButton("Клас", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Що таке виняток?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(13)
		return LS13_TEST1
	elif cqd == 'l15tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("2", callback_data="r_l3t1"),
        telegram.InlineKeyboardButton("5", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Скільки існує гілок в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(14)
		return LS14_TEST1
	elif cqd == 'l16tb':
		bot.send_message(chat_id=update.callback_query.message.chat_id, text=msg,parse_mode=telegram.ParseMode.HTML, reply_markup=kb_markup) 
		button_list = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l3t1"),
        telegram.InlineKeyboardButton("Ні", callback_data="f_l3t1")],
        [telegram.InlineKeyboardButton("Завершити тест", callback_data="testend")]]
		update.effective_message.reply_text('Чи існує база даних в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		sendStatisticJSON(15)
		return LS15_TEST1
	else:
		return ConversationHandler.END


test_conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(callback_query_handler)],
        states={
            LS1_TEST1: [CallbackQueryHandler(lesson2_test_handler, pass_user_data=True)],
            LS1_TEST2: [CallbackQueryHandler(lesson2_test_handler, pass_user_data=True)],
            LS1_TEST3: [CallbackQueryHandler(lesson2_test_handler, pass_user_data=True)],

            LS2_TEST1: [CallbackQueryHandler(lesson3_test_handler, pass_user_data=True)],
            LS2_TEST2: [CallbackQueryHandler(lesson3_test_handler, pass_user_data=True)],
            LS2_TEST3: [CallbackQueryHandler(lesson3_test_handler, pass_user_data=True)],
            LS2_TEST4: [CallbackQueryHandler(lesson3_test_handler, pass_user_data=True)],
            
            LS3_TEST1: [CallbackQueryHandler(lesson4_test_handler, pass_user_data=True)],
            LS3_TEST2: [CallbackQueryHandler(lesson4_test_handler, pass_user_data=True)],
            LS3_TEST3: [CallbackQueryHandler(lesson4_test_handler, pass_user_data=True)],
            LS3_TEST4: [CallbackQueryHandler(lesson4_test_handler, pass_user_data=True)],
            
            LS4_TEST1: [CallbackQueryHandler(lesson5_test_handler, pass_user_data=True)],
            LS4_TEST2: [CallbackQueryHandler(lesson5_test_handler, pass_user_data=True)],
            LS4_TEST3: [CallbackQueryHandler(lesson5_test_handler, pass_user_data=True)],
            LS4_TEST4: [CallbackQueryHandler(lesson5_test_handler, pass_user_data=True)],
            
            LS5_TEST1: [CallbackQueryHandler(lesson6_test_handler, pass_user_data=True)],
            LS5_TEST2: [CallbackQueryHandler(lesson6_test_handler, pass_user_data=True)],
            LS5_TEST3: [CallbackQueryHandler(lesson6_test_handler, pass_user_data=True)],
            LS5_TEST4: [CallbackQueryHandler(lesson6_test_handler, pass_user_data=True)],
            
            LS6_TEST1: [CallbackQueryHandler(lesson7_test_handler, pass_user_data=True)],
            LS6_TEST2: [CallbackQueryHandler(lesson7_test_handler, pass_user_data=True)],
            LS6_TEST3: [CallbackQueryHandler(lesson7_test_handler, pass_user_data=True)],
            LS6_TEST4: [CallbackQueryHandler(lesson7_test_handler, pass_user_data=True)],
            
            LS7_TEST1: [CallbackQueryHandler(lesson8_test_handler, pass_user_data=True)],
            LS7_TEST2: [CallbackQueryHandler(lesson8_test_handler, pass_user_data=True)],
            LS7_TEST3: [CallbackQueryHandler(lesson8_test_handler, pass_user_data=True)],
            LS7_TEST4: [CallbackQueryHandler(lesson8_test_handler, pass_user_data=True)],
            
            LS8_TEST1: [CallbackQueryHandler(lesson9_test_handler, pass_user_data=True)],
            LS8_TEST2: [CallbackQueryHandler(lesson9_test_handler, pass_user_data=True)],
            LS8_TEST3: [CallbackQueryHandler(lesson9_test_handler, pass_user_data=True)],
            LS8_TEST4: [CallbackQueryHandler(lesson9_test_handler, pass_user_data=True)],
            
            LS9_TEST1: [CallbackQueryHandler(lesson10_test_handler, pass_user_data=True)],
            LS9_TEST2: [CallbackQueryHandler(lesson10_test_handler, pass_user_data=True)],
            LS9_TEST3: [CallbackQueryHandler(lesson10_test_handler, pass_user_data=True)],
            LS9_TEST4: [CallbackQueryHandler(lesson10_test_handler, pass_user_data=True)],
            
            LS10_TEST1: [CallbackQueryHandler(lesson11_test_handler, pass_user_data=True)],
            LS10_TEST2: [CallbackQueryHandler(lesson11_test_handler, pass_user_data=True)],
            LS10_TEST3: [CallbackQueryHandler(lesson11_test_handler, pass_user_data=True)],       
            LS10_TEST4: [CallbackQueryHandler(lesson11_test_handler, pass_user_data=True)],

            LS11_TEST1: [CallbackQueryHandler(lesson12_test_handler, pass_user_data=True)],
            LS11_TEST2: [CallbackQueryHandler(lesson12_test_handler, pass_user_data=True)],
            LS11_TEST3: [CallbackQueryHandler(lesson12_test_handler, pass_user_data=True)],
            LS11_TEST4: [CallbackQueryHandler(lesson12_test_handler, pass_user_data=True)],

            LS12_TEST1: [CallbackQueryHandler(lesson13_test_handler, pass_user_data=True)],
            LS12_TEST2: [CallbackQueryHandler(lesson13_test_handler, pass_user_data=True)],
            LS12_TEST3: [CallbackQueryHandler(lesson13_test_handler, pass_user_data=True)],
            LS12_TEST4: [CallbackQueryHandler(lesson13_test_handler, pass_user_data=True)],

            LS13_TEST1: [CallbackQueryHandler(lesson14_test_handler, pass_user_data=True)],
            LS13_TEST2: [CallbackQueryHandler(lesson14_test_handler, pass_user_data=True)],
            LS13_TEST3: [CallbackQueryHandler(lesson14_test_handler, pass_user_data=True)],
            LS13_TEST4: [CallbackQueryHandler(lesson14_test_handler, pass_user_data=True)],

            LS14_TEST1: [CallbackQueryHandler(lesson15_test_handler, pass_user_data=True)],
            LS14_TEST2: [CallbackQueryHandler(lesson15_test_handler, pass_user_data=True)],
            LS14_TEST3: [CallbackQueryHandler(lesson15_test_handler, pass_user_data=True)],
            LS14_TEST4: [CallbackQueryHandler(lesson15_test_handler, pass_user_data=True)],

            LS15_TEST1: [CallbackQueryHandler(lesson16_test_handler, pass_user_data=True)],
            LS15_TEST2: [CallbackQueryHandler(lesson16_test_handler, pass_user_data=True)],
            LS15_TEST3: [CallbackQueryHandler(lesson16_test_handler, pass_user_data=True)],
            LS15_TEST4: [CallbackQueryHandler(lesson16_test_handler, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('stop_testing', cancel_testing)],conversation_timeout=120
)