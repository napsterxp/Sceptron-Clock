from rpi_ws281x import *
from clockcolours import *

##LED Parameters
LED_COUNT = 288 ##TotalNumber of pixels
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_INVERT = False
LED_CHANNEL = 0
LED_BRIGHTNESS = 255
LED_STRIP = ws.WS2811_STRIP_BGR
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

##Time Shifts
morningshift = '11:59:00'
eveningshift = '12:03:00'
FMT = '%H:%M:%S'

##Definitions
def blockfill (strip, startpixel, endpixel, color):
    for i in range (startpixel, endpixel):
        strip.setPixelColor(i,color)

def singlefill (strip, pixel, color):
    strip.setPixelColor(pixel,color)
    
def clear (strip):
    for i in range (LED_COUNT):
        strip.setPixelColor(i,Color(0,0,0))
#Novelties
def coffee():
    blockfill(strip, 284, 288, Color(coffeer, coffeeg, coffeeb)) #It
    blockfill(strip, 278, 282, Color(coffeer, coffeeg, coffeeb)) #Is
    blockfill(strip, 266, 274, Color(coffeer, coffeeg, coffeeb)) #Time
    blockfill(strip, 42, 48, Color(coffeer, coffeeg, coffeeb)) #For
    blockfill(strip, 28, 40, Color(coffeer, coffeeg, coffeeb)) #Coffee

def pint():
    blockfill(strip, 284, 288, Color(pintr, pintg, pintb)) #It
    blockfill(strip, 278, 282, Color(pintr, pintg, pintb)) #Is
    blockfill(strip, 266, 274, Color(pintr, pintg, pintb)) #Time
    blockfill(strip, 42, 48, Color(pintr, pintg, pintb)) #For
    blockfill(strip, 6, 8, Color(pintr, pintg, pintb)) #A
    blockfill(strip, 10, 18, Color(pintr, pintg, pintb)) #Pint
    
##Time Definitions

def hour0():
    blockfill(strip, 72, 84, Color(hourr, hourg, hourb))
def hour1():
    blockfill(strip, 144, 150, Color(hourr,hourg,hourb))
def hour2():
    blockfill(strip, 150, 156, Color(hourr,hourg,hourb))
def hour3():
    blockfill(strip, 156, 166, Color(hourr,hourg,hourb))
def hour4():
    blockfill(strip, 136, 144, Color(hourr,hourg,hourb))
def hour5():
    blockfill(strip, 170, 178, Color(hourr,hourg,hourb))
def hour6():
    blockfill(strip, 130, 136, Color(hourr,hourg,hourb))
def hour7():
    blockfill(strip, 120, 130, Color(hourr,hourg,hourb))
def hour8():
    blockfill(strip, 96, 106, Color(hourr,hourg,hourb))
def hour9():
    blockfill(strip, 106, 114, Color(hourr,hourg,hourb))
def hour10():
    blockfill(strip, 114, 120, Color(hourr,hourg,hourb))
def hour11():
    blockfill(strip, 84, 96, Color(hourr,hourg,hourb))
def hour12():
    blockfill(strip, 72, 84, Color(hourr,hourg,hourb))
    
def min0():
    blockfill(strip, 284, 288, Color(itr, itg, itb)) #It
    blockfill(strip, 278, 282, Color(itr, itg, itb)) #Is
    blockfill(strip, 48, 60, Color(minr, ming, minb)) #O'Clock
def min5():
    blockfill(strip, 232, 240, Color(minr, ming, minb))
    blockfill(strip, 180, 188, Color(minr, ming, minb)) ##Past
def min10():
    blockfill(strip, 252, 258, Color(minr, ming, minb))
    blockfill(strip, 180, 188, Color(minr, ming, minb)) ##Past
def min15():
    blockfill(strip, 218, 232, Color(minr, ming, minb))
    blockfill(strip, 180, 188, Color(minr, ming, minb)) ##Past
def min20():
    blockfill(strip, 240, 252, Color(minr, ming, minb))
    blockfill(strip, 180, 188, Color(minr, ming, minb)) ##Past
def min25():
    blockfill(strip, 240, 252, Color(minr, ming, minb))
    blockfill(strip, 232, 240, Color(minr, ming, minb))
    blockfill(strip, 180, 188, Color(minr, ming, minb)) ##Past
def min30():
    blockfill(strip, 206, 214, Color(minr, ming, minb))
    blockfill(strip, 180, 188, Color(minr, ming, minb)) ##Past
def min35():
    blockfill(strip, 240, 252, Color(minr, ming, minb))
    blockfill(strip, 232, 240, Color(minr, ming, minb))
    blockfill(strip, 188, 192, Color(minr, ming, minb)) ##To
def min40():
    blockfill(strip, 240, 252, Color(minr, ming, minb))
    blockfill(strip, 188, 192, Color(minr, ming, minb)) ##To
def min45():
    blockfill(strip, 218, 232, Color(minr, ming, minb))
    blockfill(strip, 188, 192, Color(minr, ming, minb)) ##To
def min50():
    blockfill(strip, 252, 258, Color(minr, ming, minb))
    blockfill(strip, 188, 192, Color(minr, ming, minb)) ##To
def min55():
    blockfill(strip, 232, 240, Color(minr, ming, minb))
    blockfill(strip, 188, 192, Color(minr, ming, minb)) ##To
 
##Time Dictionary
hourvalues = {0: hour0,
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
              1: min0,  
              2: min0,
              3: min0,
              4: min0,
              5: min5,
              6: min5,
              7: min5,
              8: min5,
              9: min5,
              10: min10,
              11: min10,
              12: min10,
              13: min10,
              14: min10,
              15: min15,
              16: min15,
              17: min15,
              18: min15,
              19: min15,
              20: min20,
              21: min20,
              22: min20,
              23: min20,
              24: min20,
              25: min25,
              26: min25,
              27: min25,
              28: min25,
              29: min25,
              30: min30,
              31: min30,  
              32: min30,
              33: min30,
              34: min30,
              35: min35,
              36: min35,
              37: min35,
              38: min35,
              39: min35,
              40: min40,
              41: min40,
              42: min40,
              43: min40,
              44: min40,
              45: min45,
              46: min45,
              47: min45,
              48: min45,
              49: min45,
              50: min50,
              51: min50,
              52: min50,
              53: min50,
              54: min50,
              55: min55,
              56: min55,
              57: min55,
              58: min55,
              59: min55
                }
