import tkinter as tk

win = tk.Tk()

frame = tk.Frame(master= win, width = 500, height = 500)
frame.pack()

win.title('Measurement Converter')
win.configure(bg='red')

#Functions
def Inch_Cent():
    win1= tk.Tk()
    win1.title('Inches to Centimeters')

    frame1= tk.Frame(master= win1, width= 200, height = 200)
    frame1.pack()

    win1.mainloop()

def Cent_Inch():
    print('Coangular Interpet')

def Feet_Meet():
    print('FM Radio')

def Meet_Feet():
    print('Mo Bamba')
    
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