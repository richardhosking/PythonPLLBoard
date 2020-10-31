"""
Thread Class Definition 
Need to run sweep update in thread so main GUI is still functional

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import aDFSetup as PLL


class Worker(QThread):
    # Thread constructor    
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False
 
        
    # Set up arguments to be passed to thread
    # Qt will call run() when Thread environment is set up 
    # start() will invoke the process    
    def sweep(self, begin, stop, step): 
        self.begin = begin
        self.stop = stop
        self.step = step
        self.start()
        
    def run(self):        
        # Note: This is never called directly. It is called by Qt 
        # variable for current freq 
        freq = self.begin
        stop = self.stop
        step = self.step
        self.exiting = False

        # continue sweeping until thread is terminated by GUI
        while not self.exiting:
            while freq < stop:
                PLL.Gen1.calculate_freq(freq)
                PLL.Gen1.update()
                freq = freq + step
                time.sleep(0.001)
 
            freq = self.begin

            # To end the loop/thread cleanly check flag thread.exiting
            # This flag is set by the sweep start/stop button
            if self.exiting == True:
                print ('Exiting thread')
                self.quit()
                      
        # In theory we will never get here  - has to be terminated by start/stop sweep button 
        self.quit()    

 
