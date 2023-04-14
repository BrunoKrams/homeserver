import sched
import time

from main.business.energymonitor.command_line_display import CommandLineDisplay
from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.energymonitor.fritzbox_adapter import FritzboxAdapter
from main.business.lightswitch.lightswitch_service import LightswitchService
from main.business.lightswitch.mock_lightswitch_adapter import MockLightswitchAdapter
from main.web.server import Server

from waitress import serve

ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND = 2

def create_lightswitch_service() -> LightswitchService:
    return LightswitchService(MockLightswitchAdapter())

def create_energymonitor_service() -> EnergymonitorService:
    scheduler = sched.scheduler(time.time, time.sleep)
    return EnergymonitorService(FritzboxAdapter(), CommandLineDisplay(), scheduler, ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND)


if __name__ == '__main__':
    lightswitch_service = create_lightswitch_service()
    energymonitor_service = create_energymonitor_service()

    server = Server(lightswitch_service, energymonitor_service)
    serve(server.app, host='0.0.0.0', port=5000)