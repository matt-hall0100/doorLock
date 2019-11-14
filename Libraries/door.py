import RPi.GPIO as GPIO
import time

def lock():

    #GPIO setup
    GPIO.setmode(GPIO.BCM)
    control_pins = [40,38,36,35]
    powerPin = 37

    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    GPIO.setup(powerPin, GPIO.OUT)
    GPIO.output(powerPin,1)

    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
        ]

    for i in range(80):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)
    GPIO.cleanup()


def unlock():

    #GPIO setup
    GPIO.setmode(GPIO.BCM)
    control_pins = [40,38,36,35]
    powerPin = 37

    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    GPIO.setup(powerPin, GPIO.OUT)
    GPIO.output(powerPin,1)

    halfstep_seq = [
        [0,0,0,1],
        [0,0,1,1],
        [0,0,1,0],
        [0,1,1,0],
        [0,1,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [1,0,0,1]
        ]

    for i in range(80):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)
    GPIO.cleanup()