import matplotlib
matplotlib.use("TKAgg")
import numpy as np
import matplotlib.pyplot as plt
import  mpl_finance
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.ticker as mticker
import datetime as dt
from matplotlib.widgets import Button,Cursor,TextBox
from matplotlib.backend_bases import cursors,FigureCanvasBase
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure


import tkinter as tk
from tkinter import ttk

#DDate = '19291001'
#Date = datetime.strptime(DDate, '%Y%m%d')
#Year = Date.year
#Month = Date.month
#Day =Date.day
#Star = '' ### remember to change number
''' GeoLines - SP 500 affected by the North Node, Neptune, Pluto and Saturn'''
Stardict = {
    "Sun" : [1,0,'Orange',[],"button10"],
    "Moon" : [2,0,'gray',[],"button10"],
    "Mercury" : [3,0,'gray',[],"button0"],
    "Venus" : [4,0,'yellow',[],"button1"],
    "Mars" : [5,0,'brown',[],"button2"],
    "Jupiter" : [6,0,'orange',[],"button3"],
    "Saturn" : [7,0,'gold',[],"button4"],
    "Uranus" : [8,0,'blue',[],"button5"],
    "Neptune" : [9,0,'Green',[],"button10"],
    "Pluto" : [10,0,'Green',[],"button10"],
    "North Node" : [11,0,'Green',[],"button10"],
    "U-S" : [12,0,'Green',[],"button6"],
    "U-J" : [13,0,'Green',[],"button7"],
    "U-M" : [14,0,'Green',[],"button8"],
    "U - V" :[15,0,'Green',[],"button9"], 
    "U - Me" : [16,0,'Green',[],"button10"],
    "S-J" : [17,0,'red',[],"button11"],
    "S -M" : [18,0,'Green',[],"button12"],
    "S - V" : [19,0,'Green',[],"button13"],
    "S - Me" : [20,0,'Green',[],"button14"],
    "J - M" : [21,0,'orange',[],"button15"],
    "J - V" : [22,0,'Green',[],"button15"],
    "J - Me" : [23,0,'Green',[],"button15"],
    "M - V" : [24,0,'Green',[],"button15"],
    "M - Me" : [25,0,'Green',[],"button15"],
    "V - Me" : [26,0,'Green',[],"button15"]
    }
#Angle = 30
#Lines = int(360/Angle)
dateshowing = 500
Clr1 = True
Clr2 = True
linesets = []
Cross_Zero = False
 


LARGE_FONT= ("Verdana", 12)


a = pd.read_csv('C:/Users/david/OneDrive/Desktop/Candlestick Plantery/^GSPC_Daily.csv')
cc = pd.read_csv('C:/Users/david/OneDrive/Desktop/Candlestick Plantery/Data/Geocentric Ephemerides (1900 - 2030).csv')

a['Date'] = pd.to_datetime(a["Date"], format="%m/%d/%Y")
cc['Date'] = pd.to_datetime(cc["Date"], format="%m/%d/%Y")

StartDate = '20180612'
StartDatetime = datetime.strptime(StartDate, '%Y%m%d')
latestdate = (a['Date'][len(a['Date'])-1])
print("The current set date: " , latestdate)
for q in range(len(a['Date'])):
    if a['Date'][q] == StartDatetime:
        StartDateindex = q
               
a = a[-(len(a['Date'])-StartDateindex):]
fig = plt.figure()
ax1=plt.subplot2grid((1,1), (0,0))

mpl_finance.candlestick_ohlc(ax1,zip(mdates.date2num(a['Date']),a['Open'], a['High'],
                                a['Low'], a['Close']),
                                width=1.6,colorup='#77d879', colordown='#db3f3f')

ax1.xaxis_date()
ax1.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')


ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
ax1.grid(True)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('SPY')
#plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)

MaxPrice = max(a['High']) * 1.05 
MinPrice = min(a['Low'])  * 0.90

