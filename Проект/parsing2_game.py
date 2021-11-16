from bs4 import BeautifulSoup as BS
import requests
import sqlite3

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

URL2 = "https://vgtimes.ru/tags/халява/"


connect = sqlite3.connect('server.db')
cursor = connect.cursor()

cursor.execute("DROP TABLE news_xgame") # Удаление БД
connect.commit()



connect = sqlite3.connect('server.db')
gcursor = connect.cursor()




def khalyava():

	gcursor.execute("""CREATE TABLE IF NOT EXISTS news_xgame(
		Дата TEXT PRIMARY KEY,
		Текст TEXT,
		Сылка TEXT
	)
	""") 
	connect.commit()

	session = requests.Session()
	response = session.get(URL2, headers=HEADERS)
	soup = BS(response.content, 'html.parser')

	khitem = soup.find_all('div', class_='item-main')

	khnews = []
	for item in khitem:
		khdata = item.find('span', class_='news_item_time').text
		khtext = item.find('div', class_='v12').text
		khlink = item.find('a').get('href')

		khnews.append({khdata : [khtext, khlink]})
		
		khnews_lst = [khdata, khtext, khlink]             #    список из данных которые перемещаются в БД
		gcursor.execute("INSERT INTO news_xgame VALUES(?, ?, ?);", khnews_lst)
		connect.commit()

		if len(khnews)==11:
			break
khalyava()