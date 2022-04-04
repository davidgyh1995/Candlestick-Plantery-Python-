from tkinter import *
import pandas as pd

Data = pd.read_csv('C:/Users/david/OneDrive/Desktop/Candlestick Plantery/irrigation_data.csv')
root = Tk()
root.geometry("600x600")


def acc_data():
    Ct = Crop_Type_Clicked.get()
    Region = Region_Clicked.get()
    water_cost = float(Water_Cost_Clicked.get())
    water_need = float(Water_Needed_Clicked.get())

    print(Region,water_cost,type(water_need))
    for i in range (len(Data)):
        if Data['crop_type'][i] == Ct:
            if Data['county'][i] == Region:
                if Data['water_cost_adj'][i] == water_cost:
                    if Data['water_need_adj'][i] == water_need:
                        print("The expected water cost is: ",Data['Exp_water_cost'][i])
                        myLabel = Label(root, text=(Data['Exp_water_cost'][i]).pack()
                        break




def show():
    myLabel = Label(root,text=clicked.get()).pack()

Crop_Type_Menu = ["Almonds","Cherries","Grapes/Raisins","Grapes/Table","Grapes/Wine","Peaches","Plums","Peaches","Prunes"]
Crop_Type_Clicked = StringVar()
Crop_Type_Clicked.set("Crop Type")
drop = OptionMenu (root, Crop_Type_Clicked, *Crop_Type_Menu)
drop.pack()
#############################################################################
Start_Irrigation_Menu = ["Jan","Feb","Mar","Apr","May","Jun","Jly","Aug","Sep","Oct","Nov","Dec"]
Start_Irrigation_Clicked = StringVar()
Start_Irrigation_Clicked.set("Start Irrigation")
drop = OptionMenu (root, Start_Irrigation_Clicked, *Start_Irrigation_Menu)
drop.pack()
#############################################################################
End_Irrigation_Menu = ["Jan","Feb","Mar","Apr","May","Jun","Jly","Aug","Sep","Oct","Nov","Dec"]
End_Irrigation_Clicked = StringVar()
End_Irrigation_Clicked.set("End Irrigation")
drop = OptionMenu (root, End_Irrigation_Clicked, *End_Irrigation_Menu)
drop.pack()
#############################################################################
Region_Menu = ["Alameda","Kings,Fresno,Tulare,Kern","San Joaquin, Stanislaus,Merced,Madera","Tehama, Glenn, Butte, Colusa, Yuba, Yolo, Sutter, Solano, Sacramento","San Francisco, San Mateo, Contra Costa, Alameda","Del Norte, Humboldt, Mendocino, Lake, Sonoma, Napa, Marin","Sierra, Nevada"]
Region_Clicked = StringVar()
Region_Clicked.set("Region")
drop = OptionMenu (root, Region_Clicked, *Region_Menu)
drop.pack()
#############################################################################
Pump_Cost_Menu = ["1","2"]
Pump_Cost_Clicked = StringVar()
Pump_Cost_Clicked.set("Pump Cost")
drop = OptionMenu (root, Pump_Cost_Clicked, *Pump_Cost_Menu)
drop.pack()
#############################################################################
Horse_Power_Menu = ["1","2"]
Horse_Power_Clicked = StringVar()
Horse_Power_Clicked.set("Horse Power")
drop = OptionMenu (root, Horse_Power_Clicked, *Horse_Power_Menu)
drop.pack()
#############################################################################
Irrigation_Amount_Menu = ["1","2"]
Irrigation_Amount_Clicked = StringVar()
Irrigation_Amount_Clicked.set("Irrigation Amount")
drop = OptionMenu (root, Irrigation_Amount_Clicked, *Irrigation_Amount_Menu)
drop.pack()
#############################################################################
Rain_Fall_Menu = ["1","2"]
Rain_Fall_Clicked = StringVar()
Rain_Fall_Clicked.set("Rain Fall")
drop = OptionMenu (root, Rain_Fall_Clicked, *Rain_Fall_Menu)
drop.pack()
#############################################################################
Water_Cost_Menu = [1,2,264]
Water_Cost_Clicked = StringVar()
Water_Cost_Clicked.set("Water Cost")
drop = OptionMenu (root, Water_Cost_Clicked, *Water_Cost_Menu)
drop.pack()
#############################################################################
Water_Needed_Menu = [1,2,4.33]
Water_Needed_Clicked = StringVar()
Water_Needed_Clicked.set("Water Needed")
drop = OptionMenu (root, Water_Needed_Clicked, *Water_Needed_Menu)
drop.pack()
#############################################################################

myButton = Button(root, text = "Show Sel", command = acc_data).pack()
root.mainloop()