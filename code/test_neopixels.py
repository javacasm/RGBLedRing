import neopixel
import machine
import time

v = '0.8'


def test_RGB():
    r = 0
    g = 40
    b = 20

    while True:
        r = (r + 1) % N
        g = (g + 1) % N
        b = (b + 1) % N
        ledRGB[r] = (50,0,0)
        ledRGB[b] = (0,0,50)
        ledRGB[g] = (0,50,0)
        ledRGB.write()
        time.sleep(0.02)
        ledRGB[r] = (0,0,0)
        ledRGB[b] = (0,0,0)
        ledRGB[g] = (0,0,0)        

def test_ciclo():
    for i in range(0, N):
        print(i)
        ledRGB[i] = (50,0,0)
        ledRGB.write()
        time.sleep(0.1) 
        ledRGB[i] = (0,0,0)
