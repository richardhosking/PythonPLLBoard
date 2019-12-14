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
mainwindow.geometry('800x450')
# fonts for all widgets
mainwindow.option_add("*Font", "helvetica 12 bold")

# make all widgets light blue
mainwindow.option_add("*Background", "light blue")


# Create instances of the ADF4531 and assign ports 
Gen1 = aDFClass.ADF4531("Gen1")

# Set ports acording to wiring of RPi
# Broadcom witring convention
Gen1.chipEnable = 17 # Physical pin 11
Gen1.loadEnable = 18  # Physical pin 12 
Gen1.dataClock = 27  # Physical pin 13
Gen1.serialData = 22 # Physical pin 15
Gen1.lockDetect = 0 
Gen1.multiplexData = 0  
Gen1.setup_port()
Gen1.initialize_registers()

Gen2 = aDFClass.ADF4531("Gen2")

Gen2.chipEnable = 0 
Gen2.loadEnable = 0 
Gen2.dataClock = 0 
Gen2.serialData = 0 
Gen2.lockDetect = 0 
Gen2.multiplexData = 0  
Gen2.setup_port()


Gen3 = aDFClass.ADF4531("Gen3")

Gen3.chipEnable = 0 
Gen3.loadEnable = 0 
Gen3.dataClock = 0 
Gen3.serialData = 0 
Gen3.lockDetect = 0 
Gen3.multiplexData = 0  
Gen3.setup_port()


# Handlers - need to be declared before widget is defined
def clickedMute1():
     # Cycle power setting between -4dBm, -1dBm, +2dBm, +5dBm and MUTE
    if Gen1.mainPower == '11':
        Gen1.mainRFEnabled = '0'
        Gen1.mainPower ='00'
        Gen1message ='MUTED'  # signal at approx -80dBm
    elif  Gen1.mainRFEnabled == '0':
        Gen1.mainRFEnabled ='1'
        Gen1.mainPower ='00'
        Gen1message = '    -9    '
    elif  Gen1.mainPower =='00':
        Gen1.mainPower ='01'
        Gen1message = '   -6     '
    elif  Gen1.mainPower =='01':
        Gen1.mainPower ='10'
        Gen1message = '   -3     '
    elif  Gen1.mainPower =='10':
        Gen1.mainPower ='11'
        Gen1message = '    0     '

    Gen1.update()
    lbl = Label(mainwindow, text=Gen1message) 
    lbl.grid(column=2, row=3)

def clickedMute2():
        # Cycle power setting between -4dBm, -1dBm, +2dBm, +5dBm and MUTE
    if Gen2.mainPower == '11':
        Gen2.mainRFEnabled = '0'
        Gen2.mainPower ='00'
        Gen2message ='MUTED'  # signal at approx -80dBm
    elif  Gen2.mainRFEnabled == '0':
        Gen2.mainRFEnabled ='1'
        Gen2.mainPower ='00'
        Gen2message = '   -9     '
    elif  Gen2.mainPower =='00':
        Gen2.mainPower ='01'
        Gen2message = '   -6     '
    elif  Gen2.mainPower =='01':
        Gen2.mainPower ='10'
        Gen2message = '   -3     '
    elif  Gen2.mainPower =='10':
        Gen2.mainPower ='11'
        Gen2message = '   0      '

    Gen2.update()
    lbl = Label(LHButtons, text=Gen2message) 
    lbl.grid(column=4, row=3)

def clickedMute3():
         # Cycle power setting between -4dBm, -1dBm, +2dBm, +5dBm and MUTE
         # In practice at output levels are -9, -6, -3 and 0dBm 
    if Gen3.mainPower == '11':
        Gen3.mainRFEnabled = '0'
        Gen3.mainPower ='00'
        Gen3message ='MUTED'
    elif  Gen3.mainRFEnabled == '0':
        Gen3.mainRFEnabled ='1'
        Gen3.mainPower ='00'
        Gen3message = '   -9     '
    elif  Gen3.mainPower =='00':
        Gen3.mainPower ='01'
        Gen3message = '   -6    '
    elif  Gen3.mainPower =='01':
        Gen3.mainPower ='10'
        Gen3message = '   -3    '
    elif  Gen3.mainPower =='10':
        Gen3.mainPower ='11'
        Gen3message = '   0      '

    Gen3.update()
    lbl = Label(LHButtons, text=Gen3message) 
    lbl.grid(column=6, row=3)

