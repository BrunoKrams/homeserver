from abc import abstractmethod, ABC

from main.business.lightswitch.logic import LightSwitchAdapter


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


class RaspberryKitchenLightAdapter(LightSwitchAdapter):

    def __init__(self, gpio_pin: GpioPin):
        self.gpio_pin = gpio_pin

    def status(self):
        return False if 0 == self.gpio_pin.status() else True

    def on(self):
        self.gpio_pin.high()

    def off(self):
        self.gpio_pin.low()


