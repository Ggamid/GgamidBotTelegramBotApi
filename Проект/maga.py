from bs4 import BeautifulSoup as BS
import requests
import sqlite3



# НОВСТИ 
URL = "https://csgo.ru/allnews"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.41 YaBrowser/21.5.0.582 Yowser/2.5 Safari/537.36', 'accept': '*/*'}


connect = sqlite3.connect('server.db')
cursor = connect.cursor()

# cursor.execute("DROP TABLE maga") # Удаление БД
# connect.commit()



connect = sqlite3.connect('server.db')
gcursor = connect.cursor()
gcursor.execute("""CREATE TABLE IF NOT EXISTS maga(
	Дата TEXT PRIMARY KEY,
	Текст TEXT,
	Сылка TEXT
)
""") 
connect.commit()

session = requests.Session()
response = session.get(URL, headers=HEADERS)
soup = BS(response.content, 'html.parser')

gitems = soup.find_all('div', class_='list-sorted-news__item')
print(gitems)



# gnews = []
# for item in gitems:
# 	gdata = item.find('div', class_='news-item__statistics').text
# 	gtext = item.find('a', class_='news-item__title').text
# 	glink = item.find('a').get('href')

# 	gnews.append({gdata : [gtext, glink]})
		
# 	gnews_lst = [gdata, gtext, glink]             #    список из данных которые перемещаются в БД
# 	gcursor.execute("INSERT INTO maga VALUES(?, ?, ?);", gnews_lst)
# 	connect.commit()

# 	if len(gnews)==11:
# 		break