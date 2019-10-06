import RPi.GPIO as GPIO
import time

servoPINs = [17]
# , 18, 22]
dutyCycles = []
pins = []
GPIO.setmode(GPIO.BCM)

for i in range(0, len(servoPINs)):
    GPIO.setup(servoPINs[i], GPIO.OUT)
    dutyCycles.append(2.5)
    pins.append(GPIO.PWM(servoPINs[i], 50))
    pins[i].start(dutyCycles[i])

try:
    while True:

        for i in range(0, len(servoPINs)):
            currentPin = pins[i]

            currentPin.ChangeDutyCycle(dutyCycles[i])
            time.sleep(0.01)

            dutyCycles[i] += 0.05

            if dutyCycles[i] >= 12.5:
                time.sleep(1.5)
                dutyCycles[i] = 2.5
                pins[i].ChangeDutyCycle(dutyCycles[i])
                time.sleep(1.5)

except KeyboardInterrupt:
    for i in range(0, len(servoPINs)):
        pins[i].stop()

    GPIO.cleanup()