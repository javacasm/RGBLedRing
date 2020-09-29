# RGBLedRing

Anillo de iluminación leds RGB, podemos controlarlos desde sus mandos y desde el móvil

![Licencia](./images/Licencia_CC.png)

by @javacasm


## Hardware

* Anillo led con  60 Leds RGBs

    ![60 x RGB Leds](./images/2846-RING60NEOPIXEL_2_main-500x500.jpg)

* Controlado por un ESP32 en una placa Wemos D1 R32 

    ![Wemos D1 R32](./images/wemos-d1-esp32-r32-wroom-32-wifi-y-bluetooth.jpg)

* Joystick Shield de elecfreaks ([Documentación](https://www.elecfreaks.com/blog/post/joystick-shield-quickstart-guide.html) [Ejemplos de elecfreaks](./code/) ) 

    ![Joystick shield de elecfreks](./images/SHD_JK_01.jpg)

## Software

* Programado en micropython
* v0.1 Encendido de leds
* v1.0 Control de color por zonas


## Conexión

### Arduino vs Wemos D1 R32

![](./images/Pinout-Arduino-WemosD1R32.png)
![](./images/Correspondencia-Arduino-WemosD1R32.png)

Cortesía de [Leopoldo Armesto Ángel](https://www.slideshare.net/LeopoldoArmestongel)


```C++

#define PIN_ANALOG_X A0
#define PIN_ANALOG_Y A1

#define X_THRESHOLD_LOW   505
#define X_THRESHOLD_HIGH  515

#define Y_THRESHOLD_LOW   500
#define Y_THRESHOLD_HIGH  510

#ifdef doc_elekfreaks

// https://www.elecfreaks.com/blog/post/joystick-shield-quickstart-guide.html

#define PIN_BUTTON_SELECT  2

#define PIN_BUTTON_B_RIGHT   3
#define PIN_BUTTON_A_UP      4
#define PIN_BUTTON_C_DOWN    5
#define PIN_BUTTON_D_LEFT    6

#else

// https://wiki.keyestudio.com/images/thumb/1/18/KS0153-2.png/800px-KS0153-2.png
// https://cdn.boxtec.ch/pub/elecfreaks/JOYSTICK_SHD_V2.0.pdf  

#define PIN_BUTTON_SELECT    8

#define PIN_BUTTON_B_RIGHT   3
#define PIN_BUTTON_A_UP      2
#define PIN_BUTTON_C_DOWN    4
#define PIN_BUTTON_D_LEFT    5

#define PIN_BUTTON_F         6
#define PIN_BUTTON_E         7


#endif


// E y F 7 y 8

int x_direction = 0;
int y_direction = 0;

void setup_buttons(){

  pinMode(PIN_BUTTON_RIGHT, INPUT_PULLUP);
  pinMode(PIN_BUTTON_LEFT, INPUT_PULLUP);
  pinMode(PIN_BUTTON_UP, INPUT_PULLUP);
  pinMode(PIN_BUTTON_DOWN, INPUT_PULLUP);
  pinMode(PIN_BUTTON_SELECT, INPUT_PULLUP);

}

void test_joystick(){

  int x_position = analogRead(PIN_ANALOG_X);
  intt y_position = analogRead(PIN_ANALOG_Y);

  if (x_position > X_THRESHOLD_HIGH) {
    x_direction = 1;
  } else if (x_position < X_THRESHOLD_LOW) {
    x_direction = -1;
  }

  if (y_position > Y_THRESHOLD_HIGH) {
    y_direction = 1;
  } else if (y_position < Y_THRESHOLD_LOW) {
    y_direction = -1; 
}
```

## micropython

Instalamos el firmware de [micropython v13](https://micropython.org/resources/firmware/esp32-idf3-20200902-v1.13.bin) haciendo

Usamos esptool para instalar el firmare (pip3 install esptool)

Borramos el firmware actual

```sh
esptool.py --port /dev/ttyUSB0 erase_flash
```

Escribimos el firmware de micropython


```sh
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin
```