#cursor = Cursor(ax1,horizOn=True,vertOn=True,color='green',linewidth=2.0)

        
def Addangle (Angle, num, star, nextnum):
    global Cross_Zero
    newnum = num + Angle
    if star < 7:
        if newnum > 360:
            newnum = newnum - 360
    else:
        if nextnum < num:
            newnum = num - Angle
            if newnum < 0:
                    Cross_Zero = True
                    newnum = Angle - abs(0 - num)
        if nextnum > num:
            newnum = num + Angle
            if newnum > 180:
                newnum = 360 - Angle - num
    return (newnum)

def findcloseset (list1, value):
    global Cross_Zero
    pass_zero_index = 0
    Zero_in_list = False
    if Cross_Zero == True:
        Cross_Zero = False
        for i in range (len(list1) -3):
            lastdiffv1 = abs(0 - list1[i+1])
            diffv1     = abs(0 - list1[i+2])
            nextdiffv1 = abs(0 - list1[i+3])
            if lastdiffv1>diffv1 and diffv1<nextdiffv1:
                pass_zero_index = i+2
                Zero_in_list = True
                break

        if Zero_in_list == False:
            pass
        else:
            for x in range (len(list1) -pass_zero_index-3):
                lastdiffv3 = abs(value - list1[pass_zero_index+x])
                diffv3     = abs(value - list1[pass_zero_index+x+1])
                nextdiffv3 = abs(value - list1[pass_zero_index+x+2])
                if lastdiffv3>diffv3 and diffv3<nextdiffv3:
                    indexs = list1.index(list1[pass_zero_index+x+1])
                    break    
    else:
        for x in range (len(list1) -3):
            lastdiff = abs(value - list1[x+1])       
            diff     = abs(value - list1[x+2])
            nextdiff = abs(value - list1[x+3])        
            if lastdiff>diff and diff<nextdiff:
                indexs = list1.index(list1[x+2])
                break
    return (indexs)

def Drawstar(Star):
    global Stardict
    Starindex = Stardict[Star][0]
    if Stardict[Star][1] == 0:
        b = pd.read_csv('C:/Users/david/OneDrive/Desktop/Candlestick Plantery/Ephemerides mmm.csv')
        b['Time'] = pd.to_datetime(b["Time"], format="%m/%d/%Y")
        NewDates = [Date]
        Cycle_index = pd.Index(b['Time']).get_loc(Date)
        for i in range(Lines):
            try: 
                Cycle_list = (b[Star][Cycle_index:]).values.tolist()
                x = Addangle(Angle,Cycle_list[0],Starindex,Cycle_list[1])
                y = findcloseset (Cycle_list , x)
                print('--------------------------')
                print(b['Time'][Cycle_index + y])
                print(b[Star][Cycle_index + y])
                NewDates = NewDates + [(b['Time'][Cycle_index + y])]
                Cycle_index = Cycle_index + y
            except UnboundLocalError:
                pass
        Stardict[Star][3] = [ax1.axvline(xx,color = Stardict[Star][2],visible = True) for xx in NewDates]
        Stardict[Star][1] = 2
        
        print('show')
    elif Stardict[Star][1] == 1:
        [yy.set_visible(True) for yy in Stardict[Star][3]]
        Stardict[Star][1] = 2
        print('show1')
    else:
        [yy.set_visible(False) for yy in Stardict[Star][3]]
        Stardict[Star][1] = 1
        print('show2')
    fig.canvas.draw()

def showStar(Star,self):
    global Stardict
    if Stardict[Star][1] == 1:
        [yy.set_visible(True) for yy in Stardict[Star][3]]
        Stardict[Star][1] = 0
        eval("self."+ Stardict[Star][4]+".configure(bg = 'green')")
    else:
        [yy.set_visible(False) for yy in Stardict[Star][3]]
        Stardict[Star][1] = 1
        eval("self."+ Stardict[Star][4]+".configure(bg = 'orange')")
    fig.canvas.draw()

def Moonphase(phase,self):
    if phase == 'New Moon':
        MoonDDate = ['20200124','20200223','20200324','20200422','20200522','20200621','20200720','20200818','20200917','20201016','20201115','20201214']
        for xx in (MoonDDate):
            MoonDate = datetime.strptime(xx, '%Y%m%d')
            ax1.axvline(MoonDate,color = 'black',visible = True)
    else:
        MoonDDate = ['20200110','20200209','20200309','20200407','20200507','20200605','20200705','20200803','20200902','20200101','20201031','20201130','20201229']
        for xx in (MoonDDate):
            MoonDate = datetime.strptime(xx, '%Y%m%d')
            ax1.axvline(MoonDate,color = 'yellow',visible = True)
    fig.canvas.draw()

