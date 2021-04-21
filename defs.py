import array
from ola.ClientWrapper import ClientWrapper
from time import sleep
import datetime

#Start with an empty array for references
data = array.array('B', )

#User Settable Parameters
intensity = 255
hourr = 200
hourg = 190
hourb = 180

mintenr = 170
minteng = 160
mintenb = 150

minunitr = 140
minunitg = 130
minunitb = 120
  
print("Running")


#HourDefinitions
def hour1():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour2():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour3():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour4():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour5():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour6():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour7():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour8():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour9():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour10():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour11():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
def hour12():
	data.extend([hourr, hourg, hourb, hourr, hourg, hourb, 0,0,0, hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,hourr, hourg, hourb, hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,hourr, hourg, hourb,hourr, hourg, hourb,0,0,0,0,0,0,0,0,0,0,0,0])

#Minute pixels to add to the array
min00pixels = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
min10pixels = mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
min20pixels = mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
min30pixels = mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
min40pixels = mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
min50pixels = mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,0,0,0,0,0,0,0,0,0,mintenr, minteng, mintenb,mintenr, minteng, mintenb,0,0,0,0,0,0,0,0,0,0,0,0

min0pixels = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0    
min1pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0    
min2pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0    
min3pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
min4pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
min5pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0    
min6pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0    
min7pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0    
min8pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0    
min9pixels = minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0,0,0,0,0,0,0,minunitr, minunitg, minunitb,minunitr, minunitg, minunitb,0,0,0,0,0,0    


#Minute definitions
def min0():
    data.extend(min00pixels + min0pixels)
def min1():
    data.extend(min00pixels + min1pixels)
def min2():
    data.extend(min00pixels + min2pixels)
def min3():
    data.extend(min00pixels + min3pixels)
def min4():
    data.extend(min00pixels + min4pixels)
def min5():
    data.extend(min00pixels + min5pixels)
def min6():
    data.extend(min00pixels + min6pixels)
def min7():
    data.extend(min00pixels + min7pixels)
def min8():
    data.extend(min00pixels + min8pixels)
def min9():
    data.extend(min00pixels + min9pixels)
def min10():
    data.extend(min10pixels + min0pixels)
def min11():
    data.extend(min10pixels + min1pixels)
def min12():
    data.extend(min10pixels + min2pixels)
def min13():
    data.extend(min10pixels + min3pixels)
def min14():
    data.extend(min10pixels + min4pixels)
def min15():
    data.extend(min10pixels + min5pixels)
def min16():
    data.extend(min10pixels + min6pixels)
def min17():
    data.extend(min10pixels + min7pixels)
def min18():
    data.extend(min10pixels + min8pixels)
def min19():
    data.extend(min10pixels + min9pixels)
def min20():
    data.extend(min20pixels + min0pixels)
def min21():
    data.extend(min20pixels + min1pixels)
def min22():
    data.extend(min20pixels + min2pixels)
def min23():
    data.extend(min20pixels + min3pixels)
def min24():
    data.extend(min20pixels + min4pixels)
def min25():
    data.extend(min20pixels + min5pixels)
def min26():
    data.extend(min20pixels + min6pixels)
def min27():
    data.extend(min20pixels + min7pixels)
def min28():
    data.extend(min20pixels + min8pixels)
def min29():
    data.extend(min20pixels + min9pixels)
def min30():
    data.extend(min30pixels + min0pixels)
def min31():
    data.extend(min30pixels + min1pixels)
def min32():
    data.extend(min30pixels + min2pixels)
def min33():
    data.extend(min30pixels + min3pixels)
def min34():
    data.extend(min30pixels + min4pixels)
def min35():
    data.extend(min30pixels + min5pixels)
def min36():
    data.extend(min30pixels + min6pixels)
def min37():
    data.extend(min30pixels + min7pixels)
def min38():
    data.extend(min30pixels + min8pixels)
def min39():
    data.extend(min30pixels + min9pixels)
def min40():
    data.extend(min40pixels + min0pixels)
def min41():
    data.extend(min40pixels + min1pixels)
def min42():
    data.extend(min40pixels + min2pixels)
def min43():
    data.extend(min40pixels + min3pixels)
def min44():
    data.extend(min40pixels + min4pixels)
def min45():
    data.extend(min40pixels + min5pixels)
def min46():
    data.extend(min40pixels + min6pixels)
def min47():
    data.extend(min40pixels + min7pixels)
def min48():
    data.extend(min40pixels + min8pixels)
def min49():
    data.extend(min40pixels + min9pixels)
def min50():
    data.extend(min50pixels + min0pixels)
def min51():
    data.extend(min50pixels + min1pixels)
def min52():
    data.extend(min50pixels + min2pixels)
def min53():
    data.extend(min50pixels + min3pixels)
def min54():
    data.extend(min50pixels + min4pixels)
def min55():
    data.extend(min50pixels + min5pixels)
def min56():
    data.extend(min50pixels + min6pixels)
def min57():
    data.extend(min50pixels + min7pixels)
def min58():
    data.extend(min50pixels + min8pixels)
def min59():
    data.extend(min50pixels + min9pixels)
							

#Time Dictionary

hourvalues = {0: hour12,
              1: hour1,
              2: hour2,
              3: hour3,
              4: hour4,
              5: hour5,
              6: hour6,
              7: hour7,
              8: hour8,
              9: hour9,
              10: hour10,
              11: hour11,
              12: hour12}
minutevalues = {0: min0,
              1: min1,  
              2: min2,
              3: min3,
              4: min4,
              5: min5,
              6: min6,
              7: min7,
              8: min8,
              9: min9,
              10: min10,
              11: min11,
              12: min12,
              13: min13,
              14: min14,
              15: min15,
              16: min16,
              17: min17,
              18: min18,
              19: min19,
              20: min20,
              21: min21,
              22: min22,
              23: min23,
              24: min24,
              25: min25,
              26: min26,
              27: min27,
              28: min28,
              29: min29,
              30: min30,
              31: min31,  
              32: min32,
              33: min33,
              34: min34,
              35: min35,
              36: min36,
              37: min37,
              38: min38,
              39: min39,
              40: min40,
              41: min41,
              42: min42,
              43: min43,
              44: min44,
              45: min45,
              46: min46,
              47: min47,
              48: min48,
              49: min49,
              50: min50,
              51: min51,
              52: min52,
              53: min53,
              54: min54,
              55: min55,
              56: min56,
              57: min57,
              58: min58,
              59: min59
                }




