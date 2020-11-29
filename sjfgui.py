from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
#import time
import os
#creating the application main window
parent = Tk()




parent.geometry("1000x800")  
title = Label(parent,text = "SCHEDULING ALGORITHMS")
title.pack()  




def sj():# function to create progress bars for the processes to display execution  and the run time information
    import time
    
    start= Label(parent,text="START").place(x=150,y=500)
    prog1 = Progressbar(parent, orient = HORIZONTAL, length = 130, mode = 'determinate',maximum=output[0])
    prog1.place(x=200,y=500)
    pt1= str(output[0])
    progtime1 = Label(parent,text=pt1 +" seconds").place(x=255,y=510)
    #plabel= Label(parent,text="P")
    prog2 = Progressbar(parent, orient = HORIZONTAL, length = 130, mode = 'determinate',maximum=output[1])
    prog2.place(x=334,y=500)
    pt2= str(output[1])
    progtime2 = Label(parent,text=pt2 +" seconds").place(x=384,y=510)
    prog3 = Progressbar(parent, orient = HORIZONTAL, length = 130, mode = 'determinate',maximum=output[2])
    prog3.place(x=470,y=500)
    pt3= str(output[2])
    progtime3 = Label(parent,text=pt3 +" seconds").place(x=520,y=510)
    prog4 = Progressbar(parent, orient = HORIZONTAL, length = 130, mode = 'determinate',maximum=output[3])
    prog4.place(x=605,y=500)
    pt4= str(output[3])
    progtime4 = Label(parent,text=pt4 +" seconds").place(x=655,y=510)
    prog5 = Progressbar(parent, orient = HORIZONTAL, length = 130, mode = 'determinate',maximum=output[4])
    prog5.place(x=742,y=500)
    pt5= str(output[4])
    progtime5 = Label(parent,text=pt5 +" seconds").place(x=792,y=510)
    
    
    for i in range(output[0]):
        prog1['value'] +=1
        parent.update() 
        time.sleep(0.75)
    time.sleep(1)
   
    for j in range(output[1]):
        prog2['value'] +=1
        parent.update() 
        time.sleep(0.75)
    time.sleep(1)
    
    for k in range(output[2]):
        prog3['value'] +=1
        parent.update() 
        time.sleep(0.75)
    time.sleep(1)
   
    for l in range(output[3]):
        prog4['value'] +=1
        parent.update() 
        time.sleep(0.75)
    time.sleep(1)
   
    for m in range(output[4]):
        prog5['value'] +=1
        parent.update() 
        time.sleep(0.75) 
   # time.sleep(2) 
    

       
    
    
    
 
SJF = Button(parent,text = "SHORTEST JOB FIRST",command=sj).place(x=100,y=130)
FCFS = Button(parent,text = "FIRST COME FIRST SERVE",command=sj).place(x=280,y=130)
PP = Button(parent,text = "PRIORITY",command=sj).place(x=484,y=130)
RR = Button(parent,text = "ROUND ROBIN").place(x = 630,y = 130)


pHeader = Label(parent,text="Process").place(x=100,y=200)
bheader= Label(parent,text="Burst Time").place(x=170,y=200)
bheader= Label(parent,text="Execute Order ").place(x=310,y=200)
wHeader = Label(parent,text="Wait Time").place(x=440,y=200)
wHeader = Label(parent,text="Turnaround Time").place(x=550,y=200)
wHeader = Label(parent,text="Priority").place(x=670,y=200)
#wHeader = Label(parent,text="Average Wait Time").place(x=600,y=600)
#wHeader = Label(parent,text="Average Turnaround Time").place(x=500,y=500)
#T.pack()

p1 = Label(parent,text="P1")# Process labels
p1.place(x=100,y=237)
p2 = Label(parent,text="P2")
p2.place(x = 100,y = 270)
p3 = Label(parent,text="P3")
p3.place(x = 100,y = 303)
p4 = Label(parent,text="P4")
p4.place(x = 100,y = 333)
p5 = Label(parent,text="P5")
p5.place(x = 100,y = 367)



b1 = Entry(parent)# positoning the labels for process numbers
b1.place(x = 170,y = 237)
b2 = Entry(parent)
b2.place(x = 170,y = 270)
b3 = Entry(parent)
b3.place(x = 170,y = 303)
b4 = Entry(parent)
b4.place(x = 170,y = 333)
b5 = Entry(parent)
b5.place(x = 170,y = 367)

prt1 = Entry(parent)# positoning the entry boxes for priority numbers
prt1.place(x = 670,y = 237)
prt2 = Entry(parent)
prt2.place(x = 670,y = 270)
prt3 = Entry(parent)
prt3.place(x = 670,y = 303)
prt4 = Entry(parent)
prt4.place(x = 670,y = 333)
prt5 = Entry(parent)
prt5.place(x = 670,y = 367)

output = []
priorityS=[]
bt=[] = output
srtd=[]
wt=[]
ttime=[]
processes=[]
n=5# number of overall processes/maximum possibe processes

def prstore():# store values in prioristy array
    priorityS.append(int(prt1.get()))
    priorityS.append(int(prt2.get()))
    priorityS.append(int(prt3.get()))
    priorityS.append(int(prt4.get()))
    priorityS.append(int(prt5.get()))
    print(priorityS)



