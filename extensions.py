import json
import requests
import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
class ConvertionException(Exception):
    pass
class Converter:
    def __init__(self,base,quote,amount):
        self.base=base
        self.quote=quote
        self.amount=amount
        self.keys={
            'доллар': 'USD',
            'евро': 'EUR',
            'злотый': 'PLN',
            'гривна': 'UAH',
            'фунт стерлингов': 'GBP',
            'иена': 'JPY',
            'юань': 'CNY',
            'рубль': 'RUB',
            'шекель': 'ILS'
        }

    def get_price(self,message):

        if self.base==self.quote:
            raise ConvertionException('Нельзя конвертировать две одинаковые валюты')
        try:
            iamount = int(self.amount)
        except ValueError:
            return ('Некорректное количество валюты')
        try:
            dbase=self.keys[self.base]
            dquote=self.keys[self.quote]
        except KeyError:
            return ('Некорректная валюта')
        url = f"http://api.exchangeratesapi.io/v1/latest?access_key=3b0ff49e10d1e922d02ab376c50fa67d&symbols={dbase}"
        response = requests.get(url)
        data = response.json()
        response = data['rates']
        first = response[dbase]
        url = f"http://api.exchangeratesapi.io/v1/latest?access_key=3b0ff49e10d1e922d02ab376c50fa67d&symbols={dquote}"
        response = requests.get(url)
        data = response.json()
        response = data['rates']
        second = response[dquote]
        return f'Курс валюты {self.base} к валюте {self.quote} в количестве {self.amount}: {first / second * iamount}'

