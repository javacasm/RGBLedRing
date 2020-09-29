import neopixel
import machine
import time

v = '0.8'

N = 60

ledRGB = neopixel.NeoPixel(machine.Pin(18), N)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (100, 100, 100)
GRAY_LIGHT  = (150, 150, 150)
GRAY_DARK   = (50, 50, 50)

def flash(c = WHITE,t = 0.001):
    setColor(c = c)
    time.sleep(t)
    black()
    

def puntoMedio(a,b,paso,pasos):
    c = int(a + (b-a)*paso/pasos)
    return c
        
def fadeIn(c1, c2, t, steps):
    for i in range(0, steps):
        r = puntoMedio(c1[0], c2[0], i, steps)
        g = puntoMedio(c1[1], c2[1], i, steps)
        b = puntoMedio(c1[2], c2[2], i, steps)
        setColor((r, g, b))
        time.sleep(t)

def _setColor(c):
    for i in range(0, N):
        ledRGB[i] = c   

def setColor(c):
     _setColor(c):
    ledRGB.write()


def black():
    setColor(BLACK)

def white():
    setColor(WHITE)

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
