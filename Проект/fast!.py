from bs4 import BeautifulSoup as BS
import requests
import sqlite3
# Начало ПАРСА С САЙТА НОВСОТЕЙ ДАГЕСТАНА
URL = "https://mkala.mk.ru/news/"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', 'accept': '*/*'}
	
connect = sqlite3.connect('server.db')
cursor = connect.cursor()

cursor.execute("DROP TABLE news2") # Удаление БД
connect.commit()


connect = sqlite3.connect('server.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS news2(
	Дата TEXT,
	Текст TEXT,
	Сылка TEXT
)
""") 
connect.commit()



session = requests.Session()
response = session.get(URL, headers=HEADERS)
soup = BS(response.content, 'html.parser')
# itemsss = soup.find_all('ul', class_='news-listing__day-list')
# items2 = soup.find_all('section', class_='news-listing__day-group')

# print(items)
# print(itemsss)

# for item in itemsss:
items = soup.find_all('li', class_='news-listing__item')

items45 = soup.find_all('section', class_='news-listing__day-group')

print(items)




# for item in items45:
# 	data = item.find('h2', class_='news-listing__day-date').text



news = {}
time_news = {}

def delete_db():
	cursor.execute("DROP TABLE news") # Удаление БД
	connect.commit()


for item in items and items45:

	data = item.find('h2', class_='news-listing__day-date').text
	time = item.find('span', class_='news-listing__item-time').text
	text = item.find('h3', class_='news-listing__item-title').text
	link = item.find('a', class_='news-listing__item-link').get('href')

	news.update({data + ' ' + time : [text, link]})

	news_lst = [data + "г " + time, text, link]             #    список из данных которые перемещаются в БД
	cursor.execute("INSERT INTO news2 VALUES(?, ?, ?);", news_lst)
	connect.commit()

	if len(news)==11:
		break