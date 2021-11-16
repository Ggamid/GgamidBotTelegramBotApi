import telebot
import config
import random
from telebot import types
import sqlite3
import time
from bs4 import BeautifulSoup as BS
import requests


connect = sqlite3.connect('server.db', check_same_thread=False)
cursor = connect.cursor()

# NEWS DAG

cursor.execute("SELECT * FROM news;")
three_results = cursor.fetchall()


cc1 = []
for item in three_results:
    cc1.append(item)
a = []
for item in cc1:
    a.append(item)

for item in a:
    news_1 = cc1[0]
    news_2 = cc1[1]
    news_3 = cc1[2]
    news_4 = cc1[3]
    news_5 = cc1[4]
    news_6 = cc1[5]
    news_7 = cc1[6]
    news_8 = cc1[7]
    news_9 = cc1[8]
    news_10 = cc1[9]

data_news1 = "Эта⬇️ Новость опубликована: " + news_1[0]
text_news1 = news_1[1]
data_text_mews1 = data_news1 + "\n" + text_news1
link_news1 = news_1[2]

data_news2 = "Эта⬇️ Новость опубликована: " + news_2[0]
text_news2 = news_2[1]
data_text_mews2 = data_news2 + "\n" + text_news2
link_news2 = news_2[2]

data_news3 = "Эта⬇️ Новость опубликована: " + news_3[0]
text_news3 = news_3[1]
data_text_mews3 = data_news3 + "\n" + text_news3
link_news3 = news_3[2]
# NEWS DAG

# news game
cursor.execute("SELECT * FROM news_game;")
GGame = cursor.fetchall()



for item in GGame:
    gnews_1 = GGame[0]
    gnews_2 = GGame[1]
    gnews_3 = GGame[2]
    gnews_4 = GGame[3]
    gnews_5 = GGame[4]
    gnews_6 = GGame[5]
    gnews_7 = GGame[6]
    gnews_8 = GGame[7]
    gnews_9 = GGame[8]
    gnews_10 = GGame[9]
    gnews_11 = GGame[10]

    gdata_news1 = "Эта⬇️ Новость опубликована: " + gnews_1[0]
    gtext_news1 = gnews_1[1]
    glink_news1 = gnews_1[2]
    GN_all1 = gdata_news1 + '\n' + '\n' + gtext_news1 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news1

    gdata_news2 = "Эта⬇️ Новость опубликована: " + gnews_2[0]
    gtext_news2 = gnews_2[1]
    glink_news2 = gnews_2[2]
    GN_all2 = gdata_news2 + '\n' + '\n' + gtext_news2 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news2

    gdata_news3 = "Эта⬇️ Новость опубликована: " + gnews_3[0]
    gtext_news3 = gnews_3[1]
    glink_news3 = gnews_3[2]
    GN_all3 = gdata_news3 + '\n' + '\n' + gtext_news3 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news3

    gdata_news4 = "Эта⬇️ Новость опубликована: " + gnews_4[0]
    gtext_news4 = gnews_4[1]
    glink_news4 = gnews_4[2]
    GN_all4 = gdata_news4 + '\n' + '\n' + gtext_news4 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news4
    
    gdata_news5 = "Эта⬇️ Новость опубликована: " + gnews_5[0]
    gtext_news5 = gnews_5[1]
    glink_news5 = gnews_5[2]
    GN_all5 = gdata_news5 + '\n' + '\n' + gtext_news5 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news5

    
    gdata_news6 = "Эта⬇️ Новость опубликована: " + gnews_6[0]
    gtext_news6 = gnews_6[1]
    glink_news6 = gnews_6[2]
    GN_all6 = gdata_news6 + '\n' + '\n' + gtext_news6 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news6 

    gdata_news7 = "Эта⬇️ Новость опубликована: " + gnews_7[0]
    gtext_news7 = gnews_7[1]
    glink_news7 = gnews_7[2] 
    GN_all7 = gdata_news7 + '\n' + '\n' + gtext_news7 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news7

    gdata_news8 = "Эта⬇️ Новость опубликована: " + gnews_8[0]
    gtext_news8 = gnews_8[1]
    glink_news8 = gnews_8[2] 
    GN_all8 = gdata_news8 + '\n' + '\n' + gtext_news8 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news8

    gdata_news9 = "Эта⬇️ Новость оп9убликована: " + gnews_9[0]
    gtext_news9 = gnews_9[1]
    glink_news9 = gnews_9[2] 
    GN_all9 = gdata_news9 + '\n' + '\n' + gtext_news9 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news9

    gdata_news10 = "Эта⬇️ Новость опубликована: " + gnews_10[0]
    gtext_news10 = gnews_10[1]
    glink_news10 = gnews_10[2]    
    GN_all10 = gdata_news10 + '\n' + '\n' + gtext_news10 +  '\n' +'\n' + 'ссылка:' + '\n' + glink_news10
    