def Clear(self):
    global Stardict
    global GeoPlt
    print(len(GeoPlt))
    print(Stardict["Mars"][3])
    print('------------')
    for z in Stardict:
        try: 
            for g in Stardict[z][3]:
                g.remove()
        except TypeError or ValueError :
            pass
        Stardict[z][3].clear()
        eval("self."+ Stardict[z][4]+".configure(bg = 'grey')")   

    try: 
        for c in GeoPlt:
            c.remove()
    except TypeError or ValueError :
        pass
        
    
    fig.canvas.draw()

def GeoShowLine(Combo1,self):
    global StartDatetime
    global latestdate
    global a
    global cc
    NumAddAfterStockDates = 30
    latestdate = pd.to_datetime(latestdate, format="%m/%d/%Y")
    
    for q in range(len(cc['Date'])):
        if cc['Date'][q] == StartDatetime:
            StartDateindex = q
            
    for u in range(len(cc['Date'])):
        if cc['Date'][u] == latestdate:
            latestDateindex = u            
               
    c = cc[StartDateindex:latestDateindex+NumAddAfterStockDates]

    PlanetName = Combo1.get()

    global GeoPlt
    GeoPlt = []
    GeoHarmonic = []
    CycleNum = 0
    global NewGeoList
    NewGeoList = []
    global MaxPrice 
    global MinPrice 
    global GeoDate
    GeoDate = []

    for i in range (StartDateindex,(latestDateindex+NumAddAfterStockDates-1)):
        if abs((c[PlanetName][i+1]-c[PlanetName][i])) < 340:
                NewGeoAngle = c[PlanetName][i+1] + (360*CycleNum)
                NewGeoList = NewGeoList + [NewGeoAngle]
                GeoDate = GeoDate + [c['Date'][i+1]]
                
        else:
            if (c[PlanetName][i+1]-c[PlanetName][i]) > 340:
                CycleNum = CycleNum - 1
                NewGeoAngle = c[PlanetName][i+1] + (360*CycleNum)
                NewGeoList = NewGeoList + [NewGeoAngle]
                GeoDate = GeoDate + [c['Date'][i+1]]
            else:
                CycleNum = CycleNum + 1
                NewGeoAngle = c[PlanetName][i+1] + (360*CycleNum)
                NewGeoList = NewGeoList + [NewGeoAngle]
                GeoDate = GeoDate + [c['Date'][i+1]]

 

    H = 0
    Checktoseeiflinehasdrawn = 0
    while True:
        Geox = []
        y = []
        maxindex = 0
        minindex = 0
        y  = [z+(360*H)for z in NewGeoList]

        ClsMax = Maxclosest(y,MinPrice,MaxPrice)
        ClsMin = Minclosest(y,MinPrice,MaxPrice)

        if ClsMax > MinPrice and ClsMax < MaxPrice:
            maxindex = y.index(ClsMax)


        if ClsMin > MinPrice and ClsMin < MaxPrice:
            minindex = y.index(ClsMin)

        if minindex <= maxindex: 
            y = y[minindex:maxindex]
            Geox = GeoDate[minindex:maxindex]
        else:
            y = y[maxindex:minindex]
            Geox = GeoDate[maxindex:minindex]

        GeoPlt = GeoPlt + [plt.plot(Geox,y,color = Stardict[PlanetName][2])[0]]
        GeoHarmonic = GeoHarmonic+[i]
        H = H +1
        
        if len(y)>1:
            Checktoseeiflinehasdrawn = 1
        if not y and Checktoseeiflinehasdrawn != 0:
            break
        '''if H == 7:
            break'''
    
    H = 0
    Checktoseeiflinehasdrawn = 0
    while True:
        Geox = []
        y = []
        maxindex = 0
        minindex = 0
        y  = [z-(360*H)for z in NewGeoList]

        ClsMax = Maxclosest(y,MinPrice,MaxPrice)
        ClsMin = Minclosest(y,MinPrice,MaxPrice)

        print(H,ClsMin,ClsMax)

        if ClsMax > MinPrice and ClsMax < MaxPrice:
            maxindex = y.index(ClsMax)

        if ClsMin > MinPrice and ClsMin < MaxPrice:
            minindex = y.index(ClsMin)

        if minindex <= maxindex: 
            y = y[minindex:maxindex]
            Geox = GeoDate[minindex:maxindex]
        else:
            y = y[maxindex:minindex]
            Geox = GeoDate[maxindex:minindex]

        GeoPlt =GeoPlt + [plt.plot(Geox,y,color = Stardict[PlanetName][2])[0]]
        GeoHarmonic = GeoHarmonic+[i]
        H = H +1
        
        if len(y)>1:
            Checktoseeiflinehasdrawn = 1
        if not y:
            break
        '''if H == 7:
            break'''
    

    fig.canvas.draw()

