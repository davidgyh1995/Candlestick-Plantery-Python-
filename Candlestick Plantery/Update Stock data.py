from pandas_datareader import data as pdr
import pandas as pd
import yfinance as yf
import csv
import datetime as dt
from datetime import timedelta
import numpy as np

with open('C:/Users/david/OneDrive/Desktop/Candlestick Plantery/^GSPC_Daily.csv') as fd:
    reader = csv.DictReader(fd)
    for row in reversed(list(reader)):
        if row['Date'] == '':
            pass
        else:
            print (row['Date'])
            Exceldate = (row['Date'])
            break

fd.close()

convertmdy = dt.datetime.strptime(Exceldate, '%m/%d/%Y')
convertmdy = convertmdy + timedelta(days=1)
convertymd = pd.to_datetime(str(convertmdy))
convertymd = convertymd.strftime('%Y-%m-%d')
print(type(convertymd))

Today = dt.date.today()
converttoday = pd.to_datetime(str(Today))
converttoday = converttoday.strftime('%Y-%m-%d')
print(converttoday)


data = pdr.get_data_yahoo("^GSPC", start=convertymd, end=converttoday)

Date  = data.index.to_numpy()
Date3 = []
for g in range (len(Date)):
    Date1 = pd.to_datetime(str(Date[g]))
    Date2 = Date1.strftime('%m/%d/%Y')
    Date3.append(Date2)
Open  = data.Open.to_numpy()
High  = data.High.to_numpy()
Low   = data.Low.to_numpy()
Close = data.Close.to_numpy()
AdjCls= data.Close.to_numpy()
Volume= data.Volume.to_numpy()


Rows = []
for i in range (len(Date)):
    Row = [Date3[i],Open[i],High[i],Low[i],Close[i],Close[i],Volume[i]]
    Rows.append(Row)

print(Rows)

with open('C:/Users/david/OneDrive/Desktop/Candlestick Plantery/^GSPC_Daily.csv','a',newline='') as fd:
    writer = csv.writer(fd)
    for j in range(len(Date)):
        writer.writerow(Rows[j])

fd.close()

print('Done!')