# news GAME
# KHALYAVA
cursor.execute("SELECT * FROM news_xgame;")
HGGame = cursor.fetchall()

for item in HGGame:
    Hnews_1 = HGGame[0]
    Hnews_2 = HGGame[1]
    Hnews_3 = HGGame[2]
    Hnews_4 = HGGame[3]
    Hnews_5 = HGGame[4]
    Hnews_6 = HGGame[5]
    Hnews_7 = HGGame[6]
    Hnews_8 = HGGame[7]
    Hnews_9 = HGGame[8]
    Hnews_10 = HGGame[9]
    Hnews_11 = HGGame[10]

    Hdata_news1 = "Эта⬇️ Новость опубликована: " + Hnews_1[0]
    Htext_news1 = Hnews_1[1]
    Hlink_news1 = Hnews_1[2]
    HGN_all1 = Hdata_news1 + '\n' + '\n' + Htext_news1 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news1

    Hdata_news2 = "Эта⬇️ Новость опубликована: " + Hnews_2[0]
    Htext_news2 = Hnews_2[1]
    Hlink_news2 = Hnews_2[2]
    HGN_all2 = Hdata_news2 + '\n' + '\n' + Htext_news2 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news2

    Hdata_news3 = "Эта⬇️ Новость опубликована: " + Hnews_3[0]
    Htext_news3 = Hnews_3[1]
    Hlink_news3 = Hnews_3[2]
    HGN_all3 = Hdata_news3 + '\n' + '\n' + Htext_news3 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news3

    Hdata_news4 = "Эта⬇️ Новость опубликована: " + Hnews_4[0]
    Htext_news4 = Hnews_4[1]
    Hlink_news4 = Hnews_4[2]
    HGN_all4 = Hdata_news4 + '\n' + '\n' + Htext_news4 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news4
    
    Hdata_news5 = "Эта⬇️ Новость опубликована: " + Hnews_5[0]
    Htext_news5 = Hnews_5[1]
    Hlink_news5 = Hnews_5[2]
    HGN_all5 = Hdata_news5 + '\n' + '\n' + Htext_news5 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news5

    
    Hdata_news6 = "Эта⬇️ Новость опубликована: " + Hnews_6[0]
    Htext_news6 = Hnews_6[1]
    Hlink_news6 = Hnews_6[2]
    HGN_all6 = Hdata_news6 + '\n' + '\n' + Htext_news6 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news6 

    Hdata_news7 = "Эта⬇️ Новость опубликована: " + Hnews_7[0]
    Htext_news7 = Hnews_7[1]
    Hlink_news7 = Hnews_7[2] 
    HGN_all7 = Hdata_news7 + '\n' + '\n' + Htext_news7 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news7

    Hdata_news8 = "Эта⬇️ Новость опубликована: " + Hnews_8[0]
    Htext_news8 = Hnews_8[1]
    Hlink_news8 = Hnews_8[2] 
    HGN_all8 = Hdata_news8 + '\n' + '\n' + Htext_news8 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news8

    Hdata_news9 = "Эта⬇️ Новость оп9убликована: " + Hnews_9[0]
    Htext_news9 = Hnews_9[1]
    Hlink_news9 = Hnews_9[2] 
    HGN_all9 = Hdata_news9 + '\n' + '\n' + Htext_news9 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news9

    Hdata_news10 = "Эта⬇️ Новость опубликована: " + Hnews_10[0]
    Htext_news10 = Hnews_10[1]
    Hlink_news10 = Hnews_10[2]    
    HGN_all10 = Hdata_news10 + '\n' + '\n' + Htext_news10 +  '\n' +'\n' + 'ссылка:' + '\n' + Hlink_news10
# Khalyava