def Minclosest(lst, MinK, MaxK):
    
    MinValue = 0
    for x in range (len(lst)):
        if lst[x] >= MinK and lst[x] <= MaxK:
            MinValue = lst[x]

    return (MinValue)

def Maxclosest(lst, MinK, MaxK):
    
    MaxValue = 0
    x= len(lst) -1
    while x >= 0:
        if lst[x] >= MinK and lst[x] <= MaxK:
            MaxValue = lst[x]
        x -=1

    return (MaxValue)

def closest(lst, K): 

    MinK = []
    for x in range (len(lst)):
        if lst[x] >= K:
            MinK = MinK + [lst[x]]
            
    if not MinK:
        Mk = 0
    else:
        Mk = min(MinK)          
    return (Mk)

def InverseGeo (Combo1,self):
    global GeoPlt
    global a
    global NewGeoList
    global GeoDate

    InvCycle = 0

    global MaxPrice
    global MinPrice

    InvY = []
    Geox = []
    ax = GeoDate
    ay = NewGeoList
    PlanetName = Combo1.get()
        
    for i in range (len(ay)):
        if ay[i] < 360:
            InvY = InvY + [360-ay[i]]
        else:
            a = int(float(ay[i])/360)
            b = float(ay[i]) % 360
            c = 360 - b - (360 * a)
            InvY = InvY + [c]
    
    
    H = 0
    Checktoseeiflinehasdrawn = 0
    while True:
        maxindex = 0
        minindex = 0
        
        y  = [z+(360*H)for z in InvY]
     
        ClsMax = Maxclosest(y,MinPrice,MaxPrice)
        ClsMin = Minclosest(y,MinPrice,MaxPrice)

        if ClsMax > MinPrice and ClsMax < MaxPrice:
            maxindex = y.index(ClsMax)


        if ClsMin > MinPrice and ClsMin < MaxPrice:
            minindex = y.index(ClsMin)
            
        if minindex <= maxindex: 
            y = y[minindex:maxindex]
            Geox = ax[minindex:maxindex]
        else:
            y = y[maxindex:minindex]
            Geox = ax[maxindex:minindex]


        if len(y) > 0:
            GeoPlt = GeoPlt + [plt.plot(Geox,y,color = Stardict[PlanetName][2])[0]]
            H = H + 1
            Checktoseeiflinehasdrawn = 1
            

        if not y:
            if Checktoseeiflinehasdrawn == 1:
                break
            else:
                H = H +1
        
        '''print(H,maxindex,minindex)
        if H == 7:
            break'''


    fig.canvas.draw()


