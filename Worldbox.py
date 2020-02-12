import requests
import telebot
from bs4 import BeautifulSoup as bs
main_chat =789430384
test_chat = 414407353
headers = {'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
token = "1098441995:AAGqy3iBI9ODvcIaGW3isg3BrSJe60wBU1I"
TELEGRAM_CHAT_ID = '789430384'
bot = telebot.TeleBot(token)
Sale_url ='https://worldbox.pl/products/obuwie-ostatnie-sztuki/category,2/flag,8/item,24?'
New_url = 'https://worldbox.pl/products/obuwie-nowosc/category,2/flag,1/item,24/sort,1?'


def worldbox_parsesale(Sale_url,headers):

    session = requests.Session()
    request = session.get(Sale_url, headers=headers)
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
            AllAnswer = text + '\n' + title + '\n' + img + '\n' + price

            bot.send_message(test_chat, AllAnswer)
            # print("Отправил")


        print('Готово')
        # print(len(divs))
        # print(title)
    else:
        print('ERROR')

def worldvox_parsnew(New_url,headers):
    session = requests.Session()
    request = session.get(New_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'block__flags product col-sm-6 col-md-4 col-xs-6'})

        for div in divs:
            tovar = div.find_all('a')
            for hhh in tovar:
                href = hhh.get('href')
            list = div.find_all('img')
            price = div.find('span', attrs={'class': 'price-tag'}).text
            title = div.find('p').text
            for first_pic in list:
                img = first_pic.get('data-echo')
            bot.send_message(704777145, href)
            request1 = session.get(href, headers=headers)
            if request1.status_code == 200:
                soup1 = bs(request1.content, 'html.parser')
                ul = soup1.find_all('span', attrs={'class': 'size_box'})
                for sizespan in ul:
                    size = sizespan.find('')
                    print(size)
                print(ul)
           # text = ('Worldbox' + '\n' + 'New🔥🔥🔥')
           #AllAnswer = text + '\n' + title + '\n' + img + '\n' + price;

            #bot.send_message(704777145, AllAnswer)
            # print("Отправил")


        print('Готово')
        # print(len(divs))
        # print(title)
    else:
        print('ERROR')