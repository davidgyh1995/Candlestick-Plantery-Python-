'''from pandas import DataFrame
from datetime import datetime,date
import csv
import time
import requests

d = date(2021,5,27)

unixtime = time.mktime(d.timetuple())

while True:

    headers = {
        'Content-Type': 'application/json'
    }
    #requestResponse = requests.get("https://api.tiingo.com/tiingo/crypto/prices?tickers=btcusd&exchanges=Bitstamp&resampleFreq=30min&token=63f454a49a441ea0508cee7b4fa46767085f9f4c", headers=headers)
    requestResponse = requests.get('https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1&since=%s'%unixtime)

    x = requestResponse.json()



    df = DataFrame (x['result']['XXBTZUSD'],columns=['date','open','high','low','close','volume','tradesDone','volumeNotional'])

    print(df['open'])
    for i in range(len(df)):
        Normal_Date = datetime.utcfromtimestamp(df['date'][i]).strftime('%Y-%m-%d %H:%M:%S')
        df.loc[i, 'date'] = Normal_Date

    print(df)

    time.sleep(60)'''

import csv
import random
import time

'''x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        print("x: ",x_value)
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    time.sleep(1)'''

xdate = [[1,2,3],[5,6,7]]
yopen = [[5,6,7],[5,6,7],[7,8,9]]

print(xdate[0:-1])

'''
fieldnames = ["date", "open"]

with open('Realtime_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

with open('Realtime_data.csv', 'a', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    for xdate_index in range (len(xdate)):
        info = {
            "date": xdate[xdate_index],
            "open": yopen[xdate_index],

        }
        csv_writer.writerow(info)'''