import neopixel
import machine
import time

import myNeopixels

v = '0.9.4'


def test_RGB():
    r = 0
    g = 40
    b = 20

    while True:
        r = (r + 1) % myNeopixels.N
        g = (g + 1) % myNeopixels.N
        b = (b + 1) % myNeopixels.N
        myNeopixels.ledRGB[r] = (50,0,0)
        myNeopixels.ledRGB[b] = (0,0,50)
        myNeopixels.ledRGB[g] = (0,50,0)
        myNeopixels.ledRGB.write()
        time.sleep(0.02)
        myNeopixels.ledRGB[r] = (0,0,0)
        myNeopixels.ledRGB[b] = (0,0,0)
        myNeopixels.ledRGB[g] = (0,0,0)        

def test_ciclo():
    for i in range(0, myNeopixels.N):
        print(i)
        myNeopixels.ledRGB[i] = (50,0,0)
        myNeopixels.ledRGB.write()
        time.sleep(0.1) 
        myNeopixels.ledRGB[i] = (0,0,0)


def test_fade():
    myNeopixels.fadeIn(myNeopixels.BLACK, myNeopixels.GRAY, 0.1, 25)                                                                          
    time.sleep(3)
    myNeopixels.black()

def test_trazo():
    for i in range(0, myNeopixels.N):
        myNeopixels.trazo(myNeopixels.BLACK, myNeopixels.ALMOST_BLACK , i)
        time.sleep(0.05)