def clickedUpdate():
    # these varaiables need to be a StringVar to be used in widget
    error = StringVar()
    errorText = StringVar()
    
    # If there is data entered 
    if mainwindow.focus_get().get():
        freqEntered =int(mainwindow.focus_get().get())
    else:
        # if no data erase previous error message and return 
       error = '          '
       errorText = '          '
       lbl1 = Label(LHButtons, textvariable=error)
       lbl1.grid(column=0, row=10)
       lbl2 = Label(LHButtons, textvariable=errorText)
       lbl2.grid(column=2, row=10)
       return
    
    if freqEntered > 4400000:  # exceeds max VCO freq
       # Bottom row message
       error.set('Error!')
       errorText.set('  Freq > max  ')
             # Error/Message labels
       lbl1 = Label(LHButtons, textvariable=error)
       lbl1.grid(column=0, row=10)
       lbl2 = Label(LHButtons, textvariable=errorText)
       lbl2.grid(column=2, row=10)
       
       # and clear data
       mainwindow.focus_get().delete(0, END)
       return
       
    elif freqEntered < 34275:  # Min freq of module 34.275 MHz 
       error.set('Error!')
       errorText.set('  Freq < min  ')
      # Error/Message labels       
       lbl1 = Label(LHButtons, textvariable=error)
       lbl1.grid(column=0, row=10)
       lbl2 = Label(LHButtons, textvariable=errorText)
       lbl2.grid(column=2, row=10)
       
       mainwindow.focus_get().delete(0, END)
       return
       
    else:
       error.set('          ')
       errorText.set('Gen updated')
       # Error/Message labels
       lbl1 = Label(LHButtons, textvariable=error)
       lbl1.grid(column=0, row=10)
       lbl2 = Label(LHButtons, textvariable=errorText)
       lbl2.grid(column=2, row=10)
       
    if mainwindow.focus_get() == freqGen1:
       Gen1.calculate_freq(freqEntered)
       Gen1.update()
    elif mainwindow.focus_get() == freqGen2:
       Gen2.calculate_freq(freqEntered)
       Gen2.update()
    elif mainwindow.focus_get() == freqGen3:
       Gen3.calculate_freq(freqEntered)
       Gen3.update()
    
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

#Widgets 
# frame for data entry except Keypad
LHButtons = Frame(mainwindow,  borderwidth = 3, height = 450)
LHButtons.grid(column=0, row=0)

# labels Generator 1
lbl = Label(LHButtons, text="Generator 1")
lbl.grid(column=2, row=0)

lbl = Label(LHButtons, text="Frequency")
lbl.grid(column=0, row=1)

freqGen1text= StringVar()
freqGen1 = Entry(LHButtons,width=10,  textvariable=freqGen1text)
freqGen1.grid(column=2, row=1)

lbl = Label(LHButtons, text="KHz")
lbl.grid(column=3, row=1)

lbl = Label(LHButtons, text="Level")
lbl.grid(column=0, row=2)

lbl = Label(LHButtons, text="MUTED")
lbl.grid(column=2, row=2)

lbl = Label(LHButtons, text="dBm")

mute1 = Button(LHButtons, text="Power/Mute", command=clickedMute1)
mute1.grid(column=2, row=3)
lbl.grid(column=3, row=2)

# Generator 2 
lbl = Label(LHButtons, text="Generator 2")
lbl.grid(column=2, row=6)

freqGen2 = Entry(LHButtons,width=10)
freqGen2.grid(column=2, row=7)

lbl = Label(LHButtons, text="KHz")
lbl.grid(column=3, row=7)

lbl = Label(LHButtons, text="MUTED")
lbl.grid(column=2, row=8)

lbl = Label(LHButtons, text="dBm")
lbl.grid(column=3, row=8)

mute2 = Button(LHButtons, text="Power/Mute", command=clickedMute2)
mute2.grid(column=2, row=9)

# Generator 3 
lbl = Label(LHButtons, text="Generator 3")
lbl.grid(column=2, row=11)

freqGen3 = Entry(LHButtons,width=10)
freqGen3.grid(column=2, row=12)

lbl = Label(LHButtons, text="KHz")
lbl.grid(column=3, row=12)

lbl = Label(LHButtons, text="MUTED")
lbl.grid(column=2, row=13)

lbl = Label(LHButtons, text="dBm")
lbl.grid(column=3, row=13) 

mute3 = Button(LHButtons, text="Power/Mute", command=clickedMute3)
mute3.grid(column=2, row=14)


# Keys to enter data 
# Inside a frame called keypad
keypad = Frame(mainwindow,  borderwidth = 10)
keypad.grid(column = 1,  row = 0)

btn = Button(keypad, text=" 1 ",   command=keypad1, height =4, width =6 )
btn.grid(column=0, row=0)

btn = Button(keypad, text=" 2 ",   command=keypad2, height =4, width =6 )
btn.grid(column=1, row=0)

btn = Button(keypad, text=" 3 ",   command=keypad3, height =4, width =6 )
btn.grid(column=2, row=0)

btn = Button(keypad, text=" 4 ",   command=keypad4, height =4, width =6 )
btn.grid(column=0, row=1)

btn = Button(keypad, text=" 5 ",   command=keypad5, height =4, width =6 )
btn.grid(column=1, row=1)

btn = Button(keypad, text=" 6 ",   command=keypad6, height =4, width =6 )
btn.grid(column=2, row=1)

btn = Button(keypad, text=" 7 ",   command=keypad7, height =4, width =6 )
btn.grid(column=0, row=2)

btn = Button(keypad, text=" 8 ",   command=keypad8, height =4, width =6 )
btn.grid(column=1, row=2)

btn = Button(keypad, text=" 9 ",   command=keypad9, height =4, width =6 )
btn.grid(column=2, row=2)

btn = Button(keypad, text=" C ",   command=keypadclear, height =4, width =6)
btn.grid(column=0, row=3)

btn = Button(keypad, text=" 0 ",   command=keypad0, height =4, width =6 )
btn.grid(column=1, row=3)

btn = Button(keypad, text=" < ",   command=keypadback, height =4, width =6 )
btn.grid(column=2, row=3)

# Update generator which has current focus 
btn = Button(mainwindow, text="Update Generator", command=clickedUpdate)
btn.grid(column=0, row=1)




