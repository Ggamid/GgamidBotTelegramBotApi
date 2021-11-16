from bs4 import BeautifulSoup as BS
import requests
import sqlite3
# Начало ПАРСА С САЙТА НОВСОТЕЙ ДАГЕСТАНА
URL = "https://mkala.mk.ru/news/"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', 'accept': '*/*'}
	
connect = sqlite3.connect('server.db')
cursor = connect.cursor()

# cursor.execute("DROP TABLE news") # Удаление БД
# connect.commit()


connect = sqlite3.connect('server.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS news(
	Дата TEXT,
	Текст TEXT,
	Сылка TEXT
)
""") 
connect.commit()



session = requests.Session()
response = session.get(URL, headers=HEADERS)
soup = BS(response.content, 'html.parser')
items = soup.find_all('section', class_='news-listing__day-group')
items2 = soup.find_all('a', class_='news-listing__item-link')

# print(items)
	
news = {}
time_news = {}

def delete_db():
	cursor.execute("DROP TABLE news") # Удаление БД
	connect.commit()


for item in items2 and items:

	data = item.find('h2', class_='news-listing__day-date').text
	time = item.find('span', class_='news-listing__item-time').text
	text = item.find('h3', class_='news-listing__item-title').text
	link = item.find('a', class_='news-listing__item-link').get('href')

	news.update({data + ' ' + time : [text, link]})

	news_lst = [data + "г " + time, text, link]             #    список из данных которые перемещаются в БД
	cursor.execute("INSERT INTO news VALUES(?, ?, ?);", news_lst)
	connect.commit()

	if len(news)==11:
		break


# Конец ПАРСА С САЙТА НОВСОТЕЙ ДАГЕСТАНА