# FOOTBALL
cursor.execute("SELECT * FROM news_ball;")
Ballgame = cursor.fetchall()


for item in Ballgame:
    Bnews_1 = Ballgame[0]
    Bnews_2 = Ballgame[1]
    Bnews_3 = Ballgame[2]
    Bnews_4 = Ballgame[3]
    Bnews_5 = Ballgame[4]
    Bnews_6 = Ballgame[5]
    Bnews_7 = Ballgame[6]
    Bnews_8 = Ballgame[7]
    Bnews_9 = Ballgame[8]
    Bnews_10 = Ballgame[9]

    Bdata_news1 = "Эта⬇️ Новость опубликована: " + Bnews_1[0]
    Btext_news1 = Bnews_1[1]
    Blink_news1 = Bnews_1[2]
    BGN_all1 = Bdata_news1 + '\n' + '\n' + Btext_news1 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Blink_news1

    Bdata_news2 = "Эта⬇️ Новость опубликована: " + Bnews_2[0]
    Btext_news2 = Bnews_2[1]
    Blink_news2 = Bnews_2[2]
    BGN_all2 = Bdata_news2 + '\n' + '\n' + Btext_news2 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Blink_news2

    Bdata_news3 = "Эта⬇️ Новость опубликована: " + Bnews_3[0]
    Btext_news3 = Bnews_3[1]
    Blink_news3 = Bnews_3[2]
    BGN_all3 = Bdata_news3 + '\n' + '\n' + Btext_news3 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Blink_news3

    Bdata_news4 = "Эта⬇️ Новость опубликована: " + Bnews_4[0]
    Btext_news4 = Bnews_4[1]
    Blink_news4 = Bnews_4[2]
    BGN_all4 = Bdata_news4 + '\n' + '\n' + Btext_news4 +  '\n' +'\n' + 'ссылка:' + '\n' +'https://matchtv.ru' +  Blink_news4
    
    Bdata_news5 = "Эта⬇️ Новость опубликована: " + Bnews_5[0]
    Btext_news5 = Bnews_5[1]
    Blink_news5 = Bnews_5[2]
    BGN_all5 = Bdata_news5 + '\n' + '\n' + Btext_news5 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Blink_news5

    
    Bdata_news6 = "Эта⬇️ Новость опубликована: " + Bnews_6[0]
    Btext_news6 = Bnews_6[1]
    Blink_news6 = Bnews_6[2]
    BGN_all6 = Bdata_news6 + '\n' + '\n' + Btext_news6 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Blink_news6 

    Bdata_news7 = "Эта⬇️ Новость опубликована: " + Bnews_7[0]
    Btext_news7 = Bnews_7[1]
    Blink_news7 = Bnews_7[2] 
    BGN_all7 = Bdata_news7 + '\n' + '\n' + Btext_news7 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Blink_news7

    Bdata_news8 = "Эта⬇️ Новость опубликована: " + Bnews_8[0]
    Btext_news8 = Bnews_8[1]
    Blink_news8 = Bnews_8[2] 
    BGN_all8 = Bdata_news8 + '\n' + '\n' + Btext_news8 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Blink_news8

    Bdata_news9 = "Эта⬇️ Новость оп9убликована: " + Bnews_9[0]
    Btext_news9 = Bnews_9[1]
    Blink_news9 = Bnews_9[2] 
    BGN_all9 = Bdata_news9 + '\n' + '\n' + Btext_news9 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Blink_news9
# FOOTBALL

# MMA
cursor.execute("SELECT * FROM news_mma;")
MMA = cursor.fetchall()


