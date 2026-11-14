try:
    import RPi.GPIO as GPIO
except ImportError:
    # Mock for testing on non-Pi environments (like your PC)
    import Mock.GPIO as GPIO

class MotorDriver:
    def __init__(self, left_pin=17, right_pin=18):
        self.left_pin = left_pin
        self.right_pin = right_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_pin, GPIO.OUT)
        GPIO.setup(self.right_pin, GPIO.OUT)

    def move_forward(self, speed=50):
        GPIO.output(self.left_pin, GPIO.HIGH)
        GPIO.output(self.right_pin, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.left_pin, GPIO.LOW)
        GPIO.output(self.right_pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()
