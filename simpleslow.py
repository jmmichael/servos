#youtube.com/watch?v=ddlDgUymbxc Gaven MacDonald 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)

try:
	while True:
		p.ChangeDutyCycle(7.5)#neutral
		time.sleep(1)
		p.ChangeDutyCycle(8.0)#neutral
		time.sleep(1)
		p.ChangeDutyCycle(8.5)#neutral
		time.sleep(1)
		p.ChangeDutyCycle(9.0)#neutral
		time.sleep(1)
		p.ChangeDutyCycle(9.5)#neutral
		time.sleep(1)
		p.ChangeDutyCycle(10.0)#neutral
		time.sleep(1)
		p.ChangeDutyCycle(10.5)#neutral
		time.sleep(1)
		p.ChangeDutyCycle(11.5)#neutral
		time.sleep(1)
		p.ChangeDutyCycle(12.5)#180deg
		time.sleep(1)
		p.ChangeDutyCycle(2.5)#0deg
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
