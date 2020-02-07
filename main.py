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
import runcolors
from datetime import date

main_chat =789430384
test_chat = 704777145


headers = {'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
token = "1098441995:AAGqy3iBI9ODvcIaGW3isg3BrSJe60wBU1I"
bot = telebot.TeleBot(token)



#Sneakerstudio.sneakerstudio_parssale(Sneakerstudio.Sale_url, headers)
#Sneakerstudio.sneakerstudio_parsnew(Sneakerstudio.New_url,headers)

#Worldbox.worldbox_parsesale(Worldbox.Sale_url, headers)
#Worldbox.worldvox_parsnew(Worldbox.New_url, headers)

runcolors.runcolors_parsnew(runcolors.New_url, headers)


bot.polling(none_stop=True, interval=0)