for item in MMA:
    mmanews_1 = MMA[0]
    mmanews_2 = MMA[1]
    mmanews_3 = MMA[2]
    mmanews_4 = MMA[3]
    mmanews_5 = MMA[4]
    mmanews_6 = MMA[5]
    mmanews_7 = MMA[6]
    mmanews_8 = MMA[7]
    mmanews_9 = MMA[8]
    mmanews_10 = MMA[9]

    Mdata_news1 = "Эта⬇️ Новость опубликована: " + mmanews_1[0]
    Mtext_news1 = mmanews_1[1]
    Mlink_news1 = mmanews_1[2]
    MGN_all1 = Mdata_news1 + '\n' + '\n' + Mtext_news1 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news1

    Mdata_news2 = "Эта⬇️ Новость опубликована: " + mmanews_2[0]
    Mtext_news2 = mmanews_2[1]
    Mlink_news2 = mmanews_2[2]
    MGN_all2 = Mdata_news2 + '\n' + '\n' + Mtext_news2 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news2

    Mdata_news3 = "Эта⬇️ Новость опубликована: " + mmanews_3[0]
    Mtext_news3 = mmanews_3[1]
    Mlink_news3 = mmanews_3[2]
    MGN_all3 = Mdata_news3 + '\n' + '\n' + Mtext_news3 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news3

    Mdata_news4 = "Эта⬇️ Новость опубликована: " + mmanews_4[0]
    Mtext_news4 = mmanews_4[1]
    Mlink_news4 = mmanews_4[2]
    MGN_all4 = Mdata_news4 + '\n' + '\n' + Mtext_news4 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news4
    
    Mdata_news5 = "Эта⬇️ Новость опубликована: " + mmanews_5[0]
    Mtext_news5 = mmanews_5[1]
    Mlink_news5 = mmanews_5[2]
    MGN_all5 = Mdata_news5 + '\n' + '\n' + Mtext_news5 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news5

    
    Mdata_news6 = "Эта⬇️ Новость опубликована: " + mmanews_6[0]
    Mtext_news6 = mmanews_6[1]
    Mlink_news6 = mmanews_6[2]
    MGN_all6 = Mdata_news6 + '\n' + '\n' + Mtext_news6 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news6 

    Mdata_news7 = "Эта⬇️ Новость опубликована: " + mmanews_7[0]
    Mtext_news7 = mmanews_7[1]
    Mlink_news7 = mmanews_7[2] 
    MGN_all7 = Mdata_news7 + '\n' + '\n' + Mtext_news7 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news7

    Mdata_news8 = "Эта⬇️ Новость опубликована: " + mmanews_8[0]
    Mtext_news8 = mmanews_8[1]
    Mlink_news8 = mmanews_8[2] 
    MGN_all8 = Mdata_news8 + '\n' + '\n' + Mtext_news8 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news8

    Mdata_news9 = "Эта⬇️ Новость оп9убликована: " + mmanews_9[0]
    Mtext_news9 = mmanews_9[1]
    Mlink_news9 = mmanews_9[2] 
    MGN_all9 = Mdata_news9 + '\n' + '\n' + Mtext_news9 +  '\n' +'\n' + 'ссылка:' + '\n' + 'https://matchtv.ru' + Mlink_news9



# MMA

# FACT

cursor.execute("SELECT * FROM fact;")
Fact = cursor.fetchall()

x = random.randint(0,41)

# fact1 = Fact[x]
# print(fact1)

bot = telebot.TeleBot(config.TOKEN)

# FACT


@bot.message_handler(commands=['start'])
def send_welcome(message):

    connect = sqlite3.connect('server.db', check_same_thread=False)
    cursor = connect.cursor()



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Спорт 🏅')
    item2 = types.KeyboardButton('Игры 🎮')
    item3 = types.KeyboardButton('Новости Дагестана 📰')
    item4 = types.KeyboardButton('Рандомный факт🤔')


    markup.add(item1, item2, item3, item4)
	
    bot.send_message(message.chat.id, f'Салам {message.from_user.first_name}!, Я бот🤖, новостной бот, на данный момент я умею отправлять новости📰, выбери из предложенных тем, интересную тебе❕⬇️'.format(message.from_user, bot.get_me()),
	   parse_mode='html', reply_markup=markup,)






