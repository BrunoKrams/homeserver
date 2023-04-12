import time
from abc import abstractmethod, ABC

import RPi.GPIO as GPIO


class GpioPin(ABC):

    @abstractmethod
    def status(self) -> int:
        pass

    @abstractmethod
    def high(self):
        pass

    @abstractmethod
    def low(self):
        pass


class GpioPinImpl(GpioPin):

    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def status(self) -> int:
        return GPIO.input(self.pin)

    def high(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def low(self):
        GPIO.output(self.pin, GPIO.LOW)

class RaspberryLightswitchAdapter():

    def __init__(self, gpio_pin: GpioPin):
        self.gpio_pin = gpio_pin

    def status(self):
        return False if 0 == self.gpio_pin.status() else True

    def on(self):
        self.gpio_pin.high()

    def off(self):
        self.gpio_pin.low()

if __name__ == '__main__':
    gpio_pin = GpioPinImpl(18)
    lightswitch_adapter = RaspberryLightswitchAdapter(gpio_pin)
    lightswitch_adapter.on()
    print('ON' if lightswitch_adapter.status() else "OFF")
    time.sleep(4)
    lightswitch_adapter.off()
    print('ON' if lightswitch_adapter.status() else "OFF")
