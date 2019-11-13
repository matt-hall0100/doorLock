import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 40 # coil 1
coil_A_2_pin = 38 # coil 2
coil_B_1_pin = 36 # coil 3
coil_B_2_pin = 35 # coil 4
powerPin = 37 # supply power to stepper controler
 
# adjust if different
StepCount = 8
Seq = range(0, StepCount)
Seq[0] = [1,0,0,0]
Seq[1] = [1,1,0,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,1,1,0]
Seq[4] = [0,0,1,0]
Seq[5] = [0,0,1,1]
Seq[6] = [0,0,0,1]
Seq[7] = [1,0,0,1]
 
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    GPIO.output(powerPin, 1)
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
    GPIO.output(powerPin, 0)
 
def backwards(delay, steps):
    GPIO.output(powerPin, 1)
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
    GPIO.output(powerPin, 0)
 
if __name__ == '__main__':
    while True:
        delay = raw_input("Time Delay (ms)?")
        steps = raw_input("How many steps forward? ")
        forward(int(delay) / 1000.0, int(steps))
        steps = raw_input("How many steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))