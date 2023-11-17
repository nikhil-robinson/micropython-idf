from micropython import const
from machine import Pin, SoftI2C, PWM, ADC, TouchPad
import neopixel
from apds.const import *
from apds.device import uAPDS9960 as APDS9960
from ip5306 import IP5306
from machine import Pin, I2C
import ssd1306

# PLAYCOMPUTER Hardware Pin Assignments

#PORTS
PORT_A1 = const(1)
PORT_A2 = const(2)
PORT_B1 = const(4)
PORT_B2 = const(5)
PORT_C1 = const(6)
PORT_C2 = const(7)
PORT_D1 = const(8)
PORT_D2 = const(9)
PORT_E1 = const(17)
PORT_E2 = const(14)
PORT_F1 = const(15)
PORT_F2 = const(16)

#SMILE LED
PORT_L1 = const(37)
PORT_L2 = const(41)
PORT_L3 = const(21)
PORT_L4 = const(35)

#RGB_PIN LED
RGB_PIN= const(36)
RGB_IND= const(46)

#TOUCHPADS
PORT_T1 = const(10)
PORT_T2 = const(11)
PORT_T3 = const(13)
PORT_T4 = const(12)

#MIC_PIN PIN
MIC_PIN = const(18)

#TEMP_PINURATURE
TEMP_PIN = const(3)

#BUZZER
BEEPER_PIN = const(45)

BOOT_PIN = const(0)



#I2C
bus = None

#helper functions

#RGB_PIN leds
class rgb_led:
    def __init__(self):
        p = Pin(RGB_PIN)
        self.strip = neopixel.NeoPixel(p, 12)
    def set_pixels(self,num,red =0,green=0,blue=0):
        self.strip[num-1] =(red,blue,green)
    def update_pixels(self):
        self.strip.write()

#smile leds
class smile_led:
    def on(num):
        sl_arr =[38,40,21,35]
        p = Pin(sl_arr[num-1], Pin.OUT)
        p.value(1)
    def off(num):
        sl_arr =[38,40,21,35]
        p = Pin(sl_arr[num-1], Pin.OUT)
        p.value(0)



class OLED():
    def __init__(self):
        "Class for SSD1306 OLED"
        self.i2c = SoftI2C(scl=Pin(PORT_D1),sda=Pin(PORT_D2))
        self.display = ssd1306.SSD1306_I2C(128, 64, self.i2c)

    def set_text(self,text,line):
        self.display.text(text,0,0,line)
    
    def show(self):
        self.display.show()
    
    def get_handel(self):
        return self.display


class QMI8658(object):
    def __init__(self,address=0X6A):
        self._address = address
        self._bus = SoftI2C(scl=Pin(PORT_D1),sda=Pin(PORT_D2))
        bRet=self.WhoAmI()
        if bRet :
            self.Read_Revision()
        else:
            return None
        self.Config_apply()

    def _read_byte(self,cmd):
        rec=self._bus.readfrom_mem(int(self._address),int(cmd),1)
        return rec[0]
    def _read_block(self, reg, length=1):
        rec=self._bus.readfrom_mem(int(self._address),int(reg),length)
        return rec
    def _read_u16(self,cmd):
        LSB = self._bus.readfrom_mem(int(self._address),int(cmd),1)
        MSB = self._bus.readfrom_mem(int(self._address),int(cmd)+1,1)
        return (MSB[0] << 8) + LSB[0]
    def _write_byte(self,cmd,val):
        self._bus.writeto_mem(int(self._address),int(cmd),bytes([int(val)]))
        
    def WhoAmI(self):
        bRet=False
        if (0x05) == self._read_byte(0x00):
            bRet = True
        return bRet
    def Read_Revision(self):
        return self._read_byte(0x01)
    def Config_apply(self):
        # REG CTRL1
        self._write_byte(0x02,0x60)
        # REG CTRL2 : QMI8658AccRange_8g  and QMI8658AccOdr_1000Hz
        self._write_byte(0x03,0x23)
        # REG CTRL3 : QMI8658GyrRange_512dps and QMI8658GyrOdr_1000Hz
        self._write_byte(0x04,0x53)
        # REG CTRL4 : No
        self._write_byte(0x05,0x00)
        # REG CTRL5 : Enable Gyroscope And Accelerometer Low-Pass Filter 
        self._write_byte(0x06,0x11)
        # REG CTRL6 : Disables Motion on Demand.
        self._write_byte(0x07,0x00)
        # REG CTRL7 : Enable Gyroscope And Accelerometer
        self._write_byte(0x08,0x03)

    def Read_Raw_XYZ(self):
        xyz=[0,0,0,0,0,0]
        raw_timestamp = self._read_block(0x30,3)
        raw_acc_xyz=self._read_block(0x35,6)
        raw_gyro_xyz=self._read_block(0x3b,6)
        raw_xyz=self._read_block(0x35,12)
        timestamp = (raw_timestamp[2]<<16)|(raw_timestamp[1]<<8)|(raw_timestamp[0])
        for i in range(6):
            # xyz[i]=(raw_acc_xyz[(i*2)+1]<<8)|(raw_acc_xyz[i*2])
            # xyz[i+3]=(raw_gyro_xyz[((i+3)*2)+1]<<8)|(raw_gyro_xyz[(i+3)*2])
            xyz[i] = (raw_xyz[(i*2)+1]<<8)|(raw_xyz[i*2])
            if xyz[i] >= 32767:
                xyz[i] = xyz[i]-65535
        return xyz
    def Read_XYZ(self):
        xyz=[0,0,0,0,0,0]
        raw_xyz=self.Read_Raw_XYZ()  
        #QMI8658AccRange_8g
        acc_lsb_div=(1<<12)
        #QMI8658GyrRange_512dps
        gyro_lsb_div = 64
        for i in range(3):
            xyz[i]=raw_xyz[i]/acc_lsb_div#(acc_lsb_div/1000.0)
            xyz[i+3]=raw_xyz[i+3]*1.0/gyro_lsb_div
        return xyz


