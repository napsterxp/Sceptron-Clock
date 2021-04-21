import array
from ola.ClientWrapper import ClientWrapper
from time import sleep
import datetime
from defs import *

#Confirms DMX Sent. Breaks without it?!
def DmxSent(status):		
	global wrapper
	if wrapper:
		wrapper.Stop()

universe = 1


##The part that turns the array into a DMX Packet
def run():  
  global wrapper
  wrapper = ClientWrapper()
  client = wrapper.Client()
  client.SendDmx(universe, data, DmxSent)
  wrapper.Run()
 
#The Loop  
while True:
	del data[:] #Deletes previous array to empty DMX Frame
	data.extend([intensity, 0,0,0,0,0,0,]) #Add Intensity then zero out macro channels
	now=datetime.datetime.now()
	hour = ((now.hour)%12)
	minute = now.second
	hourvalues[(hour)]()
	minutevalues[(minute)]()
	run()
	sleep(.3)


print("End")

