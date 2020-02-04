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
import Sneakerstudio
import Worldbox
from datetime import date


headers = {'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
token = "1098441995:AAGqy3iBI9ODvcIaGW3isg3BrSJe60wBU1I"
TELEGRAM_CHAT_ID = '704777145'
bot = telebot.TeleBot(token)
Sneakerstudio_url ='https://sneakerstudio.pl/pol_m_SALE-665.html'
Worldbox_url= 'https://worldbox.pl/products/cupon-ostatnie-sztuki/flag,8/item,24'



token = "1098441995:AAGqy3iBI9ODvcIaGW3isg3BrSJe60wBU1I"
TELEGRAM_CHAT_ID = '704777145'
bot = telebot.TeleBot(token)



Sneakerstudio.sneakerstudio_pars(Sneakerstudio_url, headers)


#Worldbox.worldbox_parse(Worldbox_url, headers)



bot.polling(none_stop=True, interval=0)

