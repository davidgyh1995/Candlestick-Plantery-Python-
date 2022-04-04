import matplotlib
matplotlib.use("TkAgg")
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
Stardict = {
    "Mercury" : [1,0,'gray',[],"button1"],
    "Venus" : [2,0,'yellow',[],"button2"],
    "Mars" : [3,0,'brown',[],"button3"],
    "Jupiter" : [4,0,'orange',[],"button4"],
    "Saturn" : [5,0,'gold',[],"button5"],
    "Uranus" : [6,0,'blue',[],"button6"],
    "U-S" : [7,0,'Green',[],"button7"],
    "U-J" : [8,0,'Green',[],"button8"],
    "U-M" : [9,0,'Green',[],"button9"],
    "U - V" :[10,0,'Green',[],"button10"], 
    "U - Me" : [11,0,'Green',[],"button1"],
    "S-J" : [12,0,'Green',[],"button12"],
    "S -M" : [13,0,'Green',[],"button1"],
    "S - V" : [14,0,'Green',[],"button1"],
    "S - Me" : [15,0,'Green',[],"button1"],
    "J - M" : [16,0,'Green',[],"button16"],
    "J - V" : [17,0,'Green',[],"button1"],
    "J - Me" : [18,0,'Green',[],"button1"],
    "M - V" : [19,0,'Green',[],"button1"],
    "M - Me" : [20,0,'Green',[],"button1"],
    "V - Me" : [21,0,'Green',[],"button1"]
    }
#Angle = 30
#Lines = int(360/Angle)
dateshowing = 500
Clr1 = True
Clr2 = True
linesets = []


LARGE_FONT= ("Verdana", 12)


a = pd.read_csv('C:/Users/David/Desktop/Candlestick Plantery/^GSPC_Monthly.csv')
a['Date'] = pd.to_datetime(a["Date"], format="%m/%d/%Y")
'''StartDate = '20180101'
StartDatetime = datetime.strptime(StartDate, '%Y%m%d')
print(StartDatetime)
for q in range(len(a['Date'])):
    if a['Date'][q] == StartDatetime:
        StartDateindex = q
               
a = a[StartDateindex:len(a)]'''

fig = plt.figure()
ax1=plt.subplot2grid((1,1), (0,0))

a.Open.astype(float)
a.High.astype(float)
a.Low.astype(float)
a.Close.astype(float)

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


#cursor = Cursor(ax1,horizOn=True,vertOn=True,color='green',linewidth=2.0)

        
def Addangle (Angle, num, star, nextnum):
    newnum = num + Angle
    if star < 7:
        if newnum > 360:
            newnum = newnum - 360
    else:
        if nextnum < num:
            newnum = num - Angle
            if newnum < 0:
                newnum = Angle - abs(0 - num)
        if nextnum > num:
            newnum = num +30
            if newnum > 180:
                newnum = 360 - Angle - num
    return (newnum)

def findcloseset (list1, value):
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
        b = pd.read_csv('C:/Users/David/Desktop/Candlestick Plantery/Ephemerides mmm.csv')
        b['Time'] = pd.to_datetime(b["Time"], format="%m/%d/%Y")
        NewDates = [Date]
        Cycle_index = pd.Index(b['Time']).get_loc(Date)
        for i in range(Lines):
            try: 
                Cycle_list = (b[Star][Cycle_index:]).values.tolist()
                print(Angle)
                print(Cycle_list[0])
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

def Clear():
    global Stardict
    for z in Stardict:
        try: 
            for g in Stardict[z][3]:
                g.remove()
        except TypeError:
            pass
    print("Clear")
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
    b = pd.read_csv('C:/Users/David/Desktop/Candlestick Plantery/Ephemerides mmm.csv')
    b['Time'] = pd.to_datetime(b["Time"], format="%m/%d/%Y")
    NewDates = [Date]
    Cycle_index = pd.Index(b['Time']).get_loc(Date)

    print(b['Time'][Cycle_index])
    print(Star, b[Star][Cycle_index])

    if len(Stardict[Star][3]) > 0:
        for g in Stardict[Star][3]:
                g.remove()

    for i in range(Lines):
        try:
            Cycle_list = (b[Star][Cycle_index:]).values.tolist()
            x = Addangle(Angle,Cycle_list[0],Starindex,Cycle_list[1])
            y = findcloseset (Cycle_list , x)
            print('--------------------------')
            print(b['Time'][Cycle_index + y])
            print(Star, b[Star][Cycle_index + y])
            NewDates = NewDates + [(b['Time'][Cycle_index + y])]
            Cycle_index = Cycle_index + y
        except UnboundLocalError:
            pass
    Stardict[Star][3] = [ax1.axvline(xx,color = Stardict[Star][2],visible = True) for xx in NewDates]
    Stardict[Star][1] = 0
    eval("self."+ Stardict[Star][4]+".configure(bg = 'green')")
    print(len(Stardict[Star][3]))
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
        E1.place(x=60, y=0,relwidth=0.025)

        label2 = tk.Label(self, text="Month: ", font=LARGE_FONT)
        label2.place(x=0, y=25)

        E2 = tk.Entry(self)
        E2.insert(tk.END, "10")  
        E2.place(x=60, y=25,relwidth=0.025)

        label3 = tk.Label(self, text="Day: ", font=LARGE_FONT)
        label3.place(x=0, y=50)

        E3 = tk.Entry(self)
        E3.insert(tk.END, "01")  
        E3.place(x=60, y=50,relwidth=0.025)
