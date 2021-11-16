from bs4 import BeautifulSoup as BS
import requests
import sqlite3
# 	MMA
URL = "https://matchtv.ru/news/boxing"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', 'accept': '*/*'}
	

connect = sqlite3.connect('server.db')
cursor = connect.cursor()

cursor.execute("DROP TABLE news_mma") # Удаление БД
connect.commit()

connect = sqlite3.connect('server.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS news_mma(
	Дата TEXT,
	Текст TEXT,
	Сылка TEXT
)
""") 
connect.commit()



session = requests.Session()
response = session.get(URL, headers=HEADERS)
soup = BS(response.content, 'html.parser')

items = soup.find_all('a', class_='node-news-list__item')
link2 = soup.find('div',class_='node-news-list').find_all('a', class_='node-news-list__item')
# print(link2)
# print(items)

	
news = {}
time_news = {}

def delete_db():
	cursor.execute("DROP TABLE news") # Удаление БД
	connect.commit()


for item in items and link2:

	link = item.get('href')

	data_time = item.find('li', class_='list__item credits__item').text
	# print(data_time)

	text = item.find('div', class_='node-news-list__title').text.strip()

	news.update({data_time : [text, link]})

	news_lst = [data_time, text, link]             #    список из данных которые перемещаются в БД
	cursor.execute("INSERT INTO news_mma VALUES(?, ?, ?);", news_lst)
	connect.commit()

	if len(news)==10:
		break