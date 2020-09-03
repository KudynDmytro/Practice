import time
import requests

# Подключится к бирже Kuna ,
# # узнать текущий курс BTC-USD (продажа или покупка; можно сделать оба варианта) и сообщить его пользователю.
# # Создайте функцию, которая бы могла мониторить биржу с определенной периодичностью и сообщать пользователю об
# изменениях курса с указанием величины изменения по отношению к самому первому запросу.
res = requests.get('https://api.kuna.io/v3/exchange-rates/usd')

dct = res.json()
lst = dct.items()
print(dct)

for i in lst:
    if i[0] == 'btc':
        print('Покупка BTC за USD:', i)

lst_2 = []
# for i in res.json().values():
#     lst.append(i)


def monitor(req):
    s = req.json()
    new = []
    for i in s.values():
        new.append(i)
    print(new)
    if lst_2 != new:
        print(lst_2, 'changed ---->', new)
    time.sleep(2)
    monitor(req)


# monitor(res)