def store(): #stores the input from the user for SJF into the queue for processing
    #output = []
    output.append(int(b1.get()))
    output.append(int(b2.get()))
    output.append(int(b3.get()))
    output.append(int(b4.get()))
    output.append(int(b5.get()))
    print(output)

def proc():
    for i in range(0,n):
        processes.insert(i,i+1)

def sort():#applies bubble sort to sort process according to their burst time to find the Shortest Job
    for i in range(0,len(output)-1):  
        for j in range(0,len(output)-i-1):
             if(output[j]>output[j+1]):
                temp=output[j]
                output[j]=output[j+1]
                output[j+1]=temp
                temp=processes[j]
                processes[j]=processes[j+1]
                processes[j+1]=temp

def prioritySort(): #Funtion to sort burst times, based on the priority
    for i in range(0,len(priorityS)-1):
        for j in range(0,len(priorityS)-i-1):
            if(priorityS[j]>priorityS[j+1]):
                swap=priorityS[j]
                priorityS[j]=priorityS[j+1]
                priorityS[j+1]=swap

                swap=output[j]
                output[j]=output[j+1]
                output[j+1]=swap

                swap=processes[j]
                processes[j]=processes[j+1]
                processes[j+1]=swap


def waitTime():# function to calculate the wait time for each process as well as average wait time time and turnaround time
    avgwt=0
    avgtat=0
    wt.insert(0,0)
    ttime.insert(0,output[0])
    
    
    for i in range(1,len(output)):  
        wt.insert(i,wt[i-1] + output[i-1])
        ttime.insert(i,wt[i]+output[i])
       
        avgwt+=wt[i]
        avgtat+=ttime[i]

    avgwt=float(avgwt)/n
    avgtat=float(avgtat)/n
    avgwt= str(avgwt)
    avgtat = str(avgtat)
    AWT = Label(parent,text="Average Wait Time: "+avgwt).place(x=200,y=540)
    ATT = Label(parent,text="Average Turnaround Time: "+avgtat).place(x=200,y=560)


       


def updateWaitTime():# function that displays to wait time of each process
    wt1= str(wt[0])
    wt1=Label(parent, text=wt1)
    wt1.place(x = 470,y = 237)
    wt2= str(wt[1])
    wt2=Label(parent, text=wt2)
    wt2.place(x = 470,y = 270)
    wt3= str(wt[2])
    wt3=Label(parent, text=wt3)
    wt3.place(x = 470,y = 303)
    wt4= str(wt[3])
    wt4=Label(parent, text=wt4)
    wt4.place(x = 470,y = 333)
    wt5= str(wt[4])
    wt5=Label(parent, text=wt5)
    wt5.place(x = 470,y = 367)





def executeOrder():# function that displays the exuction order of the processes
    eo1= str(processes[0])
    eo11= str(processes[0])
    eo11=Label(parent, text="P"+eo11)
    eo1=Label(parent, text="P"+eo1)
    eo11.place(x=255,y=480)
    eo1.place(x = 340,y = 237)

    eo2= str(processes[1])
    eo22= str(processes[1])
    eo22=Label(parent, text="P"+eo22)
    eo2=Label(parent, text="P"+eo2)
    eo22.place(x=384,y=480)
    eo2.place(x = 340,y = 270)

    eo3= str(processes[2])
    eo33= str(processes[2])
    eo33=Label(parent, text="P"+eo33)
    eo3=Label(parent, text="P"+eo3)
    eo33.place(x=520,y=480)
    eo3.place(x = 340,y = 303)

    eo4= str(processes[3])
    eo44= str(processes[3])
    eo44=Label(parent, text="P"+eo44)
    eo4=Label(parent, text="P"+eo4)
    eo44.place(x=655,y=480)
    eo4.place(x = 340,y = 333)

    eo5= str(processes[4])
    eo55= str(processes[4])
    eo55=Label(parent, text="P"+eo55)
    eo5=Label(parent, text="P"+eo5)
    eo55.place(x=740,y=480)
    eo5.place(x = 340,y = 367)

def updateTT():#function that displays turnaround times
    tt1= str(ttime[0])
    tt1=Label(parent, text=tt1)
    tt1.place(x = 580,y = 237)
    tt2= str(ttime[1])
    tt2=Label(parent, text=tt2)
    tt2.place(x = 580,y = 270)
    tt3= str(ttime[2])
    tt3=Label(parent, text=tt3)
    tt3.place(x = 580,y = 303)
    tt4= str(ttime[3])
    tt4=Label(parent, text=tt4)
    tt4.place(x = 580,y = 333)
    tt5= str(ttime[4])
    tt5=Label(parent, text=tt5)
    tt5.place(x = 580,y = 367)






    
    
    
    
    
#Load values for SJF Calculations
Button(parent,text="Load",command=lambda:[store(),proc(),sort(),waitTime(),executeOrder(),updateWaitTime(),updateTT()]).place(x = 100,y = 100)

##Load values for FCFS Calculations
Button(parent,text="Load",command=lambda:[store(),proc(),waitTime(),executeOrder(),updateWaitTime(),updateTT()]).place(x = 280,y = 100)

#Load values for Priority Calculations
Button(parent,text="Load",command=lambda:[store(),prstore(),proc(),prioritySort(),waitTime(),executeOrder(),updateWaitTime(),updateTT()]).place(x = 485,y = 100)#Load values for Priority Calculations

parent.mainloop()