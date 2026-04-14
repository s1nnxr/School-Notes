from machine import Pin, PWM
from time import sleep

# Motor pin (GPIO2)
motor_pin = Pin(2)

# Create PWM object
motor = PWM(motor_pin, freq=5000)

while True:
    
    # Increase speed
    for duty in range(0, 1024, 20):
        motor.duty(duty)
        sleep(0.02)
    
    sleep(1)
    
    # Decrease speed
    for duty in range(1023, -1, -20):
        motor.duty(duty)
        sleep(0.02)
    
    sleep(1)
    
# ESP32 GPIO2 → 220Ω → transistor base
# transistor collector → motor
# motor other side → +5V
# transistor emitter → GND
# diode across motor

