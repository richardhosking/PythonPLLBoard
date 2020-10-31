"""
File to abstract PLL setup code from main GUI

"""
import aDFClass

# Create instances of the ADF4531 and assign ports 
# second parameter is clock trim 
Gen1 = aDFClass.ADF4531("Gen1", 80)

# Set ports acording to wiring of RPi
# Broadcom wiring convention
Gen1.chipEnable = 2 # Physical pin 3
Gen1.loadEnable = 3  # Physical pin 5 
Gen1.dataClock = 4  # Physical pin 7
Gen1.serialData = 14 # Physical pin 8
Gen1.lockDetect = 15 # Physical pin 10 
Gen1.multiplexData = 101  
Gen1.setup_port()
Gen1.initialize_registers()

Gen2 = aDFClass.ADF4531("Gen2",0)

Gen2.chipEnable = 17  # Physical pin 11
Gen2.loadEnable = 27  # Physical pin 13
Gen2.dataClock = 22   # Physical pin 15 
Gen2.serialData = 18  # Physical pin 12
Gen2.lockDetect = 23  # Physical pin 16
Gen2.multiplexData = 201  
Gen2.setup_port()
Gen2.initialize_registers()

Gen3 = aDFClass.ADF4531("Gen3",0)

Gen3.chipEnable = 10  # Physical pin 19 
Gen3.loadEnable = 9   # Physical pin 21 
Gen3.dataClock = 11   # Physical pin 23 
Gen3.serialData = 25  # Physical pin 22 
Gen3.lockDetect = 8   # Physical pin 24 
Gen3.multiplexData = 301  
Gen3.setup_port()
Gen3.initialize_registers()

