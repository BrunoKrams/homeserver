import sched
import time

from main.business.energymonitor.command_line_display import CommandLineDisplay
from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.energymonitor.fritzbox_adapter import FritzboxAdapter
from main.business.lightswitch.lightswitch_service import LightSwitchService
from main.business.lightswitch.mock_light_switch_adapter import MockLightSwitchAdapter
from main.business.lightswitch.shelly_light_switch_adapter import ShellyLightSwitchAdapter
from main.web.server import Server

from waitress import serve

ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND = 2
SHELLY_KITCHEN_COUNTER_RELAIS_IP='192.168.178.105'
SHELLY_GARAGE_LIGHT_RELAIS_IP='192.168.178.106'

def create_kitchen_light_service() -> LightSwitchService:
    return LightSwitchService(MockLightSwitchAdapter())

def create_kitchen_counter_light_service() -> LightSwitchService:
    return LightSwitchService(ShellyLightSwitchAdapter(SHELLY_KITCHEN_COUNTER_RELAIS_IP))

def create_garage_light_service() -> LightSwitchService:
    return LightSwitchService(ShellyLightSwitchAdapter(SHELLY_GARAGE_LIGHT_RELAIS_IP))


def create_energymonitor_service() -> EnergymonitorService:
    scheduler = sched.scheduler(time.time, time.sleep)
    return EnergymonitorService(FritzboxAdapter(), CommandLineDisplay(), scheduler, ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND)


if __name__ == '__main__':
    kitchen_light_service = create_kitchen_light_service()
    kitchen_counter_light_service = create_kitchen_counter_light_service()
    garage_light_service = create_garage_light_service()
    energymonitor_service = create_energymonitor_service()


    server = Server(kitchen_light_service, kitchen_counter_light_service, garage_light_service, energymonitor_service)
    serve(server.app, host='0.0.0.0', port=5000)