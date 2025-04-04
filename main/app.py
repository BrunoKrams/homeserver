import sched
import time

from main.business.energymonitor.command_line_display import CommandLineDisplay
from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.energymonitor.fritzbox_adapter import FritzboxAdapter
from main.business.lightswitch.lightswitch_service import LightSwitchService
from main.web.server import Server

ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND = 2

def create_kitchen_light_service() -> LightSwitchService:
    return LightSwitchService(MockLightSwitchAdapter())

def create_energymonitor_service() -> EnergymonitorService:
    scheduler = sched.scheduler(time.time, time.sleep)
    return EnergymonitorService(FritzboxAdapter(), CommandLineDisplay(), scheduler, ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND)


if __name__ == '__main__':
    kitchen_light_service = create_kitchen_light_service()
    energymonitor_service = create_energymonitor_service()

    server = Server(kitchen_light_service, energymonitor_service)
    server.run(host="0.0.0.0")
