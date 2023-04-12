import time
from abc import abstractmethod, ABC

from RPi import GPIO


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


class RaspberryLightswitchAdapter():

    def __init__(self, gpio_pin: GpioPin):
        self.gpio_pin = gpio_pin

    def status(self):
        return False if 0 == self.gpio_pin.status() else True

    def on(self):
        self.gpio_pin.high()

    def off(self):
        self.gpio_pin.low()


class GpioPinImpl(GpioPin):

    def __init__(self, pin: int):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def status(self) -> int:
        pass

    def high(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def low(self):
        GPIO.output(self.pin, GPIO.LOW)




if __name__ == '__main__':
    pin = 18

    gpio_pin = GpioPinImpl(pin)
    gpio_pin.high()
    # gpio = GPIO()
    # gpio.setmode(gpio.BOARD)
    # gpio.setup(pin, gpio.OUT)
    #
    # gpio.output(pin, gpio.HIGH)
    # if (0 == gpio.input(pin)):
    #     print('off')
    # if (1 == gpio.input(pin)):
    #     print('on')

    time.sleep(5.0)

    gpio_pin.low()
    # gpio.output(pin, gpio.LOW)
    # if (0 == gpio.input(pin)):
    #     print('off')
    # if (1 == gpio.input(pin)):
    #     print('on')
