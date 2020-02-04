import telebot
import  requests
from bs4 import BeautifulSoup as bs
import  urllib.request as urllib2
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from logging import Handler, Formatter
import logging
import datetime
import scrapy
import lxml.html
from datetime import date


headers = {'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
token = "1098441995:AAGqy3iBI9ODvcIaGW3isg3BrSJe60wBU1I"
TELEGRAM_CHAT_ID = '704777145'
bot = telebot.TeleBot(token)
base_url ='https://sneakerstudio.pl/pol_m_SALE-665.html'




def sneakerstudio_pars(base_url,headers):

    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'product_wrapper col-md-4 col-xs-6'})

        for div in divs:
            list = div.find_all('img')
            price = div.find('span', attrs={'class': 'price'}).text
            title = div.find('a', attrs={'class': 'product-name'}).text
            #print(title)
            #print(price)
            for first_pic in list:
                img = first_pic.get('data-lazy')

            pict =('https://sneakerstudio.pl' + img)

            text = ('SneakerStudio' + '\n' + 'Sale🔥🔥🔥')
            AllAnswer = text + '\n' + title + '\n' + price + '\n' + pict;
            #bot.send_photo(704777145, pict)
            bot.send_message(704777145, AllAnswer)
           #print("Отправил")

           # print(list)
        print('Готово')
        #print(len(divs))
       # print(title)
    else:
        print('ERROR')
