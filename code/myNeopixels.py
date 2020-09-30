import neopixel
import machine
import time

v = '0.9.5'

N = 60

ledRGB = neopixel.NeoPixel(machine.Pin(18), N)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (100, 100, 100)
GRAY_LIGHT  = (150, 150, 150)
GRAY_DARK   = (50, 50, 50)
ALMOST_BLACK = (25, 25, 25)

def flash(c = WHITE,t = 0.001):
    setColor(c)
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
    _setColor(c)
    ledRGB.write()

def black():
    setColor(BLACK)

def white():
    setColor(WHITE)

def trazo(c1, c2, pixel):
    for i in range(0,N//2):
        r = puntoMedio(c1[0], c2[0], i, N//2)
        g = puntoMedio(c1[1], c2[1], i, N//2)
        b = puntoMedio(c1[2], c2[2], i, N//2)
        ledRGB[(pixel - i) % N] = (r, g, b)
        ledRGB[(pixel + i) % N] = (r, g, b)
    ledRGB.write()