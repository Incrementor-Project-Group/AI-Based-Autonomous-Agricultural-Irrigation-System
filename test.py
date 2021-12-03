import RPI.GPIO as GPIO
import gpiozero
import gpio
from gpiozero.pins.pigpio import PiGPIOFactory

# gpio_factory = PiGPIOFactory(host='192.168.2.203')

# Read value from gpio pin 17
print(gpio.read(17))

import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(17, GPIO.OUT)           # set GPIO24 as an output   
  
try:  
    while True:  
        GPIO.output(17, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.5)                 # wait half a second  
        GPIO.output(17, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(0.5)                 # wait half a second  
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  
