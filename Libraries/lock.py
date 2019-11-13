def lock(bool state):
    import RPi.GPIO as GPIO
    import time

    #GPIO setup
    GPIO.setmode(GPIO.BCM)
    control_pins = [40,38,36,35]
    powerPin = 37

    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    GPIO.setup(powerPin, GPIO.OUT)
    GPIO.output(powerPin,)
    
    if state == True:
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
    else:
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

    
    #setup direction variable based on state

    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)
    GPIO.cleanup()