import pandas as pd
from pandas import DataFrame
from datetime import datetime,date,timedelta
import csv
import time
import requests

Time_Int_Boolean = True


fieldnames = ["date", "open","high","low","close","volume"]


with open('Realtime_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    d = datetime.now() - timedelta(minutes=240)
    unixtime = time.mktime(d.timetuple())

    if Time_Int_Boolean == True:
        d = datetime.now() - timedelta(minutes=240)
        unixtime = time.mktime(d.timetuple())
        Time_Int_Boolean = False
    else:
        d = datetime.now()- timedelta(minutes=2)
        unixtime = time.mktime(d.timetuple())


    headers = {
        'Content-Type': 'application/json'
    }

    requestResponse = requests.get('https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=1&since=%s' % unixtime)
    x = requestResponse.json()

    df = DataFrame(x['result']['XXBTZUSD'],
                   columns=['date', 'open', 'high', 'low', 'close', 'volume', 'tradesDone', 'volumeNotional'])

    print('df: ',Time_Int_Boolean,df)
    #Normal_Date = datetime.utcfromtimestamp(df['date']).strftime('%Y-%m-%d %H:%M:%S')
    xdate=pd.to_datetime(df['date'][0:-1],unit = 's')
    yopen=(df['open'][0:-1])
    yhigh=(df['high'][0:-1])
    ylow=(df['low'][0:-1])
    yclose=(df['close'][0:-1])
    yvolume=(df['volume'][0:-1])

    '''
    Normal_Date = datetime.utcfromtimestamp(df['date'][df.index[-2]]).strftime('%Y-%m-%d %H:%M:%S')
    xdate=Normal_Date
    yopen=(df['open'][df.index[-2]])
    yhigh=(df['high'][df.index[-2]])
    ylow=(df['low'][df.index[-2]])
    yclose=(df['close'][df.index[-2]])
    yvolume=(df['volume'][df.index[-2]])
    print(type(xdate))
    print(type(yopen))
    
    '''

    with open('Realtime_data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for xdate_index in range(len(xdate)):
            info = {
                "date": xdate[xdate_index],
                "open": yopen[xdate_index],
                "high": yhigh[xdate_index],
                "low": ylow[xdate_index],
                "close": yclose[xdate_index],
                "volume": yvolume[xdate_index],
            }
            csv_writer.writerow(info)

    print(xdate.iloc[-1])
    print(datetime.now())
    time.sleep(60)