##########
        label4 = tk.Label(self, text="Star: ", font=LARGE_FONT)
        label4.place(x=140, y=0)

        Combo1 = ttk.Combobox(self, values=("Mercury",
                                            "Venus",
                                            "Mars",
                                            "Jupiter",
                                            "Saturn",
                                            "Uranus",
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
        Combo1.place(x=200, y=0,relwidth=0.05)

        label5 = tk.Label(self, text="#Angles: ", font=LARGE_FONT)
        label5.place(x=120, y=25)

        E5 = tk.Entry(self)
        E5.insert(tk.END, "30")  
        E5.place(x=200, y=25,relwidth=0.05)

        label6 = tk.Label(self, text="#Lines: ", font=LARGE_FONT)
        label6.place(x=120, y=50)

        E6 = tk.Entry(self)
        E6.insert(tk.END, "12")  
        E6.place(x=200, y=50,relwidth=0.05)



        
##########

        self.button1 = tk.Button(self, text="Mercury",
                            command=lambda: showStar('Mercury',self))
        self.button1.place(x=1300, y=0,relwidth=0.04,relheight=0.03)

        self.button2 = tk.Button(self, text="Venus",
                            command=lambda: showStar('Venus',self))
        self.button2.place(x=1400, y=0,relwidth=0.04,relheight=0.03)
        
        self.button3 = tk.Button(self, text="Mars",
                            command=lambda: showStar('Mars',self))
        self.button3.place(x=1500, y=0,relwidth=0.04,relheight=0.03)

        self.button4 = tk.Button(self, text="Jupiter",
                            command=lambda: showStar('Jupiter'))
        self.button4.place(x=1600, y=0,relwidth=0.04,relheight=0.03)

        self.button5 = tk.Button(self, text="Saturn",
                            command=lambda: showStar('Saturn'))
        self.button5.place(x=1700, y=0,relwidth=0.04,relheight=0.03)

        self.button6 = tk.Button(self, text="Uranus",
                            command=lambda: showStar('Uranus'))
        self.button6.place(x=1800, y=0,relwidth=0.04,relheight=0.03)

        self.button7 = tk.Button(self, text="U-S",
                            command=lambda: showStar('U-S'))
        self.button7.place(x=1300, y=40,relwidth=0.04,relheight=0.03)
        
        self.button8 = tk.Button(self, text="U-J",
                            command=lambda: showStar('U-J'))
        self.button8.place(x=1400, y=40,relwidth=0.04,relheight=0.03)

        self.button9 = tk.Button(self, text="U-M",
                            command=lambda: showStar('U-M'))
        self.button9.place(x=1500, y=40,relwidth=0.04,relheight=0.03)
        
        self.button10 = tk.Button(self, text="U - V",
                            command=lambda: showStar('U - V'))
        self.button10.place(x=1600, y=40,relwidth=0.04,relheight=0.03)

        self.button16 = tk.Button(self, text="J - M",
                            command=lambda: showStar('J - M'))
        self.button16.place(x=1700, y=40,relwidth=0.04,relheight=0.03)

        self.button12 = tk.Button(self, text="S-J",
                            command=lambda: showStar('S-J'))
        self.button12.place(x=1800, y=40,relwidth=0.04,relheight=0.03)

        self.button13 = tk.Button(self, text="empty",
                            command=lambda: showStar('S-J'))
        self.button13.place(x=1200, y=0,relwidth=0.04,relheight=0.03)

        self.button14 = tk.Button(self, text="empty",
                            command=lambda: showStar('S-J'))
        self.button14.place(x=1200, y=40,relwidth=0.04,relheight=0.03)        
        
        self.button15 = tk.Button(self, text="empty",
                            command=lambda: showStar('S-J'))
        self.button15.place(x=1100, y=0,relwidth=0.04,relheight=0.03)        
        
        self.button16 = tk.Button(self, text="empty",
                            command=lambda: showStar('S-J'))
        self.button16.place(x=1100, y=40,relwidth=0.04,relheight=0.03)  

        self.button17 = tk.Button(self, text="empty",
                            command=lambda: showStar('S-J'))
        self.button17.place(x=1000, y=0,relwidth=0.04,relheight=0.03)

        self.button18 = tk.Button(self, text="empty",
                            command=lambda: showStar('S-J'))
        self.button18.place(x=1000, y=40,relwidth=0.04,relheight=0.03)  


###########
        

        self.button222 = tk.Button(self, text="Clear All",
                            command=lambda: Clear())
        self.button222.pack()

        self.button233 = tk.Button(self, text="ShowLine",
                            command=lambda: ShowLine(E1,E2,E3,Combo1,E5,E6,self))
        self.button233.pack()

        self.button244 = tk.Button(self, text="Drawgraph",
                            command=lambda: ShowLine())
        self.button244.pack()

        
        


        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()


        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)        



        

app = SeaofBTCapp()
app.mainloop()

