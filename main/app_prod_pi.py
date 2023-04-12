import sched
import time

import RPi.GPIO as GPIO
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.energymonitor.fritzbox_adapter import FritzboxAdapter
from main.business.energymonitor.matrix_display import MatrixDisplay
from main.business.lightswitch.lightswitch_service import LightswitchService
from main.business.lightswitch.raspberry_lightswitch_adapter import RaspberryLightswitchAdapter, GpioPin
from main.web.server import Server

LIGHTSWITCH_GPIO_PIN = 18
ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND = 60

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


def create_lightswitch_service() -> LightswitchService:
    gpio_pin = GpioPinImpl(LIGHTSWITCH_GPIO_PIN)
    lightswitch_adapter = RaspberryLightswitchAdapter(gpio_pin)
    return LightswitchService(lightswitch_adapter)

def create_energymonitor_service() -> EnergymonitorService:
    scheduler = sched.scheduler(time.time, time.sleep)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)
    return EnergymonitorService(FritzboxAdapter(), MatrixDisplay(device), scheduler, ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND)


if __name__ == '__main__':
    lightswitch_service = create_lightswitch_service()
    energymonitor_service = create_energymonitor_service()

    server = Server(lightswitch_service, energymonitor_service)
    server.run(host="192.168.178.51")
