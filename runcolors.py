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

main_chat =789430384
test_chat = 704777145
headers = {'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
token = "1098441995:AAGqy3iBI9ODvcIaGW3isg3BrSJe60wBU1I"
TELEGRAM_CHAT_ID = '789430384'
bot = telebot.TeleBot(token)
New_url='https://runcolors.pl/product_advanced_searcher/from_category/121.html?order=created_desc&s%5B17%5D=&s%5B19%5D%5B%5D=67&s%5B19%5D%5B%5D=68&s%5B19%5D%5B%5D=71&s%5B19%5D%5B%5D=75&s%5B19%5D%5B%5D=78&s%5B19%5D%5B%5D=82&s%5B19%5D%5B%5D=83&s%5B19%5D%5B%5D=86&s%5B19%5D%5B%5D=88&s%5B19%5D%5B%5D=89&s%5B19%5D%5B%5D=93&s%5B19%5D%5B%5D=94&s%5B19%5D%5B%5D=100&s%5B19%5D%5B%5D=117&s%5B19%5D%5B%5D=119&s%5B19%5D%5B%5D=121&s%5B19%5D%5B%5D=124&s%5B19%5D%5B%5D=125&s%5B19%5D%5B%5D=126&s%5B28%5D%5Bfrom%5D=&s%5B28%5D%5Bto%5D=&direction=asc&order=created_desc&per_page=120&view_option=box'


def runcolors_parsnew(New_url,headers):
    global hreff
    session = requests.Session()
    request = session.get(New_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('li', attrs={'class': 'pList__item'})

        for div in divs:
            list = div.find_all('img')
            tovar = div.find_all('a')
            for hhh in tovar:
                href = hhh.get('href')
            price = div.find('p', attrs={'class': 'pList__price'}).text
            title = div.find('span', attrs = {'class': 'pList__title'}).text
            for first_pic in list:
                img = first_pic.get('src')
            hreff = ('https://runcolors.pl' + href)
            request1 = session.get(hreff, headers=headers)
            if request1.status_code == 200:
                soup1 = bs(request1.content, 'html.parser')
                ul = soup1.find_all('div', attrs={'class': 'product__data__options'})
                print(ul)
                for sizes in ul:
                    size = sizes.get()
                    print(size)
            #print(hreff)
           # print(title)
            #print(img)
            #print(price)
            all = title + '\n' + price + '\n' + img
            #bot.send_message(test_chat, all)
            print('qwe')








