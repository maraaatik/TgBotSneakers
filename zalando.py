import telebot
import  requests
from bs4 import BeautifulSoup as bs

main_chat =789430384
test_chat = 414407353
headers = {'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
token = "1098441995:AAGqy3iBI9ODvcIaGW3isg3BrSJe60wBU1I"
TELEGRAM_CHAT_ID = '789430384'
bot = telebot.TeleBot(token)

sneakers_url = 'https://www.zalando.pl/obuwie/'

def zalando_pars(New_url,headers):
    global hreff
    session = requests.Session()
    request = session.get(New_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('z-grid-item', attrs={'class': 'cat_card-1o_9G cat_normalWidth-tz8JR'})
        print(divs)
        for div in divs:
            title = div.find('font', attrs= {'style':'vertical-align: inherit;'})
            print(title)
