import tkinter as tk

win = tk.Tk()

frame = tk.Frame(master= win, width = 500, height = 500)
win.minsize(500,500)
win.maxsize(500,500)
frame.pack()

win.title('Measurement Converter')
win.configure(bg='red')

#Functions
def Inch_Cent():
    #Secondary Window Setup
    win1= tk.Tk()
    win1.title('Inches to Centimeters')

    frame= tk.Frame(master= win1, width= 400, height = 200)
    win1.minsize(400,200)
    win1.maxsize(400,200)
    frame.pack()
    
    unit = ' centimeters'
    #Calculation Function
    def Inch_to_Cent():
        val = entry.get()
        ret =int(val)*2.54
        rNum = round(ret, 2)
        display = tk.Label(win1, text = str(rNum) + unit, font=('Arial', 17))
        display.place(x=120, y=150)
        
    title= tk.Label(win1, text= 'Inches to Centimeters', font=('Arial', 17))
    title.place(x=85, y=0)

    entry= tk.Entry(win1, width=50)
    entry.place(x=50,y=50)
    
    calc= tk.Button(win1, text='Calculate', height= 3, width =20, command= Inch_to_Cent, font=('Arial', 10), 
    bg = 'navy', fg = 'white')
    calc.place(x=120, y= 80)

    win1.mainloop()

def Cent_Inch():
    #Secondary Window Setup
    win2= tk.Tk()
    win2.title('Centimeters to Inches')

    frame= tk.Frame(master= win2, width= 400, height = 200)
    win2.minsize(400,200)
    win2.maxsize(400,200)
    frame.pack()
    
    unit = ' inches'
    #Calculation Function
    def Cent_to_Inch():
        val = entry.get()
        ret =int(val)/2.54
        rNum = round(ret, 2)
        display = tk.Label(win2, text = str(rNum) + unit, font=('Arial', 17))
        display.place(x=120, y=150)
        
    title= tk.Label(win2, text= 'Centimeters to Inches', font=('Arial', 17))
    title.place(x=85, y=0)

    entry= tk.Entry(win2, width=50)
    entry.place(x=50,y=50)
    
    calc= tk.Button(win2, text='Calculate', height= 3, width =20, command= Cent_to_Inch, font=('Arial', 10), 
    bg = 'navy', fg = 'white')
    calc.place(x=120, y= 80)

    win2.mainloop()

def Feet_Meet():
    #Secondary Window Setup
    win3= tk.Tk()
    win3.title('Feet to Meters')

    frame= tk.Frame(master= win3, width= 400, height = 200)
    win3.minsize(400,200)
    win3.maxsize(400,200)
    frame.pack()
    
    unit = ' meters'
    #Calculation Function
    def Feet_to_Meet():
        val = entry.get()
        ret =int(val)/3.281
        rNum = round(ret, 2)
        display = tk.Label(win3, text = str(rNum) + unit, font=('Arial', 17))
        display.place(x=120, y=150)
        
    title= tk.Label(win3, text= 'Feet to Meters', font=('Arial', 17))
    title.place(x=120, y=0)

    entry= tk.Entry(win3, width=50)
    entry.place(x=50,y=50)
    
    calc= tk.Button(win3, text='Calculate', height= 3, width =20, command= Feet_to_Meet, font=('Arial', 10), 
    bg = 'navy', fg = 'white')
    calc.place(x=120, y= 80)

    win3.mainloop()

def Meet_Feet():
    #Secondary Window Setup
    win4= tk.Tk()
    win4.title('Feet to Meters')

    frame= tk.Frame(master= win4, width= 400, height = 200)
    win4.minsize(400,200)
    win4.maxsize(400,200)
    frame.pack()
    
    unit = ' meters'
    #Calculation Function
    def Meet_to_Feet():
        val = entry.get()
        ret =int(val)*3.281
        rNum = round(ret, 2)
        display = tk.Label(win4, text = str(rNum) + unit, font=('Arial', 17))
        display.place(x=120, y=150)
        
    title= tk.Label(win4, text= 'Meters to Feet', font=('Arial', 17))
    title.place(x=120, y=0)

    entry= tk.Entry(win4, width=50)
    entry.place(x=50,y=50)
    
    calc= tk.Button(win4, text='Calculate', height= 3, width =20, command= Meet_to_Feet, font=('Arial', 10), 
    bg = 'navy', fg = 'white')
    calc.place(x=120, y= 80)

    win4.mainloop()
    
#GUI Configuration
title= tk.Label(win, text= 'Measurement Converter', font=('Arial', 20))
title.place(x=100, y =0)

InchCent= tk.Button(win, text='Inches \n to \n Centimeters', height= 10, width =20, command= Inch_Cent, font=('Arial', 10), 
bg = 'navy', fg = 'white')
InchCent.place(x=50, y=50)

CentInch= tk.Button(win, text='Centimeters \n to \n Inches', height= 10, width =20, command= Cent_Inch, font=('Arial', 10), 
bg = 'navy', fg ='white')
CentInch.place(x=300, y=50)

FtM= tk.Button(win, text='Feet \n to \n Meters', height= 10, width =20, command= Feet_Meet, font=('Arial', 10), 
bg = 'navy', fg ='white')
FtM.place(x=50, y=300)

MFt= tk.Button(win, text='Meters \n to \n Feet', height= 10, width =20, command= Meet_Feet, font=('Arial', 10), 
bg = 'navy', fg ='white')
MFt.place(x=300, y=300)

win.mainloop()