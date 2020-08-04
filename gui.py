# This file has code for Signal Generator interface 
# Three separate signal generator modules 
# Frequency and amplitude data can be entered via
# a touchscreen interface 

from Tkinter import * 

# Definitions and code for ADF4531  

import aDFClass

# Main window 
mainwindow = Tk()
mainwindow.title("RF Signal Generator")
#mainwindow.geometry('650x300')
w, h = mainwindow.winfo_screenwidth(), mainwindow.winfo_screenheight()
mainwindow.geometry("%dx%d+0+0" % (w, h))

#Frames
# Frequency control frame to enclose freq widgets
freq = Frame(mainwindow,  borderwidth = 10)
freq.grid(column = 0,   row = 0,  sticky=(N,S))
#freq.pack()
# Frame to enclose level widgets
levels = Frame(mainwindow, borderwidth = 10)
levels.grid(column = 1,  row = 0,  sticky=(N,S))
#levels.pack()

# Keys to enter data 
# Inside a frame called keypad
keypad = Frame(mainwindow,  borderwidth = 10, height=h-10, width=w-200)
keypad.grid(column = 2,  row = 0, sticky=N)
#keypad.pack(expand=YES, fill=BOTH)
#keypad.geometry('650x300')

# Create instances of the ADF4531 and assign ports 
Gen1 = aDFClass.ADF4531("Gen1")

# Set ports acording to wiring of RPi
# Broadcom wiring convention
Gen1.chipEnable = 2 # Physical pin 3
Gen1.loadEnable = 3  # Physical pin 5 
Gen1.dataClock = 4  # Physical pin 7
Gen1.serialData = 14 # Physical pin 8
Gen1.lockDetect = 100 
Gen1.multiplexData = 101  
Gen1.setup_port()
Gen1.initialize_registers()

Gen2 = aDFClass.ADF4531("Gen2")

Gen2.chipEnable = 17  # Physical pin 11
Gen2.loadEnable = 27  # Physical pin 13
Gen2.dataClock = 22   # Physical pin 15 
Gen2.serialData = 18  # Physical pin 12
Gen2.lockDetect = 200 
Gen2.multiplexData = 201  
Gen2.setup_port()
Gen2.initialize_registers()

Gen3 = aDFClass.ADF4531("Gen3")

Gen3.chipEnable = 10  # Physical pin 19 
Gen3.loadEnable = 9   # Physical pin 21 
Gen3.dataClock = 11   # Physical pin 23 
Gen3.serialData = 25  # Physical pin 22 
Gen3.lockDetect = 300 
Gen3.multiplexData = 301  
Gen3.setup_port()
Gen3.initialize_registers()

# Handlers - need to be declared before widget is defined
def clickedMute1():
    Gen1message =  StringVar()

     # Cycle power setting between -9dBm, -6dBm, -3dBm, 0dBm and MUTE
    if Gen1.mainPower == '11':
        Gen1.mainRFEnabled = '0'
        Gen1.mainPower ='00'
        Gen1message ='MUTED'  # signal at approx -80dBm
    elif Gen1.mainRFEnabled == '0':
        Gen1.mainRFEnabled ='1'
        Gen1.mainPower ='00'
        Gen1message = '-9dBm '
    elif Gen1.mainPower =='00':
        Gen1.mainPower ='01'
        Gen1message = '-6dBm '
    elif Gen1.mainPower == '01':
        Gen1.mainPower ='10'
        Gen1message = '-3dBm '
    elif Gen1.mainPower =='10':
        Gen1.mainPower ='11'
        Gen1message = '0dBm '
        
    levlbl1 = Label(levels, text=Gen1message)
    levlbl1.grid(column=1, row=2,  padx=5)
    Gen1.updatePower()