@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомный факт🤔':
            
            cursor.execute("SELECT * FROM fact;")
            Fact = cursor.fetchall()

            x = random.randint(0,139)

            bot.send_message(message.chat.id, "Читаю факты..")
            time.sleep(1.0)
            bot.send_message(message.chat.id, "Выбираю интересный...")
            time.sleep(1.5)
            bot.send_message(message.chat.id, Fact[x])
        elif message.text == 'Новости Дагестана 📰':

                   
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1_2 = types.InlineKeyboardButton("За сегодня", callback_data='good')
            item2_2 = types.InlineKeyboardButton("За 3️⃣ дня", callback_data='bad')
            item3_2 = types.InlineKeyboardButton("Хочу больше новостей!", callback_data='damage')

            markup.add(item1_2, item2_2, item3_2)
            bot.send_message(message.chat.id, 'Новость за какой промежуток времени вы хотите узнать?', reply_markup=markup)

        elif message.text == 'Спорт 🏅':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("MMA/БОКС🥊🤼‍♂️")
            item2 = types.KeyboardButton("Футбол⚽️")
            item3 = types.KeyboardButton("Вернуться назад⏮")


            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Выбери вид спорта?'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

        elif message.text == "Футбол⚽️":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("1", callback_data='1Ball')
            item2 = types.InlineKeyboardButton("3", callback_data='3Ball')
            item3 = types.InlineKeyboardButton("Давай все что есть!", callback_data='allBall')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Выбирай количество новостей?', reply_markup=markup)

        elif message.text == "MMA/БОКС🥊🤼‍♂️":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("1", callback_data='1mma')
            item2 = types.InlineKeyboardButton("3", callback_data='3mma')
            item3 = types.InlineKeyboardButton("Давай все что есть!", callback_data='allmma')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Выбирай количество новостей?', reply_markup=markup)



        elif message.text == 'Игры 🎮':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Халява 🚫💸🚫')
            item2 = types.KeyboardButton('Новости 💬')  
            item3 = types.KeyboardButton("Вернуться назад⏮")

            markup.add(item1, item2, item3)
            
            bot.send_message(message.chat.id, 'Выбирай, хочешь узнать о халяве или Новости'.format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup,)


        elif message.text == "Вернуться назад⏮":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Спорт 🏅')
            item2 = types.KeyboardButton('Игры 🎮')
            item3 = types.KeyboardButton('Новости Дагестана 📰')
            item4 = types.KeyboardButton('Рандомный факт🤔')


            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Ты возвращен в главное меню', reply_markup=markup)

        elif message.text == "Халява 🚫💸🚫":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("1", callback_data='1khalyava')
            item2 = types.InlineKeyboardButton("3", callback_data='3khalyava')
            item3 = types.InlineKeyboardButton("Давай все что есть!", callback_data='allkh')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Выбирай сколько?', reply_markup=markup)

        elif message.text == 'Новости 💬':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item22 = types.InlineKeyboardButton("1 новость", callback_data='onenews')
            item33 = types.InlineKeyboardButton("3 новости", callback_data='3news')
            item44 = types.InlineKeyboardButton("Давай все что есть!", callback_data='allnews')

            markup.add(item22, item33, item44)

            bot.send_message(message.chat.id, 'Выбирай сколько??', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            #news

            if call.data == 'good':
                bot.send_message(call.message.chat.id, data_text_mews1)
                bot.send_message(call.message.chat.id, link_news1)
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, data_text_mews1)
                bot.send_message(call.message.chat.id, link_news1)
                bot.send_message(call.message.chat.id, data_text_mews2)
                bot.send_message(call.message.chat.id, link_news2)
                bot.send_message(call.message.chat.id, data_text_mews3)
                bot.send_message(call.message.chat.id, link_news3)

            elif call.data == 'damage':
                bot.send_message(call.message.chat.id, "Для большего количества новостей, переходите на сайт!😁")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, 'https://mkala.mk.ru/news/')
            
            # news game 
            elif call.data == 'onenews':
                bot.send_message(call.message.chat.id, "Хорошо, сейчас скину😁")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, GN_all1)

            elif call.data == '3news':
                bot.send_message(call.message.chat.id, "Как я  могу вам отказать, сейчас все будет😌")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, GN_all2)

                bot.send_message(call.message.chat.id,GN_all3)

                bot.send_message(call.message.chat.id, GN_all4)
            
            elif call.data == "allnews":
                bot.send_message(call.message.chat.id, GN_all1)
                bot.send_message(call.message.chat.id, GN_all2)
                bot.send_message(call.message.chat.id, GN_all3)
                bot.send_message(call.message.chat.id, GN_all4)
                bot.send_message(call.message.chat.id, GN_all5)
                bot.send_message(call.message.chat.id, GN_all6)
                bot.send_message(call.message.chat.id, GN_all7)
                bot.send_message(call.message.chat.id, GN_all8)
                bot.send_message(call.message.chat.id, GN_all9)
                bot.send_message(call.message.chat.id, GN_all10)
                time.sleep(1.5)
                bot.send_message(call.message.chat.id, "Не хвватает и этого?! Вот тебе ссылка '\n' https://vgtimes.ru/news/")

            # Khalyava
            elif call.data == "1khalyava":
                bot.send_message(call.message.chat.id, "Вот, все как по заказу😉")
                bot.send_message(call.message.chat.id, HGN_all1)

            elif call.data == "3khalyava":
                bot.send_message(call.message.chat.id, "Будет сделано😎")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, HGN_all2)
                bot.send_message(call.message.chat.id, HGN_all3)
                bot.send_message(call.message.chat.id, HGN_all4)
            elif call.data == "allkh":
                bot.send_message(call.message.chat.id, "Ооокей😉")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, HGN_all1)
                bot.send_message(call.message.chat.id, HGN_all2)
                bot.send_message(call.message.chat.id, HGN_all3)
                bot.send_message(call.message.chat.id, HGN_all4)
                bot.send_message(call.message.chat.id, HGN_all5)
                bot.send_message(call.message.chat.id, HGN_all6)
                bot.send_message(call.message.chat.id, HGN_all7)
                bot.send_message(call.message.chat.id, HGN_all8)
                bot.send_message(call.message.chat.id, HGN_all9)
                bot.send_message(call.message.chat.id, HGN_all10)
                bot.send_message(call.message.chat.id, "Хотите еще Халявы? Вот вам ссылка на источник!")
                bot.send_message(call.message.chat.id, "https://vgtimes.ru/tags/халява/")

            # FOOTBALL
            elif call.data == "1Ball":
                bot.send_message(call.message.chat.id, "Вот, все как по заказу😉")
                bot.send_message(call.message.chat.id, BGN_all1)

            elif call.data == "3Ball":
                bot.send_message(call.message.chat.id, "Будет сделано😎")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, BGN_all2)
                bot.send_message(call.message.chat.id, BGN_all3)
                bot.send_message(call.message.chat.id, BGN_all4)
            elif call.data == "allBall":
                bot.send_message(call.message.chat.id, "Ооокей😉")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, BGN_all1)
                bot.send_message(call.message.chat.id, BGN_all2)
                bot.send_message(call.message.chat.id, BGN_all3)
                bot.send_message(call.message.chat.id, BGN_all4)
                bot.send_message(call.message.chat.id, BGN_all5)
                bot.send_message(call.message.chat.id, BGN_all6)
                bot.send_message(call.message.chat.id, BGN_all7)
                bot.send_message(call.message.chat.id, BGN_all8)
                bot.send_message(call.message.chat.id, BGN_all9)
                bot.send_message(call.message.chat.id, "Хотите еще новостей о Футболе? Вот вам ссылка на источник!")
                bot.send_message(call.message.chat.id, "https://matchtv.ru/news/football")
            # FOOTBALL

            # MMA
            elif call.data == "allmma":
                bot.send_message(call.message.chat.id, "Ооокей😉")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, MGN_all1)
                bot.send_message(call.message.chat.id, MGN_all2)
                bot.send_message(call.message.chat.id, MGN_all3)
                bot.send_message(call.message.chat.id, MGN_all4)
                bot.send_message(call.message.chat.id, MGN_all5)
                bot.send_message(call.message.chat.id, MGN_all6)
                bot.send_message(call.message.chat.id, MGN_all7)
                bot.send_message(call.message.chat.id, MGN_all8)
                bot.send_message(call.message.chat.id, MGN_all9)
                bot.send_message(call.message.chat.id, "Хотите еще новостей о Боксе и ММА? Вот вам ссылка на источник!")
                bot.send_message(call.message.chat.id, "https://matchtv.ru/news/boxing")

            elif call.data == "1mma":
                bot.send_message(call.message.chat.id, "Вот, все как по заказу😉")
                bot.send_message(call.message.chat.id, MGN_all1)

            elif call.data == "3mma":
                bot.send_message(call.message.chat.id, "Будет сделано😎")
                time.sleep(1.0)
                bot.send_message(call.message.chat.id, MGN_all2)
                bot.send_message(call.message.chat.id, MGN_all3)
                bot.send_message(call.message.chat.id, MGN_all4)
            # MMA

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбор произведен✅",
                reply_markup=None)
 
            # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
            #     text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))



bot.polling()