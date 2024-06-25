import tkinter
from tkinter import ttk
from tkinter import messagebox
def save_data():
    fname=fnameentry.get()
    lname=lnameentry.get()
    if fname!='' and lname!=' ':
        title=titlecombo.get()
        age=agespinbox.get()
        nationality=nationcombo.get()
        registrated=reg_status.get()
    #for show in the data if person is registreted or no
        if registrated=='1':
            registered='Registered'
        else:
            registered= 'Not registered'


        print('First Name:',fname,'\tLAst NAme:',lname)
        print('Title:',title,'\tAge',age,'\tNationality:',nationality)
        print(registrated)
        with open('student.txt','a') as fwrite:
            fwrite.write(fname+' '+title+' '+str(age)+' '+nationality+'\n'+' '+registered+'\n')
        print('saved')
    else:
        tkinter.messagebox.showwarning(title='Error: Missing data',message='First name and last name required to save data')

window=tkinter.Tk()
window.title('Data entry form')

frame=tkinter.Frame(window)
frame.pack()

userinfoframe=tkinter.LabelFrame(frame,text='User Information')
userinfoframe.grid(row=0,column=0)
framelabel=tkinter.Label(userinfoframe,text='First Name')
framelabel.grid(row=0,column=0)

fnameentry=tkinter.Entry(userinfoframe)
fnameentry.grid(row=0,column=1)

lnamelabel=tkinter.Label(userinfoframe,text='Last Name')
lnamelabel.grid(row=0,column=2)


lnameentry=tkinter.Entry(userinfoframe)
lnameentry.grid(row=0,column=3)
#import ttk to do many choices
titlelabel=tkinter.Label(userinfoframe,text='Tile')
titlecombo=ttk.Combobox(userinfoframe,values=["","Mr","Mrs","Ms","Dr"])
titlelabel.grid(row=1,column=0)
titlecombo.grid(row=1,column=1)

agelabel=tkinter.Label(userinfoframe,text='Age')
agespinbox=tkinter.Spinbox(userinfoframe,from_=18,to=50)
agelabel.grid(row=1,column=2)
agespinbox.grid(row=1,column=3)

countries=['Venezuela','Peru','Mexico','Panama','Chile']
nationlabel=tkinter.Label(userinfoframe,text='Nationality')
nationcombo=ttk.Combobox(userinfoframe,values=countries)
nationlabel.grid(row=2,column=0)
nationcombo.grid(row=2,column=1)

courseframe=tkinter.LabelFrame(frame,text='Registracion')
courseframe.grid(row=1,column=0)

registeredlabel=tkinter.Label(courseframe,text='Registreted')
reg_status=tkinter.StringVar()# add after def for store the data
regcheck=tkinter.Checkbutton(courseframe,text='Currently Registered',variable=reg_status)

registeredlabel.grid(row=0,column=0)
regcheck.grid(row=0,column=0)

savebtn=tkinter.Button(frame,text='Save',command=save_data)
savebtn.grid(row=2,column=0)

graphbtn=tkinter









window.mainloop()