#APDS
class APDS:
    "CLASS FOR APDS9960"
    dirs = {APDS9960_DIR_NONE: "none",APDS9960_DIR_LEFT: "right",APDS9960_DIR_RIGHT: "left",APDS9960_DIR_UP: "down",APDS9960_DIR_DOWN: "up",APDS9960_DIR_NEAR: "near",APDS9960_DIR_FAR: "far"}
    def __init__(self):
        self._bus = SoftI2C(scl=Pin(PORT_D1),sda=Pin(PORT_D2))
        self.apds = APDS9960(self._bus)

    "ENABLE LIGHT SENSOR"
    def enable_light_sensor(self):
        self.apds.enableLightSensor()

    "ENABLE color SENSOR"
    def enable_color_sensor(self):
        self.apds.enableLightSensor()
    
    "ENABLE PROXIMITY SENSOR"
    def enable_proximity_sensor(self,thres = 50):
        self.apds.setProximityIntLowThreshold(thres)
        self.apds.enableProximitySensor()
    
    "ENABLE GESTURE SENSOR"
    def enable_gesture_sensor(self,thres=50):
        self.apds.setProximityIntLowThreshold(thres)
        self.apds.enableGestureSensor()

    "READ LIGHT"
    def read_light(self):
        return self.apds.readAmbientLight()

    "READ color"
    def read_color(self):
        return self.apds.readRedLight(),self.apds.readGreenLight(),self.apds.readBlueLight()

    "READ PROXIMITY"
    def read_proximity(self):
        return self.apds.readProximity()
    
    "READ GESTURE"
    def read_gesture(self):
        if self.apds.isGestureAvailable():
            return self.dirs.get(self.apds.readGesture(), "unknown")



class buzzer:
    global bp
    global bb
    def start(duty = 50):
        buzzer.bp = Pin(BEEPER_PIN,Pin.OUT)
        buzzer.bb= PWM(buzzer.bp)
        buzzer.bb.duty(duty)
    def set_freq(f):
        buzzer.bb.freq(1047)
    def stop():
        buzzer.bb.deinit()

class temperature_sensor:
    def read():
        p = ADC(Pin(TEMP_PIN))
        p.atten(ADC.ATTN_11DB)       #Full range: 3.3v
        return p.read()
class mic:
    def read():
        p = ADC(Pin(MIC_PIN))
        p.atten(ADC.ATTN_11DB)       #Full range: 3.3v
        return p.read()

class battery:
    def get_level():
        ip5306 = IP5306(bus)
        return ip5306.level


class TOUCHPAD:
    def read_t0():
        t = TouchPad(Pin(PORT_T1))
        return t.read()
    def read_t1():
        t = TouchPad(Pin(PORT_T2))
        return t.read()
    def read_t2():
        t = TouchPad(Pin(PORT_T3))
        return t.read()
    def read_t3():
        t = TouchPad(Pin(PORT_T4))
        return t.read()