
from time import sleep

from machine import Pin, I2C

from apds.const import *
from apds.device import uAPDS9960 as APDS9960

bus = I2C(sda=Pin(13), scl=Pin(14))

apds = APDS9960(bus)

print("Light Sensor Test")
print("=================")
apds.enableLightSensor()

oval = -1
while True:
    sleep(0.25)
    val = apds.readAmbientLight()
    if val != oval:
        print("AmbientLight={}".format(val))
        oval = val