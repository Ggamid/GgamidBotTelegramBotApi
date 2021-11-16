from bs4 import BeautifulSoup as BS
import requests
import sqlite3
# 	MMA
URL = "https://pikabu.ru/story/100_interesnyikh_faktov_obo_vsem_na_svete_4109303"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36', 'accept': '*/*'}
	



connect = sqlite3.connect('server.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS fact(
	Текст TEXT
)
""") 
connect.commit()



session = requests.Session()
response = session.get(URL, headers=HEADERS)
soup = BS(response.content, 'html.parser')

link2 = soup.find('div', class_='story-block story-block_type_text').find_all('p')

# aaa = link2.strip(" ")

# print(link2)

	
news = []



for item in link2:

	text = item.text.strip('№ 1 2 3 4 5 6 7 8 9')
	# print(text)

	news.append(text)

	news_lst = [text]             #    список из данных которые перемещаются в БД
	cursor.execute("INSERT INTO fact VALUES(?);", news_lst)
	connect.commit()

	if len(news)==3000:
		break