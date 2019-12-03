import RPi.GPIO as io # using RPi.GPIO
io.setmode(io.BCM)  # Broadcom pin assignment     

class ADFReg:
    """ Creates a 32 bit number to write to ADF4531 Register containing various parameters
    
    Arbitrary number of parameters , each of arbitrary length 
    Attributes:
    name
    Nested list of parameters
    register 
    Effectively private as it is only called by ADF4531 class 
    """ 
  
# Create class instance 
    def __init__(self, reg_name):
# Instance attributes
# creates a new 32 bit binary string containing the data passed to each instance
         self.register = '0b0'   
         self.name = reg_name # each instance has a name
 
# Class methods 

# Create a 32 bit register with binary data 
# Data is list of register definitions of arbitrary length
# in the format [variable_name, variable length(bits), variable data(binary string)]
# MSBit first
# Pack binary data into register using join()

    def add_data(self, data):
         binary_data = '0b0'
         i=0
         for d in data:
             if i==0:
                binary_data = str(data[i][2])
             else:
                 join_data = (binary_data, str(data[i][2]))
                 binary_data = ''.join(join_data) 
             i+=1
         
         self.register = binary_data    

# end of class ADFReg definition



class ADF4531: 
    """ Class containing variables and functions to drive the ADF4531 Fractional N PLL synthesizer chip 
        
    """ 
    
       # Create instance with instance variables and default values  
    def __init__(self, PLL_name): 
        self.output_freq = 0 		# main output frquency KHz 
        self.reference_clock = 25000 	# Reference clock  in KHz 25 MHz in these modules 
        self.integer = 0    		# integer part of PLL main divider 16 bits
        self.phase = 0		        # Output phase can be shifted 12 bits - disabled for this application 
        self.rf_divider = '000' 	# Output divider 1(000) to 64 (110)  		 
        self.auxPower = '00'		# Output power 00 = -4dBm, 01 = -1dBm, 10 = +2dBm 11 = +5dBm  
        self.mainPower = '00' 
        self.modulus = 1000		# Modulus of fractional N divider Int steps 1MHz hence this will give 1KHz steps  
        self.fraction = 0		# fraction of fractional N divider 12 bits
        self.reference_counter = 25	# divide main reference (25 MHz) to give phase detector frequency of 1MHz
        self.powerdown = '0' 		# Power the chip down 1 
        self.auxRFEnabled = '0' 	# Aux output off 0  
        self.mainRFEnabled = '0' 	# Main RF out 0 = off  
        self.feedbackType = '1' 	# feedback direct from VCO to N Divider (1) or via output divider (0) 
        self.prescaler = '0' 		# Output prescaler 4/5 if VCO >3.6GHz must be set to 8/9 1 
        self.ABP = '0' 			# antibacklash pulse width 6ns for Fractional N mode 
        self.ref_doubler = '0'		# Reference doubler to extend range of Phase detector active 1  
        self.ref_halve = '0' 		# reference halve active 1  
        
        # Port pin assignments 
 
        self.chipEnable = 0 
        self.loadEnable = 0 
        self.dataClock = 0 
        self.serialData = 0 
        self.lockDetect = 0 
        self.multiplexData = 0 
        
      
        # ADF4531 Registers with maps of variables  
        # many are "hard-wired" - see below and ADF4531 datasheet for details - address is 3 Least Significant Bits 
        
        
        self.R0 = ADFReg('R0') 
        
        R0data = [['reserved',1,'0'],  ['integer',16, format(self.integer, '016b')],  ['fraction', 12,  format(self.fraction, '012b')],  ['address', 3,  '000']]
        self.R0.add_data(R0data)
        
        
        # R1 settings  
        # Phase_adj VCO band selection and phase resync with R0 updates (use for fixed freq or narrow band applications only)
        # Prescaler 4/5 or 8/9 
        # phase Output phase can be shifted - disabled for this application	12 bits           
        self.R1 = ADFReg('R1') 
        R1data = [['reserved',3,'000'], ['phase_adj', 1, '0' ],  ['prescaler',  1,  self.prescaler],  ['phase',12, format(self.phase,  '012b')],  ['modulus', 12, format(self.modulus,  '012b')],  ['address', 3,  '001']]
        self.R1.add_data(R1data)
        
        
        # R2 Settings 
        # noise_spur_mode - optimize for low phase noise or best spur reduction 00 for low noise, 11 for low spur 10 and 01 reserved
        # MUX out 000 3 state, 001 DVdd 010 DGnd 011 R counter out 100 N divider out 101 Analog lock detect 110 Digital Lock Detect 111 reserved
        # double_buffer R4 DB22:20 (RF Divider select) 0 disabled 1 enabled 
        # Charge_pump_current with a 5.1K loop filter resistor - set according to loop filter design in this case midrange
        # LDF Lock detect Function - number of PFD cycles for lock 40 for Fractional N (0) 5 cycles for INT PLL (1)
        # Lock detect comparison window Precision LDP 10ns for 0 6ns for 1 reccomend 0 for Fractional N
        # Phase Detector polarity PD_polarity set 1 if noninverting/passive loop filter 0 for inverting active loop filter   
        # power_down set 1 for Software power down - registers retain data and can be written to in this state
        # Charge Pump 3 state CP_3state 0 for normal operation
        # reset_counter if 1 R and N counters are held in reset - 0 for normal operation   
        
        self.R2 = ADFReg('R2') 
        R2data = [['reserved',1,'0'], ['noise_spur_mode',  2,  '11' ], ['mux_out',  3,  '000'], ['ref_doubler',  1,  self.ref_doubler] ,  ['ref_halve',  1,  self.ref_halve], 
        ['reference_counter',10, format(self.reference_counter,  '010b')] , ['double_buffer',  1,  '0'],   ['charge_pump_current', 4,  '1100'], ['LDF',  1,  '0'],  ['LDP',  1,  '0'],  ['PD_polarity',  1,  '1'] ,   
        ['power_down',  1,  '0'],  ['CP_3state',  1,  '0'],  ['reset_counter',  1,  '0'],  ['address', 3,  '010']]
        self.R2.add_data(R2data)
        
        
        # R3 settings
        # band_select_clock_mode set to 1 for fast lock modes
        # Antibacklash pule width ABP 0 for Fractional N modes
        # Charge pump cancel reduces spurs in INT mode 0 for Fractional N 
        # Cycle Slip Reduction CSR 0 for standard operation 
        # Clock Divider Mode clk_div_mode 10 Phase Resync (works in C++ version) 01 fast lock 00 disable clock divider (see datasheet)
        # Clock Divider - timeout counter for Phase resync and fast lock ie NOT reference divider was 1000 in C++ design 
        
        self.R3 = ADFReg('R3') 
        R3data = [['reserved', 8, '00000000'], ['band_select_clock_mode',  1,  '0'],  ['ABP',  1,  self.ABP],  ['charge_cancel',  1,  '0'], ['reserved', 2, '00'], ['CSR',  1,  '0'],  ['reserved',  1,  '0'],  
        ['clk_div_mode', 2,  '10'], ['clock_divider',  12,  '000001000010'],  ['address', 3,  '011']] 
        self.R3.add_data(R3data)
        
        
        # R4 settings  
        # rf_divider value of RF output divider 000 = 1 001 = 2 .... to 110 = 64
        # Band select clock divider - normally taken from R counter out but if this is too high (>125KHz) then need a value here - in this case R out is 1 MHz so use 16
        # VCO_power_down when set to 1 
        # Mute till Lock Detect MTLD - mutes output until lock when set 1 
        # Aux_output_select if 0 is from RF dividers if 1 direct from VCO
        
        self.R4 = ADFReg('R4') 
        R4data = [['reserved',8,'00000000'],  ['feedbackType',1, self.feedbackType], ['rf_divider',3, self.rf_divider], ['band_select_clk_divider', 8,'00001000'], ['VCO_power_down',  1,  '0'],  
        ['MTLD',  1,  '0'],  ['aux_output_select',  1,  '0'],  ['aux_output_enable',  1,  self.auxRFEnabled],  ['aux_output_power',  2,  self.auxPower],  ['output_enable',  1,  self.mainRFEnabled],  
        ['output_power',  2,  self.mainPower],   
        ['address', 3,'100']]
        self.R4.add_data(R4data) 
        
        
        # R5 settings
        # Lock Detect pin mode LD_pin_mode 00 low 01 Digital Lock Detect 10 Low 11 High           
        
        self.R5 = ADFReg('R5') 
        R5data = [['reserved',8,'00000000'],  ['LD_pin_mode',2, '00'],  ['reserved', 19,  '0110000000000000000'],  ['address', 3,  '101']]
        self.R5.add_data(R5data)
        
    def setup_port(self):
        io.setup(self.chipEnable,io.OUT) # make pin into an output   
        io.setup(self.loadEnable,io.OUT) 
        io.setup(self.dataClock,io.OUT) 
        io.setup(self.serialData,io.OUT)      
        
    def write_to_register(self, ADFReg): 
        io.output(self.chipEnable,0)    
        io.output(self.loadEnable,0) 
        io.output(self.dataClock,0) 
        io.output(self.serialData,0)  # Initialize all data lines  
        
        data = ADFReg.register; 
     # Read data out of register MSBit first 
        for i in data:
            if i == '0':
                io.output(self.serialData,0)
            elif i == '1':
                io.output(self.serialData,1)  
            io.output(self.dataClock,1) 
            io.output(self.dataClock,0)
            
        io.output(self.loadEnable,1)
        io.output(self.loadEnable,0)         
        
        io.output(self.chipEnable,1) 
                
        
      # Initialize registers 
    def initialize_registers(self):       
        self.write_to_register(self.R5)
        print ("R5 equals ", self.R5.register)
        self.write_to_register(self.R4)
        print ('R4 equals ', self.R4.register)
        self.write_to_register(self.R3)
        print ("R3 equals ", self.R3.register)
        self.write_to_register(self.R2)
        print ("R2 equals ", self.R2.register)
        self.write_to_register(self.R1)
        print ("R1 equals ", self.R1.register)
        self.write_to_register(self.R0)
        print ("R0 equals ", self.R0.register)
       
     # Update relevant registers after change      
    def update(self): 
        self.R4 = ADFReg('R4_update') 
        R4data = [['reserved',8,'00000000'],  ['feedbackType',1, self.feedbackType], ['rf_divider',3, self.rf_divider], ['band_select_clk_divider', 8,'00001000'], ['VCO_power_down',  1,  '0'],  
        ['MTLD',  1,  '0'],  ['aux_output_select',  1,  '0'],  ['aux_output_enable',  1,  self.auxRFEnabled],  ['aux_output_power',  2,  self.auxPower],  ['output_enable',  1,  self.mainRFEnabled],  
        ['output_power',  2,  self.mainPower],   
        ['address', 3,'100']]
        self.R4.add_data(R4data) 
        self.write_to_register(self.R4)
        print ("R4 equals ", self.R4.register)
        
        self.R1 = ADFReg('R1_update') 
        R1data = [['reserved',3,'000'], ['phase_adj', 1, '0' ],  ['prescaler',  1,  self.prescaler],  ['phase',12, format(self.phase,  '012b')],  ['modulus', 12, format(self.modulus,  '012b')],  ['address', 3,  '001']]
        self.R1.add_data(R1data)
        self.write_to_register(self.R1)
        print ("R1 equals ", self.R1.register)
        
        self.R0 = ADFReg('R0_update') 
        R0data = [['reserved',1,'0'],  ['integer',16, format(self.integer, '016b')],  ['fraction', 12,  format(self.fraction, '012b')],  ['address', 3,  '000']]
        self.R0.add_data(R0data)
        self.write_to_register(self.R0)
        self.write_to_register(self.R0)        
        print ("R0 equals ", self.R0.register)
        
    
    def calculate_freq(self, freq):
        self.output_frequency = freq  	# Frequency in KHz between 32 and 4400 MHz
        output_divider = 0		# output division
        VCO = 0 			# Actual VCO operating frequency KHz  
            
            # Setup output divider
        if freq > 4400000:
            print ("Error frequency Greater than max")            
        elif freq >= 2200000:     
            output_divider = 1
            self.rf_divider = '000' 	# output_divider = 1
        elif freq >= 1100000:  
            self.rf_divider = '001'      # divide output by 2
            output_divider = 2 
        elif freq >= 550000: 
            self.rf_divider = '010'      # divide output by 4
            output_divider = 4  
        elif freq >= 275000: 
            self.rf_divider = '011'	# divide output by 8
            output_divider = 8  
        elif freq >= 137500: 
            self.rf_divider = '100'      # divide output by 16
            output_divider = 16  
        elif freq >= 68750: 
            self.rf_divider = '101'      # divide output by 32
            output_divider = 32 
        elif 34275 < freq & freq <= 68750:  # freq lies between 34.375MHz to 68.75MHz 
            self.rf_divider = '110'
            output_divider = 64
        else:
            print ("Error frequency below minimum")
        
        # Final freq = 1000*(INT + frac/mod)/(output division) KHz 
        # quotient = dividend / divisor 
        # remainder = dividend % divisor
        
        VCO = freq *output_divider 
        self.integer = int(VCO/1000)     # quotient integer part of Fractional N divider 
        self.fraction = int(VCO%1000+31) # remainder fractional part 
                                         # add trim to allow for reference clock error
        # But if fraction > 1000 need to subtract 1000 and add 1 to integer   
        if self.fraction > 999:
            self.fraction = self.fraction-1000
            self.integer = self.integer+1                                 
        
        # If VCO has to go above 3.6GHz prescaler should be set to 8/9 
        if(VCO > 3600000): 
            self.prescaler = '1'  
        
        print ("Output freq is ", freq,  " KHz")
        print ("VCO freq is ",  VCO)
        print ("Integer is ",  self.integer)
        print ("Fraction is ",  self.fraction)
        print ("Modulus is ",  self.modulus)
        print ("RF Divider is ",  output_divider)
    

        
               
    def get_variable(variable): 
        return self.variable 
         
    def set_variable(variable): 
        self.variable = variable
        
        
# end of ADF4531 Class definition     
    
