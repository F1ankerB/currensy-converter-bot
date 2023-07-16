import telebot
from config import TOKEN
from extensions import Converter, ConvertionException
access_key = '1180f53b6880fc26d766225b0a3945f0'

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
    try:
        values = message.text.split(' ')
        if len(values)!=3:
            raise ConvertionException(f'Некорректное количество параметров')
        base, quote, amount=values
        example=Converter(base,quote,amount)
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        bot.reply_to(message, example.get_price(message))

bot.polling(none_stop=True)
