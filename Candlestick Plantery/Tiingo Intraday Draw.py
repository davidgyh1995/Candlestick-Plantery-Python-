import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.animation as animation
from matplotlib.widgets import Button, TextBox
from datetime import datetime,date,timedelta

'''Initialize and read csv'''

'''What to do next?
    1. Download historical data (1 hr) 
    2. see if realtime data only add to the bottom of the csv, not creat a new file every time
    3. Merge Geo lines to here
    4. See to have dropbox
    5.Everytime load a data first then realtime (refresh everytime?)
    6.3 change variable downstair i index and x index
    6.3 offset problem; not locate in the low price
    6.3 Find 1 hour chart so the angle line will show
    6.3 Scale? Adding more buttons
'''

a = pd.read_csv('C:/Users/david/OneDrive/Desktop/Candlestick Plantery/Test_Data/Geo_1min_MayToJune.csv')
a['Date'] = pd.to_datetime(a["Date"], format="%d.%m.%Y %H:%M:%S")



test_date = '202162'
test_hour = '21'
test_datetime = test_date + test_hour

Realtime_data = pd.read_csv('Realtime_data.csv', index_col=0, parse_dates=True)

list_ForDrawing = []
'''Old Code'''

def Sq_Line_Draw(E1, E2, E3, Combo1, E7, E8, E9, E10):
    ''' E7 = End Date
        E8 = High/Low
        E9 = Scale
        E10 = UP/down
    '''
    global a
    global GeoPlt
    global cycle

    StartDate_Sq_Line = '20216221'
    EndDate_Sq_Line = '20216222'

    PlanetName = Combo1
    Sq_Line_Xdate = (a['Date'])
    Sq_Line_Yangle = (a[PlanetName])

    Start_index = 0
    End_index = 0

    L_or_H = E8
    Scale_Sq_Line = float(E9)
    UpOrDown = E10
    #StarDatetime_Sq_Line = datetime.strptime(StartDate_Sq_Line, '%Y%m%d')
    #EndDatetime_Sq_Line = datetime.strptime(EndDate_Sq_Line, '%Y%m%d')
    '''Probably don't need b/c this code is for hour/mins Ymd not apply.'''

    for x_index in range(len(Sq_Line_Xdate)):
        a_pd_datetime = str(Sq_Line_Xdate[x_index].year) + str(Sq_Line_Xdate[x_index].month) + str(
            Sq_Line_Xdate[x_index].day) + str(Sq_Line_Xdate[x_index].hour)
        if a_pd_datetime == test_datetime:
            Sq_Line_Xdate = (Sq_Line_Xdate[x_index:x_index+2])
            Sq_Line_Yangle = (Sq_Line_Yangle[x_index:x_index+2])
            break


    Sq_Line_Yangle = Sq_Line_Yangle.values.tolist()

    cycle_Sq_Line = 0
    Before_Added_Cycle = Sq_Line_Yangle[0]

    for cycle_index in range(1, len(Sq_Line_Yangle)):
        cycle_added_degree = cycle_Sq_Line * 360
        if abs(Sq_Line_Yangle[cycle_index] - Before_Added_Cycle) > 300:
            cycle_Sq_Line = cycle_Sq_Line + 1
            Before_Added_Cycle = Sq_Line_Yangle[cycle_index]
            Sq_Line_Yangle[cycle_index] = Sq_Line_Yangle[cycle_index] + (cycle_Sq_Line * 360)
        else:
            Before_Added_Cycle = Sq_Line_Yangle[cycle_index]
            Sq_Line_Yangle[cycle_index] = Sq_Line_Yangle[cycle_index] + cycle_added_degree

    for Realtime_i_index in range (len(Realtime_data.index)):
        Realtime_datetime = str(Realtime_data.index[Realtime_i_index].year) + str(Realtime_data.index[Realtime_i_index].month) + str(
            Realtime_data.index[Realtime_i_index].day) + str(Realtime_data.index[Realtime_i_index].hour)
        if Realtime_datetime == test_datetime:
            Realtime_x_index = Realtime_i_index
            break

    Off_Set = [Realtime_data[L_or_H][Realtime_x_index].tolist()]

    print('offset: ', Off_Set)

    New_Yangle = Off_Set

    if UpOrDown == "Up":
        for o_index in range(len(Sq_Line_Yangle) - 1):
            New_Yangle = New_Yangle + [
                (Sq_Line_Yangle[o_index + 1] - Sq_Line_Yangle[0]) * Scale_Sq_Line + float(Off_Set[0])]
    else:
        for o_index in range(len(Sq_Line_Yangle) - 1):
            New_Yangle = New_Yangle + [
                (Sq_Line_Yangle[0] - Sq_Line_Yangle[o_index + 1]) * Scale_Sq_Line + float(Off_Set[0])]

    print('final: ',Sq_Line_Xdate,New_Yangle)

    '''drawing angle trend line on matplotlib, note that xdate needs to used iloc for 0, and New_Yangle don't need iloc'''
    for i_lstwithinlst in range(len(Sq_Line_Xdate)):
        list_ForDrawing.append([Sq_Line_Xdate.iloc[i_lstwithinlst], New_Yangle[i_lstwithinlst]])

    print('drawinglist: ',list_ForDrawing)
'''Search Geo file for the angle on specific date that matches with testdate'''




print(test_datetime)

Sq_Line_Draw('2021', '6', '2', 'Sun', None, 'low', 1, 'Up')

'''for i_Geo in range (len(a)):
    str_datetime = str(a['Date'][i_Geo].year)+str(a['Date'][i_Geo].month)+str(a['Date'][i_Geo].day)+str(a['Date'][i_Geo].hour)
    if str_datetime == test_datetime:
        #print (a['Sun'][i_Geo])
        Sq_Line_Xdate = (a['Date'][i_Geo:i_Geo + 2])
        Sq_Line_Yangle = (a['Sun'][i_Geo:i_Geo + 2])
        break'''



'''Creat a new list with in list for aline drawing'''




#print(str(a['Date'][1].year)+str(a['Date'][1].month)+str(a['Date'][1].day)+str(a['Date'][1].hour))



'''Setting up figures and Animation'''

fig = mpf.figure(style='charles')
ax1 = fig.add_subplot(1,1,1)


def Draw_Line(event):
    print("Ok!")

def Line_Data(text):
    Txt_Data = eval(text)
    print(Txt_Data)

def animate(i):
    Realtime_data = pd.read_csv('Realtime_data.csv', index_col=0, parse_dates=True)
    Realtime_data.index.name = 'date'
    ax1.clear()
    mpf.plot(Realtime_data,ax=ax1,style='charles',type='candle',alines=dict(alines=list_ForDrawing))



#GeoPlt = mpf.make_addplot
#mpf.plot(Sq_Combined,volume=True,addplot=GeoPlt)


ani = animation.FuncAnimation(fig, animate, interval=1000)


'''Below are button stuff'''

ax_Draw_Line = plt.axes([0.02, 0.2, 0.1, 0.075])
b_Draw_Line = Button(ax_Draw_Line, 'Draw Line')
b_Draw_Line.on_clicked(Draw_Line)

ax_Line_Data = plt.axes([0.02, 0.1, 0.1, 0.075])
b_Line_Data = TextBox(ax_Line_Data, 'Draw Line')
b_Line_Data.on_submit(Line_Data)

mpf.show()