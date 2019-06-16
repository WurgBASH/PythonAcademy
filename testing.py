from telegram.ext import CommandHandler, MessageHandler, Filters, Updater,CallbackQueryHandler,RegexHandler,ConversationHandler
import telegram
from telegram import ReplyKeyboardMarkup

LS1_TEST1, LS1_TEST2, LS1_TEST3 = range(3)
LS2_TEST1, LS2_TEST2, LS2_TEST3, LS2_TEST4 = range(4)
LS3_TEST1, LS3_TEST2, LS3_TEST3, LS3_TEST4 = range(4)


def checkingWrite3(bot,update,user_data):
	if (user_data['1'] and user_data['2'] and user_data['3']):
		update.effective_message.reply_text('Ви відповили вірно на всі питання в тесті.\nДякуємо за вашу уважність!')
	elif (user_data['1'] and user_data['2'] and not user_data['3']):
		update.effective_message.reply_text('Ви відповили вірно лише на перше та друге питання.\nВи молодець!')
	elif (user_data['1'] and user_data['3'] and not user_data['2']):
		update.effective_message.reply_text('Ви відповили вірно лише на перше та третє питання.\nВи молодець!')
	elif (user_data['2'] and user_data['3'] and not user_data['1']):
		update.effective_message.reply_text('Ви відповили вірно лише на друге та третє питання.\nВи молодець!')
	elif (user_data['1']):
		update.effective_message.reply_text('Ви відповили вірно лише на перше питання.\nПрочитайте 1 урок знову!')
	elif (user_data['2']):
		update.effective_message.reply_text('Ви відповили вірно лише на друге питання.\nПрочитайте 1 урок знову!')
	elif (user_data['3']):
		update.effective_message.reply_text('Ви відповили вірно лише на третє питання.\nПрочитайте 1 урок знову!')
	return ConversationHandler.END

def lesson2_test_handler(bot,update,user_data):
	query_data = update.callback_query.data
	button_list1 = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l2t2"),
         telegram.InlineKeyboardButton("Ні", callback_data="f_l2t2")]]

	button_list2 = [
        [telegram.InlineKeyboardButton("Так", callback_data="r_l2t3"),
         telegram.InlineKeyboardButton("Ні", callback_data="f_l2t3")]]

	if query_data == 'r_l2t1':
		update.effective_message.reply_text('Ви відповили вірно \nЧи потрібно вказувати тип даних при створенні змінної?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		user_data['1'] = True
		return LS1_TEST2
	elif query_data == 'f_l2t1':
		update.effective_message.reply_text('Ви відповили невірно \nЧи потрібно вказувати тип даних при створенні змінної?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		user_data['1'] = False
		return LS1_TEST2
	elif query_data == 'r_l2t2':
		update.effective_message.reply_text('Ви відповили вірно \nЧи можна множити рядки в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list))
		user_data['2'] = True
		return LS1_TEST3
	elif query_data == 'f_l2t2':
		update.effective_message.reply_text('Ви відповили невірно \nЧи можна множити рядки в Python?',reply_markup=telegram.InlineKeyboardMarkup(button_list2))
		user_data['2'] = False
		return LS1_TEST3
	elif query_data == 'r_l2t3':
		user_data['3'] = True
		checkingWrite3(bot,update,user_data)
	elif query_data == 'f_l2t3':
		user_data['3'] = False
		checkingWrite3(bot,update,user_data)
	

def cancel_testing(bot,update):
	update.effective_message.reply_text('Тест завершено')
	return ConversationHandler.END

def callback_query_handler(bot, update):
	cqd = update.callback_query.data
	if cqd == 'l2tb':
		button_list = [
        [telegram.InlineKeyboardButton("Інтерпретована мова", callback_data="r_l2t1"),
         telegram.InlineKeyboardButton("Компільована мова", callback_data="f_l2t1")]]
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
            LS1_TEST3: [CallbackQueryHandler(lesson2_test_handler, pass_user_data=True)]
        },
        fallbacks=[CommandHandler('cancel_testing', cancel_testing)]
)
