import requests
import telebot
from bs4 import BeautifulSoup as bs

headers = {'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
token = "1098441995:AAGqy3iBI9ODvcIaGW3isg3BrSJe60wBU1I"
TELEGRAM_CHAT_ID = '704777145'
bot = telebot.TeleBot(token)
base_url ='https://worldbox.pl/products/cupon-ostatnie-sztuki/flag,8/item,24'


def worldbox_parse(base_url,headers):

    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'block__flags product col-sm-6 col-md-4 col-xs-6'})

        for div in divs:
            list = div.find_all('img')
            price = div.find('span', attrs={'class': 'price-tag'}).text
            title = div.find('p').text
            for first_pic in list:
                img = first_pic.get('data-echo')

            text = ('Worldbox' + '\n' + 'Sale🔥🔥🔥')
            AllAnswer = text + '\n' + title + '\n' + img + '\n' + price;

            bot.send_message(704777145, AllAnswer)
            # print("Отправил")


        print('Готово')
        # print(len(divs))
        # print(title)
    else:
        print('ERROR')

