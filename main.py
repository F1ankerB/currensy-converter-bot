import telebot
import requests
access_key = '1180f53b6880fc26d766225b0a3945f0'
TOKEN = "6372111966:AAEzjWHzs5AhesxDXmGofPSzuBCCt7xVmG4"
keys={
    'доллар':'USD',
    'евро':'EUR',
    'злотый':'PLN',
    'гривна':'UAH',
    'фунт стерлингов':'GBP',
    'иена':'JPY',
    'юань':'CNY',
    'рубль':'RUB',
    'шекель':'ILS'
}
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start','help'])
def instruction(message):
    text="Здравствуйте! " \
         "Это бот для быстрой конвертации одной валюты в другую. " \
         "Вы можете получить список всех доступных валют по команде /values. " \
         "Для получения корректного ответа вводите свой запрос в формате: " \
         "<имя валюты, цену которой вы хотите узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>"
    bot.reply_to(message,text)
@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text='Доступные валюты:'
    for key in keys.keys():
        text='\n'.join((text,key,))
    bot.reply_to(message,text)
@bot.message_handler(content_types=['text'],)
def convert(message: telebot.types.Message):
    base, quote, amount=message.text.split(' ')
    dbase=keys[base]
    dquote=keys[quote]
    iamount=int(amount)
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
    bot.reply_to(message,f'Курс валюты {base} к валюте {quote} в количестве {amount}: {first/second*iamount}')

bot.polling()
