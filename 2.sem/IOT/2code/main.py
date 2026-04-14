import machine
import utime
from lcd_I2C import I2CLcd

i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

i2c_addresses = i2c.scan()
if not i2c_addresses:
    print("No I2C devices found!")
    while True:
        pass

lcd_address = i2c_addresses[0]
lcd = I2CLcd(i2c, lcd_address)

red = machine.Pin(2, machine.Pin.OUT)
yellow = machine.Pin(4, machine.Pin.OUT)
green = machine.Pin(5, machine.Pin.OUT)

def all_off():
    red.value(0)
    yellow.value(0)
    green.value(0)

lcd.move_to(0, 0)
lcd.putstr("Traffic Light")
lcd.move_to(0, 1)
lcd.putstr("Starting...")
utime.sleep(2)
lcd.clear()

while True:

    all_off()
    red.value(1)
    lcd.move_to(0, 0)
    lcd.putstr("RED LIGHT")
    lcd.move_to(0, 1)
    lcd.putstr("STOP")
    utime.sleep(5)
    lcd.clear()

    all_off()
    yellow.value(1)
    red.value(1)
    lcd.move_to(0, 0)
    lcd.putstr("+ YELLOW LIGHT")
    lcd.move_to(0, 1)
    lcd.putstr("PREPARE")
    utime.sleep(5)
    lcd.clear()

    all_off()
    green.value(1)
    lcd.move_to(0, 0)
    lcd.putstr("GREEN LIGHT")
    lcd.move_to(0, 1)
    lcd.putstr("GO")
    utime.sleep(0.2)
    lcd.clear()

