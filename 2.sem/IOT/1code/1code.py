# Přepínačka žárovek
```py
ledPin1 = 2
ledPin2 = 5
ledPin3 = 18
ledPin4 = 16
ledPin5 = 17
ledPin6 = 19
ledPin7 = 21

buttonPin=4
import machine, time
led1 = machine.Pin(ledPin1, machine.Pin.OUT)
led2 = machine.Pin(ledPin2, machine.Pin.OUT)
led3 = machine.Pin(ledPin3, machine.Pin.OUT)
led4 = machine.Pin(ledPin4, machine.Pin.OUT)
led5 = machine.Pin(ledPin5, machine.Pin.OUT)
led6 = machine.Pin(ledPin6, machine.Pin.OUT)
led7 = machine.Pin(ledPin7, machine.Pin.OUT)
button = machine.Pin(buttonPin, machine.Pin.IN,machine.Pin.PULL_UP)

n = 0
while True:
    if button.value() == 0:
        if n == 8: n = 0
        n += 1
        time.sleep(0.3)
        if n == 1:
            led7.value(0)
            led1.value(1)
        elif n == 2:
            led1.value(0)
            led2.value(1)
        elif n == 3:
            led2.value(0)
            led3.value(1)
        elif n == 4:
            led3.value(0)
            led4.value(1)
        elif n == 5:
            led4.value(0)
            led5.value(1)
        elif n == 6:
            led5.value(0)
            led6.value(1)
        elif n == 7:
            led6.value(0)
            led7.value(1)
```
