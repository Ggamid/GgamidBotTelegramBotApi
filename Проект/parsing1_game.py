from bs4 import BeautifulSoup as BS
import requests
import sqlite3



# НОВСТИ 
URL = "https://vgtimes.ru/news/"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}


connect = sqlite3.connect('server.db')
cursor = connect.cursor()

cursor.execute("DROP TABLE news_game") # Удаление БД
connect.commit()



connect = sqlite3.connect('server.db')
gcursor = connect.cursor()
gcursor.execute("""CREATE TABLE IF NOT EXISTS news_game(
	Дата TEXT PRIMARY KEY,
	Текст TEXT,
	Сылка TEXT
)
""") 
connect.commit()

session = requests.Session()
response = session.get(URL, headers=HEADERS)
soup = BS(response.content, 'html.parser')

gitems = soup.find_all('div', class_='item-main')
	# print(gitems)



gnews = []
for item in gitems:
	gdata = item.find('span', class_='news_item_time').text
	gtext = item.find('div', class_='v12').text
	glink = item.find('a').get('href')

	gnews.append({gdata : [gtext, glink]})
		
	gnews_lst = [gdata, gtext, glink]             #    список из данных которые перемещаются в БД
	gcursor.execute("INSERT INTO news_game VALUES(?, ?, ?);", gnews_lst)
	connect.commit()

	if len(gnews)==11:
		break

# НОВОСТИ




