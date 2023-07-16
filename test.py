import redis

red=redis.Redis(
    host='redis-10746.c293.eu-central-1-1.ec2.cloud.redislabs.com',
    port=10746,
    password='yGcbWPY2qbQjzlO68z6yUCLCxrGDw1Ou'
)
import requests

# Замените 'YOUR_ACCESS_KEY' на ваш API ключ ExchangeratesAPI
access_key = '3b0ff49e10d1e922d02ab376c50fa67d'

# Задайте базовую и целевую валюты
base_currency = 'USD'
target_currency = 'EUR'
base='RUB'
# Формируем URL для запроса
url = f"http://api.exchangeratesapi.io/v1/latest?access_key=3b0ff49e10d1e922d02ab376c50fa67d&symbols={base}"
response = requests.get(url)
data = response.json()
response = data['rates']
q=response['RUB']
url = f"http://api.exchangeratesapi.io/v1/latest?access_key=3b0ff49e10d1e922d02ab376c50fa67d&symbols=USD"
response = requests.get(url)
data = response.json()
response = data['rates']
d=response['USD']
k=q/d
print(100*k)

