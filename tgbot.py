import telebot
from telebot import types

#Author @Lani_Ka_Nani

token=''
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id,"Привет! Ознакомиться с функциями бота и его описанием можно, введя команду '/info'")

@bot.message_handler(commands=['info'])

def info_message(message):
    bot.send_message(message.chat.id,"Этот бот создан для автоматизированного взаимодействия с лайв-инфраструктурой и его отдельных элементов. В скором времени тут появится возможность вывода мультивьювера, по нажатию одной кнопки формирования и отправки json в чат WSC, а также коммутирования и заведения записей.")
    bot.send_message(message.chat.id,"Список команд: '/start', '/info', '/menu'")

@bot.message_handler(commands=['menu'])

def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def menu_message(message):
    button_list = [
     types.InlineKeyboardButton(text="Запомнить логин", callback_data="1"),
     types.InlineKeyboardButton(text="Запомнить пароль", callback_data="2"),
     types.InlineKeyboardButton(text="Сформировать json", callback_data="3"),
     types.InlineKeyboardButton(text="#Мультивьювер", callback_data="4"),
     types.InlineKeyboardButton(text="#Скоммутировать", callback_data="5"),
     types.InlineKeyboardButton(text="#Завести запись", callback_data="6")
]
    n_cols = "2"
    reply_markup = types.InlineKeyboardMarkup(build_menu(button_list, n_cols))
    bot.send_message(message.chat.id, text="Menu", reply_markup=reply_markup)

@bot.message_handler(content_types=['text'])

def menu_reply(message):
    if message.text=="Запомнить логин":
        bot.send_message(message.chat.id,"Введите логин:")
    elif message.text=="Запомнить пароль":
          bot.send_message(message.chat.id,"Введите пароль:")

    elif message.text=="Сформировать json":
          markup3=types.ReplyKeyboardMarkup(resize_keyboard=True)
          item3_1=types.KeyboardButton("Все заведенные матчи в LCM prod")
          markup3.add(item3_1)
          item3_2=types.KeyboardButton("Все заведенные матчи в LCM pre-prod")
          markup3.add(item3_2)
          item3_3=types.KeyboardButton("Один матч из LCM prod")
          markup3.add(item3_3)
          item3_4=types.KeyboardButton("Один матч из LCM pre-prod")
          markup3.add(item3_4)
          item3_back=types.KeyboardButton("Назад")
          markup3.add(item3_back)
          bot.send_message(message.chat.id,"Какие матчи добавить в файл?",reply_markup=markup3)

@bot.message_handler(content_types=['text'])

def back_to_menu(message):
    if "Назад" in message.text:
         bot.send_message(message.chat.id,"Главное меню", reply_markup=markupMane)


bot.infinity_polling()

