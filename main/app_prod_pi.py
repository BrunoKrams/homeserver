import sched
import time

import RPi.GPIO as GPIO
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from waitress import serve

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.energymonitor.fritzbox_adapter import FritzboxAdapter
from main.business.energymonitor.matrix_display import MatrixDisplay
from main.business.lightswitch.lightswitch_service import LightSwitchService
from main.business.lightswitch.shelly_light_switch_adapter import ShellyLightSwitchAdapter
from main.web.server import Server

ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND = 60
HOMESERVER_IP = '192.168.178.51'
SHELLY_KITCHEN_COUNTER_RELAIS_IP = '192.168.178.105'
SHELLY_KITCHEN_WINDOW_RELAIS_IP='192.168.178.108'
SHELLY_GARAGE_LIGHT_RELAIS_IP='192.168.178.106'


def create_kitchen_light_service() -> LightSwitchService:
    return LightSwitchService(ShellyLightSwitchAdapter(SHELLY_KITCHEN_WINDOW_RELAIS_IP))

def create_kitchen_counter_light_service() -> LightSwitchService:
    return LightSwitchService(ShellyLightSwitchAdapter(SHELLY_KITCHEN_COUNTER_RELAIS_IP))

def create_garage_light_service() -> LightSwitchService:
    return LightSwitchService(ShellyLightSwitchAdapter(SHELLY_GARAGE_LIGHT_RELAIS_IP))


def create_energymonitor_service() -> EnergymonitorService:
    scheduler = sched.scheduler(time.time, time.sleep)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0, blocks_arranged_in_reverse_order=False)
    return EnergymonitorService(FritzboxAdapter(), MatrixDisplay(device), scheduler,
                                ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND)


if __name__ == '__main__':
    GPIO.setwarnings(False)

    kitchen_light_service = create_kitchen_light_service()
    kitchen_counter_light_service = create_kitchen_counter_light_service()
    garage_light_service = create_garage_light_service()
    energymonitor_service = create_energymonitor_service()

    server = Server(kitchen_light_service, kitchen_counter_light_service, garage_light_service, energymonitor_service)
    serve(server.app, host=HOMESERVER_IP, port=5000)
