
import tkinter
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

def person_data():
    global data
    name=fnameentry.get()
    age=ageentry.get()
    weight=weightspinbox.get()
    height=heightspinbox.get()
    BMI=float(weight)/(float(height)**2)
    if BMI>=25:
        data='overweight'
        messagebox.showwarning('BMI','Take care! you are overweight')
    elif BMI<25:
        data ='normal'
        messagebox.showwarning('BMI', 'you BMI is Normal')
    elif BMI>=30:
        data='obese'
        messagebox.showwarning('BMI','Attention! you are obese')
    else:
        data='underweight'
        messagebox.showwarning('BMI','Attention! you are underweight')
data=''

BMIfile = 'BMIdata.txt'
def get_data():
    global data
    with open(BMIfile,'a') as f:
        f.write(data+'\n')
def show_data():
    with open(BMIfile,'r') as fread:
        read=fread.read()
        messagebox.showwarning(read)
def plot_data():
    categories = {'underweight': 0, 'normal': 0, 'overweight': 0, 'obese': 0}

    try:
        with open(BMIfile, 'r') as fread:
            for line in fread:
                category = line.strip().split(',')[-1]
                if category in categories:
                    categories[category] += 1

        labels = categories.keys()
        sizes = categories.values()

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('BMI Categories Distribution')
        plt.show()
    except FileNotFoundError:
        messagebox.showerror('File Error', 'BMI data file not found')


window=tkinter.Tk()
window.title('BMI calculator')
frame=tkinter.Frame(window)
frame.pack()


userinfoframe=tkinter.LabelFrame(frame,text='User Information')
userinfoframe.grid(row=0,column=0)
framelabel=tkinter.Label(userinfoframe,text='Name')
framelabel.grid(row=0,column=0)

fnameentry=tkinter.Entry(userinfoframe)
fnameentry.grid(row=0,column=1)

agelabel=tkinter.Label(userinfoframe,text='Age')
agelabel.grid(row=0,column=2)

ageentry=tkinter.Entry(userinfoframe)
ageentry.grid(row=0,column=3)

heightlabel=tkinter.Label(userinfoframe,text='Height(m)')
heightspinbox=tkinter.Spinbox(userinfoframe,from_=150,to=195)
heightlabel.grid(row=1,column=0)
heightspinbox.grid(row=1,column=1)


weightlabel=tkinter.Label(userinfoframe,text='Weight(Kg)')
weightspinbox=tkinter.Spinbox(userinfoframe,from_=45,to=100)
weightlabel.grid(row=1,column=2)
weightspinbox.grid(row=1,column=3)

calcubtn=tkinter.Button(frame,text='BMI Calculation',command=person_data)
calcubtn.grid(row=2,column=0)

savebtn=tkinter.Button(frame,text='Save',command=get_data)
savebtn.grid(row=3,column=0)

label_result=tkinter.Label(frame,text="BMI:\ndata:")
label_result.grid(row=3,column=2)

graphbtn=tkinter.Button(frame,text='Graph',command=plot_data)
graphbtn.grid(row=3,column=7)














window.mainloop()





