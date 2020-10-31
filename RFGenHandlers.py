"""
RF generator handler routines
Into a separate file for clarity
imported into Ui_MainWindow class 

"""
# Definitions and code for ADF4531 including port setup 
# Uncomment this import when using Raspberry Pi 
# TODO Stub for RPi library - cant seem to get a solution for an ordinary PC
import aDFSetup as PLL

# Event handlers "slots"

# Enter keypad press into relevant line edit indicated by currentData class variable
def keypadEnter(self, char):    
    if self.currentData.text() == '0':
        self.currentData.setText(char)
    else:
        text = self.currentData.text()
        self.currentData.setText(text + char)
        
# Clear data in current line edit     
def keypadClear(self):    
    self.currentData.clear()

# Go back one character in current line edit         
def keypadBack(self):    
    self.currentData.backspace()
    
# When keypad Update key pressed
def keypadUpdate(self):
    if self.currentData in [self.gen1Frequency, self.gen2Frequency, self.gen3Frequency]:
        validateSingleFreq(self)
    
    # tab between entries in sweep page 
    elif self.currentData == self.sweepStart:
        self.currentData = self.sweepStop
    elif self.currentData == self.sweepStop:
        self.currentData = self.sweepStep            
    elif self.currentData == self.sweepStep:
        self.currentData = self.sweepStart           
    
# Assign the Line Edit with current focus to currentData    
def setFocus(self):    
    if self.GeneratorTabs.currentIndex() == 0:
        self.currentData = self.gen1Frequency
    elif self.GeneratorTabs.currentIndex() == 1:
        self.currentData = self.gen2Frequency  
    elif self.GeneratorTabs.currentIndex() == 2:
        self.currentData = self.gen3Frequency
    elif self.GeneratorTabs.currentIndex() == 3:
        self.currentData = self.sweepStart        
        
        
# Validate single Frequency and send data to relevant PLL     
   
def validateSingleFreq(self):
    error = ''
    data = int(self.currentData.text())
             
    if data > 4400000:
        error = 'Freq > max'
        # Max VCO Freq 4.4GHz
        self.currentData.setText('0')
    elif data < 34375:
        error = 'Freq < min'
        # Min PLL Output is 34.375 MHz
        self.currentData.setText('0')         
    else:
        error = 'Gen updated'
        # Update PLL
        if self.GeneratorTabs.currentIndex() == 0:
            PLL.Gen1.calculate_freq(data)
            PLL.Gen1.update()
        if self.GeneratorTabs.currentIndex() == 1:
            PLL.Gen2.calculate_freq(data)
            PLL.Gen2.update()
        if self.GeneratorTabs.currentIndex() == 2:
            PLL.Gen3.calculate_freq(data)
            PLL.Gen3.update()    
    self.errorMessage = error
    self.infoLabel.setText(error)



# Slot to handle start/stop sweep button            
def manageSweep(self):
    # if thread is already running  and sweep start/stop button pressed
    if self.sweepThread.isRunning():
        # Set sweepThread.exiting flag so thread can exit gracefully
        # Thread will check for flag at the end of each sweep
        self.sweepThread.exiting = True
        self.startStopSweep.setText('Start')
        self.infoLabel.setText("Sweep Stopped")
    else:
        validateSweep(self)
    
def validateSweep(self):
  
    start = int(self.sweepStart.text()) 
    stop = int(self.sweepStop.text())
    step = int(self.sweepStep.text())    
    error = 'Sweep started'

    for data in [start,stop]:
        if data == '':
            error = 'No entry'
            self.errorMessage = error
            self.sweepStart.setText('0')
            self.sweepStop.setText('0')
            self.sweepStep.setText('0') 
        elif data > 4400000:
            error = ' Freq > max'
            self.errorMessage = error
            self.sweepStart.setText('0')
            self.sweepStop.setText('0')
            self.sweepStop.setText('0') 
        elif data < 34375:
            error = 'Freq < min'
            self.errorMessage = error
            self.sweepStart.setText('0')
            self.sweepStop.setText('0')
            self.sweepStop.setText('0') 
    
    if start > stop:
        error  = 'Start must be < stop'
        self.errorMessage = error
        self.sweepStart.setText('0')
        self.sweepStop.setText('0')         
    elif step > 10000:
        error = 'Step must be < 10 MHz'
        self.errorMessage = error
        self.sweepStep.setText('0')                 
    else:
        error = 'Sweep started'  
        self.sweepThread.sweep(start,stop,step)
        self.startStopSweep.setText('Stop')
        self.sweepThread.exiting = False             
    self.infoLabel.setText(error)

# Handler to update output power    
def updatePLLPower(self):
    enableRF = '0'
    
    if self.GeneratorTabs.currentIndex() == 0:
        name = self.gen1PowerLabel.text()
    elif self.GeneratorTabs.currentIndex() == 1:
        name = self.gen2PowerLabel.text()
    elif self.GeneratorTabs.currentIndex() == 2:
        name = self.gen3PowerLabel.text()
    elif self.GeneratorTabs.currentIndex() == 3:
        name = self.sweepPowerLabel.text()
        
    if name == 'MUTED':
        name ='-9dBm'
        power = '00'
        enableRF = '1'
    elif name == '-9dBm':
        name ='-6dBm'
        power = '01'
        enableRF = '1'
    elif name == '-6dBm':
        name ='-3dBm'
        power = '10'
        enableRF = '1'
    elif name == '-3dBm':
        name ='0dBm'
        power = '11' 
        enableRF = '1'               
    elif name == '0dBm':
        name ='MUTED'
        power = '00'
        enableRF = '0'
        
    if self.GeneratorTabs.currentIndex() == 0:
        self.gen1PowerLabel.setText(name)
        PLL.Gen1.mainPower = power
        PLL.Gen1.mainRFEnabled = enableRF
        PLL.Gen1.updatePower()
    elif self.GeneratorTabs.currentIndex() == 1:
        self.gen2PowerLabel.setText(name)
        PLL.Gen2.mainPower = power
        PLL.Gen2.mainRFEnabled = enableRF
        PLL.Gen2.updatePower()
    elif self.GeneratorTabs.currentIndex() == 2:
        self.gen3PowerLabel.setText(name)
        PLL.Gen3.mainPower = power
        PLL.Gen3.mainRFEnabled = enableRF
        PLL.Gen3.updatePower()
    elif self.GeneratorTabs.currentIndex() == 3:
        self.sweepPowerLabel.setText(name)        
        PLL.Gen1.mainPower = power
        PLL.Gen1.mainRFEnabled = enableRF
        PLL.Gen1.updatePower()