def clickedMute2():
    Gen2message =  StringVar()
        # Cycle power setting between -4dBm, -1dBm, +2dBm, +5dBm and MUTE
    if Gen2.mainPower == '11':
        Gen2.mainRFEnabled = '0'
        Gen2.mainPower ='00'
        Gen2message ='MUTED'  # signal at approx -80dBm
    elif Gen2.mainRFEnabled == '0':
        Gen2.mainRFEnabled ='1'
        Gen2.mainPower ='00'
        Gen2message = '-9dBm '
    elif Gen2.mainPower =='00':
        Gen2.mainPower ='01'
        Gen2message = '-6dBm '
    elif Gen2.mainPower =='01':
        Gen2.mainPower ='10'
        Gen2message = '-3dBm '
    elif Gen2.mainPower =='10':
        Gen2.mainPower ='11'
        Gen2message = ' 0dBm '

    Gen2.updatePower()
    levlbl2 = Label(levels, text=Gen2message)
    levlbl2.grid(column=1, row=5,  padx=5)

def clickedMute3():
    Gen3message =  StringVar()    
         # Cycle power setting between -4dBm, -1dBm, +2dBm, +5dBm and MUTE
         # In practice at output levels are -9, -6, -3 and 0dBm 
    if Gen3.mainPower == '11':
        Gen3.mainRFEnabled = '0'
        Gen3.mainPower ='00'
        Gen3message ='MUTED'
    elif Gen3.mainRFEnabled == '0':
        Gen3.mainRFEnabled ='1'
        Gen3.mainPower ='00'
        Gen3message = '-9dBm '
    elif Gen3.mainPower =='00':
        Gen3.mainPower ='01'
        Gen3message = '-6dBm '
    elif Gen3.mainPower =='01': 
        Gen3.mainPower ='10'
        Gen3message = '-3dBm '
    elif Gen3.mainPower =='10':
        Gen3.mainPower ='11'
        Gen3message = '0dBm '

    Gen3.updatePower()
    levlbl3 = Label(levels, text=Gen3message)
    levlbl3.grid(column=1, row=8,  padx=5)

def clickedUpdate():
    # these varaiables need to be a StringVar to be used in widget
    error = StringVar()
    errorText = StringVar()
    
    # If there is data entered 
    if mainwindow.focus_get().get():
        freqEntered =int(mainwindow.focus_get().get())

   
        if freqEntered > 4400000:  # exceeds max VCO freq
           # Bottom row message
           error.set('Error!')
           errorText.set('  Freq > max  ')
         
           # and clear data
           mainwindow.focus_get().delete(0, END)
    
        elif freqEntered < 34375:  # Min freq of module 34.275 MHz 
           error.set('Error!')
           errorText.set('  Freq < min  ')
          # Error/Message labels       
          
           mainwindow.focus_get().delete(0, END)
                  
        else:
           error.set('          ')
           errorText.set('Gen updated')
           # Error/Message labels
           
           if mainwindow.focus_get() == freqGen1:
              Gen1.calculate_freq(freqEntered)
              Gen1.update()
           elif mainwindow.focus_get() == freqGen2:
              Gen2.calculate_freq(freqEntered)
              Gen2.update()
           elif mainwindow.focus_get() == freqGen3:
              Gen3.calculate_freq(freqEntered)
              Gen3.update()
       
    else:
        # if no data erase previous error message and return 
       error = '          '
       errorText = '          '

    lbl1 = Label(keypad, textvariable=error)
    lbl1.grid(column=0, row=5)
    lbl2 = Label(keypad, textvariable=errorText)
    lbl2.grid(column=1, row=5,  columnspan=2)
    
#Insert digit at end of variable in window in focus   
def keypad1():
    mainwindow.focus_get().insert(END,"1") 
def keypad2():
    mainwindow.focus_get().insert(END,"2") 
def keypad3():
    mainwindow.focus_get().insert(END, "3") 
def keypad4():
    mainwindow.focus_get().insert(END, "4") 
def keypad5():
    mainwindow.focus_get().insert(END, "5") 
def keypad6():
    mainwindow.focus_get().insert(END, "6") 
def keypad7():
    mainwindow.focus_get().insert(END, "7") 
def keypad8():
    mainwindow.focus_get().insert(END, "8") 
def keypad9():
    mainwindow.focus_get().insert(END, "9") 
def keypad0():
    mainwindow.focus_get().insert(END, "0") 
# Clear data 
def keypadclear():
    mainwindow.focus_get().delete(0, END)
def keypadback():
    # Go back one character 
    data = mainwindow.focus_get().get()
    index = len(data)-1
    mainwindow.focus_get().delete(index) 

#FREQ FRAME
#Widgets frequency frame
lbl = Label(freq, text="Frequency")
lbl.grid(column=0, row=1)