def ShowLine(E1,E2,E3,Combo1,E5,E6,self):
    DDate = E1.get() + E2.get() + E3.get()
    Date = datetime.strptime(DDate, '%Y%m%d')
    global Star
    Star = Combo1.get()
    Angle = int(E5.get())
    Lines = int(E6.get())
    global Stardict
    Starindex = Stardict[Star][0]
    b = pd.read_csv('C:/Users/david/OneDrive/Desktop/Candlestick Plantery/Ephemerides mmm.csv')
    b['Time'] = pd.to_datetime(b["Time"], format="%m/%d/%Y")
    NewDates = [Date]
    print(DDate)
    print(NewDates)
    Cycle_index = pd.Index(b['Time']).get_loc(Date)  ### initial index
    Cycle_Chaning_index = Cycle_index

    

    if len(Stardict[Star][3]) > 0:
        print(Stardict["Mars"][3])
        print('------------')   
        for g in Stardict[Star][3]:
                g.remove()
        Stardict[Star][3].clear()

    for i in range(Lines):
        try:
            print(i,NewDates)
            Cycle_list = (b[Star][Cycle_Chaning_index:]).values.tolist()    
            x = Addangle(Angle,Cycle_list[0],Starindex,Cycle_list[1])
            y = findcloseset (Cycle_list , x)
            Cycle_Chaning_index = Cycle_Chaning_index + y
            NewDates = NewDates + [(b['Time'][Cycle_Chaning_index])]
            

            print('--------------------------')
            print(b['Time'][Cycle_Chaning_index])
            print(Star, b[Star][Cycle_Chaning_index])


        except UnboundLocalError:
            print("error ")
            break
 
    Stardict[Star][3] = [ax1.axvline(xx,color = Stardict[Star][2],visible = True) for xx in NewDates]
    Stardict[Star][1] = 0
    eval("self."+ Stardict[Star][4]+".configure(bg = 'green')")
    #print(len(Stardict[Star][3]))
    fig.canvas.draw()

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Sea of BTC client")
          
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        ### Show Frames. If multiple windows, do a for loop here##
        self.frames = {}
        frame =PageThree(container,self)
        self.frames[PageThree] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(PageThree)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        ### Show Frames. If multiple windows, do a for loop here##
        

        

class PageThree(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="Year: ", font=LARGE_FONT)
        label1.place(x=0, y=0)

        E1 = tk.Entry(self)
        E1.insert(tk.END, "2018")  
        E1.place(x=60, y=0,relwidth=0.025,relheight=0.035)

        label2 = tk.Label(self, text="Month: ", font=LARGE_FONT)
        label2.place(x=140, y=0)

        E2 = tk.Entry(self)
        E2.insert(tk.END, "01")  
        E2.place(x=200, y=0,relwidth=0.025,relheight=0.035)

        label3 = tk.Label(self, text="Day: ", font=LARGE_FONT)
        label3.place(x=260, y=0)

        E3 = tk.Entry(self)
        E3.insert(tk.END, "29")  
        E3.place(x=300, y=0,relwidth=0.025,relheight=0.035)

        label4 = tk.Label(self, text="Star: ", font=LARGE_FONT)
        label4.place(x=0, y=50)

        Combo1 = ttk.Combobox(self, values=("Sun",
                                            "Moon",
                                            "Mercury",
                                            "Venus",
                                            "Mars",
                                            "Jupiter",
                                            "Saturn",
                                            "Uranus",
                                            "Neptune",
                                            "Pluto",
                                            "North Node",
                                            "U-S",
                                            "U-J",
                                            "U-M",
                                            "U - V", 
                                            "U - Me",
                                            "S-J",
                                            "S -M",
                                            "S - V",
                                            "S - Me",
                                            "J - M",
                                            "J - V",
                                            "J - Me",
                                            "M - V",
                                            "M - Me",
                                            "V - Me"), font=LARGE_FONT)
        Combo1.set("Mars")
        Combo1.place(x=60, y=50,relwidth=0.05, relheight=0.025)

        label5 = tk.Label(self, text="#Angles: ", font=LARGE_FONT)
        label5.place(x=190, y=50)

        E5 = tk.Entry(self)
        E5.insert(tk.END, "30")  
        E5.place(x=250, y=50,relwidth=0.02, relheight=0.02)

        label6 = tk.Label(self, text="#Lines: ", font=LARGE_FONT)
        label6.place(x=280, y=50)

        E6 = tk.Entry(self)
        E6.insert(tk.END, "12")  
        E6.place(x=340, y=50,relwidth=0.02, relheight=0.02)



        
