import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import time as t
"""
    Uwaga program niedokończony!!!
"""
###### potrzebne funkcje
def unit_separation(str:str):# separates unit from string
    bools = []
    for i in str:
        if i != 'e' and i !='E':
            bools.append(i.lower().isalpha())
        else:
            bools.append(False)
    return str[bools.index(True):]
def readdata(filename:str):
    file = open(filename , 'r')
    data = pd.read_csv(file)
    column_names = data.columns
    file.close()
    print(f'Data column names: {list(column_names)}')
    return data, list(column_names)
def plot(filename:str, option:str) :
        data , col_names = readdata(filename= filename)
        fig1, (Volttime,Currtime) = plt.subplots(2)
        fig2 , (Volttemp,Currtemp,Temptime) = plt.subplots(3)
        fig1.tight_layout()
        fig2.tight_layout()
        if option == 'p':
            for i in (Volttemp,Currtemp,Temptime, Volttime,Currtime):
                i.clear()
            for i,j in zip((Volttime,Currtime,Volttemp,Currtemp,Temptime),("Voltage(Time)","Current(Time)","Voltage(Temperature)","Current(Temperature)","Temperature(Time)")):
                i.set_title(j)
            Volttime.plot(data[:][col_names[0]],data[:][col_names[1]])
            Currtime.plot(data.loc[:,col_names[0]], data.loc[:,col_names[2]])
            Volttemp.plot(data[:][col_names[4]],data[:][col_names[1]])
            Currtemp.plot(data.loc[:,col_names[4]], data.loc[:,col_names[2]])
            Temptime.plot(data.loc[:,col_names[0]],data.loc[:,col_names[4]])
            #Volttemp.invert_xaxis()
            #Currtemp.invert_xaxis()
            plt.show()
        else:
            pass
def liveplot(i,plot1,plot2,*plot3):
    
    
    pass
    
 ##########################################################
a , names= readdata("log@290K@_19th_00-57-42.csv")
filename = "log@290K@_19th_00-57-42.csv"
print(a.loc[:,names[4]])
print(f'do you want to plot all current data or start live data \np/l ')
option = 'p'
if option.lower() == 'p':
    plot(filename,option=option.lower())
elif option.lower() == 'l':
    data , col_names = readdata(filename= filename)
    fig1, (Volttime,Currtime) = plt.subplots(2)
    fig2 , (Volttemp,Currtemp,Temptime) = plt.subplots(3)
    fig1.tight_layout()
    fig2.tight_layout()
    #Volttemp.invert_xaxis()
    #Currtemp.invert_xaxis()
    pass
else:
    print("error wrong option selected")