lbl = Label(freq, text="Generator 1")
lbl.grid(column=0,   row=2)

freqGen1text= StringVar()
freqGen1 = Entry(freq,width=10,  textvariable=freqGen1text)
freqGen1.grid(column=0,  row=3,  pady=3)

lbl = Label(freq, text="KHz")
lbl.grid(column=1,  row=3)

# Spacer
lbl = Label(freq)
lbl.grid(column=0, row=4)

lbl = Label(freq, text="Generator 2")
lbl.grid(column=0,   row=5)

freqGen2text= StringVar()
freqGen2 = Entry(freq,width=10,  textvariable=freqGen2text)
freqGen2.grid(column=0, row=6,  pady=3)

lbl = Label(freq, text="KHz")
lbl.grid(column=1, row=6)

# Spacer
lbl = Label(freq)
lbl.grid(column=0, row=7)

lbl = Label(freq, text="Generator 3")
lbl.grid(column=0,  row=8)

freqGen3text= StringVar()
freqGen3 = Entry(freq,width=10,  textvariable=freqGen3text)
freqGen3.grid(column=0, row=9,  pady=3)

lbl = Label(freq, text="KHz")
lbl.grid(column=1, row=9)

#LEVEL FRAME
# Level widgets
lbl = Label(levels, text="Level")
lbl.grid(column=0, row=0)

# Spacer
lbl = Label(levels)
lbl.grid(column=0, row=1)

mute1 = Button(levels, text="Power/Mute", command=clickedMute1)
mute1.grid(column=0, row=2)
levlbl1 = Label(levels, text='MUTED')
levlbl1.grid(column=1, row=2,  padx=5)

# Spacer
lbl = Label(levels)
lbl.grid(column=0, row=3)
lbl = Label(levels)
lbl.grid(column=0, row=4)

mute2 = Button(levels, text="Power/Mute", command=clickedMute2)
mute2.grid(column=0, row=5)
levlbl2 = Label(levels, text='MUTED')
levlbl2.grid(column=1, row=2,  padx=5)

# Spacer
lbl = Label(levels)
lbl.grid(column=0, row=6)
lbl = Label(levels)
lbl.grid(column=0, row=7)

mute3 = Button(levels, text="Power/Mute", command=clickedMute3)
mute3.grid(column=0, row=8)
levlbl3 = Label(levels, text='MUTED')
levlbl3.grid(column=1, row=2,  padx=5)

#KEYPAD
# Keypad widgets
btn = Button(keypad, text=" 1 ",   command=keypad1, height = 3, width = 3)
btn.grid(column=0, row=0)

btn = Button(keypad, text=" 2 ",   command=keypad2, height = 3, width = 3)
btn.grid(column=1, row=0)

btn = Button(keypad, text=" 3 ",   command=keypad3, height = 3, width = 3)
btn.grid(column=2, row=0)

btn = Button(keypad, text=" 4 ",   command=keypad4, height = 3, width = 3)
btn.grid(column=0, row=1)

btn = Button(keypad, text=" 5 ",   command=keypad5, height = 3, width = 3)
btn.grid(column=1, row=1)

btn = Button(keypad, text=" 6 ",   command=keypad6, height = 3, width = 3)
btn.grid(column=2, row=1)

btn = Button(keypad, text=" 7 ",   command=keypad7, height = 3, width = 3)
btn.grid(column=0, row=2)

btn = Button(keypad, text=" 8 ",   command=keypad8, height = 3, width = 3)
btn.grid(column=1, row=2)

btn = Button(keypad, text=" 9 ",   command=keypad9, height = 3, width = 3)
btn.grid(column=2, row=2)

btn = Button(keypad, text=" C ",   command=keypadclear, height = 3, width = 3)
btn.grid(column=0, row=3)

btn = Button(keypad, text=" 0 ",   command=keypad0, height = 3, width = 3)
btn.grid(column=1, row=3)

btn = Button(keypad, text=" < ",   command=keypadback, height = 3, width = 3)
btn.grid(column=2, row=3)

# Update generator which has current focus 
btn = Button(keypad, text="Update Generator", command=clickedUpdate, height = 3)
btn.grid(column=0, row=4, columnspan = 3)