##########
        self.button0 = tk.Button(self, text="Mercury",
                            command=lambda: showStar('Mercury',self))
        self.button0.place(x=1150, y=0,relwidth=0.04,relheight=0.03)

        self.button1 = tk.Button(self, text="Venus",
                            command=lambda: showStar('Venus',self))
        self.button1.place(x=1250, y=0,relwidth=0.04,relheight=0.03)

        self.button2 = tk.Button(self, text="Mars",
                            command=lambda: showStar('Mars',self))
        self.button2.place(x=1350, y=0,relwidth=0.04,relheight=0.03)

        self.button3 = tk.Button(self, text="Jupiter",
                            command=lambda: showStar('Jupiter',self))
        self.button3.place(x=1450, y=0,relwidth=0.04,relheight=0.03)
        
        self.button4 = tk.Button(self, text="Saturn",
                            command=lambda: showStar('Saturn',self))
        self.button4.place(x=1550, y=0,relwidth=0.04,relheight=0.03)

        self.button5 = tk.Button(self, text="Uranus",
                            command=lambda: showStar('Uranus',self))
        self.button5.place(x=1650, y=0,relwidth=0.04,relheight=0.03)

        self.button6 = tk.Button(self, text="U-S",
                            command=lambda: showStar('U-S',self))
        self.button6.place(x=1750, y=0,relwidth=0.04,relheight=0.03)

        self.button7 = tk.Button(self, text="U-J",
                            command=lambda: showStar('U-J',self))
        self.button7.place(x=1850, y=0,relwidth=0.04,relheight=0.03)

        self.button8 = tk.Button(self, text="U - V",
                            command=lambda: showStar('U - V',self))
        self.button8.place(x=1150, y=40,relwidth=0.04,relheight=0.03)

        self.button9 = tk.Button(self, text="U - V",
                            command=lambda: showStar('U - V',self))
        self.button9.place(x=1250, y=40,relwidth=0.04,relheight=0.03)
        
        self.button10 = tk.Button(self, text="U - Me",
                            command=lambda: showStar('U - Me',self))
        self.button10.place(x=1350, y=40,relwidth=0.04,relheight=0.03)

        self.button11 = tk.Button(self, text="S-J",
                            command=lambda: showStar('S-J',self))
        self.button11.place(x=1450, y=40,relwidth=0.04,relheight=0.03)
        
        self.button12 = tk.Button(self, text="S -M",
                            command=lambda: showStar('S -M',self))
        self.button12.place(x=1550, y=40,relwidth=0.04,relheight=0.03)

        self.button13 = tk.Button(self, text="S - V",
                            command=lambda: showStar('S - V',self))
        self.button13.place(x=1650, y=40,relwidth=0.04,relheight=0.03)

        self.button14 = tk.Button(self, text="S - Me",
                            command=lambda: showStar('S - Me',self))
        self.button14.place(x=1750, y=40,relwidth=0.04,relheight=0.03)

        self.button15 = tk.Button(self, text="J - M",
                            command=lambda: showStar('J - M',self))
        self.button15.place(x=1850, y=40,relwidth=0.04,relheight=0.03)
        
#########

        
        self.buttonMoon = tk.Button(self, text="New Moon Phase",
                            command=lambda: Moonphase('New Moon',self))
        self.buttonMoon.place(x=1050, y=0,relwidth=0.04,relheight=0.03)
        

        self.buttonMoon = tk.Button(self, text="Full Moon Phase",
                            command=lambda: Moonphase('Full Moon',self))
        self.buttonMoon.place(x=1050, y=40,relwidth=0.04,relheight=0.03)



###########
        

        self.button222 = tk.Button(self, text="Clear All",
                            command=lambda: Clear(self))
        self.button222.pack()

        self.button233 = tk.Button(self, text="ShowLine",
                            command=lambda: ShowLine(E1,E2,E3,Combo1,E5,E6,self))
        self.button233.pack()

        self.button244 = tk.Button(self, text="Drawgraph",
                            command=lambda: ShowLine())
        self.button244.pack()

        self.button255 = tk.Button(self, text="GeoShowLine",
                            command=lambda: GeoShowLine(Combo1,self))
        self.button255.place(x=550, y=0,relwidth=0.06,relheight=0.03)

        self.button266 = tk.Button(self, text="InverseGeo",
                            command=lambda: InverseGeo(Combo1,self))
        self.button266.place(x=550, y=40,relwidth=0.06,relheight=0.03)
        

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()


        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)        



        

app = SeaofBTCapp()
app.mainloop()

