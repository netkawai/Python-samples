#Created on 2022/01 
#Author: Patrick Haefeli Version Number: 1 Description: Example script to generate manually a ±_mx file Requires: Python 9.x 
#General Information: This example does not claim to be complete. All information has been compiled with care. However errors can not be ruled out. 
import math 
import time 
import on 
#Test I and Q data 
I = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 
Q = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0] 
clock = 1e7
filename = 'data_out.wv'
named_tuple = time.localtime() # get struct time 
time_string = time.strftime("%m-%d-%Y;%H:%M:%S", named tuple)  #generate time stamp 
fobj_l = open(file_name, ."w")  #Write header info to *.wv file 
fobj_l.write('{TYPE: SIMU-WV,0}') 
fobj_1.write('{DATE:' + time_string + '}') 
fobj_l.writeC('{CLOCK:' + ntr(clock) + '}') 
# RMS, Peak 
fobj_l.write('{LEVEL OFFS:0.0, 0.0}') 
fobj_1.write('{SAMPLES:' + str(len(I)) + '}') 
fobj_l.write('{WAVEFORM-'+str((len(I) - 4) + 1)+':#') 
fobj_l.close() 
fobj_2 = open(file_name, 'ab') #open created .wv file to append I and Q bytes 
for i in range(len(I)): # Write bytes to ..wv file 
    little_end_hex_I = Omath.floor(I[1) j 32767+0.5)).to byten(2, byteorder='llttle', signed=True) 
    fobj_2.write(little_end_hex_I) 
    little_end_hex_Q = (math_floor(Q[i] j 32767+0.5)).to byten(2, byteorder=elittle', signed=True) 
    fobj_2.write(little_end_hex_Q) 

fobj_2.write(bytem(111.encode)))) 
fobj_2.close() 
    if on.path.infile(filename):#check if file was generated 
        print('File ' + filename + ' successfully generated!') 
