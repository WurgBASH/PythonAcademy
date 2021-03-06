import telegram

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

lesson1_button = telegram.InlineKeyboardButton(text='Як встановити Python?',callback_data='l1',url=lessons_url[0])
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

lessons_buts =[[lesson1_button],[lesson2_button],[lesson3_button],[lesson4_button],[lesson5_button],[lesson6_button],
	[lesson7_button],[lesson8_button],[lesson9_button],[lesson10_button],[lesson11_button],[lesson12_button],
	[lesson13_button],[lesson14_button],[lesson15_button],[lesson16_button]]

test_buts =[[lesson2_test_button],[lesson3_test_button],[lesson4_test_button],[lesson5_test_button],[lesson6_test_button],
	[lesson7_test_button],[lesson8_test_button],[lesson9_test_button],[lesson10_test_button],[lesson11_test_button],[lesson12_test_button],
	[lesson13_test_button],[lesson14_test_button],[lesson15_test_button],[lesson16_test_button]]

links1_button = telegram.InlineKeyboardButton(text='ПИТОНТЬЮТОР',url='http://pythontutor.ru/')
links2_button = telegram.InlineKeyboardButton(text='Python. Youtube курс.',url='https://www.youtube.com/playlist?list=PL-_cKNuVAYAXkJLFpu-dq3nphjftOOR6C')
links3_button = telegram.InlineKeyboardButton(text='Python.org',url='https://www.python.org/')

link_buts =[[links1_button],[links2_button],[links3_button]]