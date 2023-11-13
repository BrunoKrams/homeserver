import sched
import time

from main.business.energymonitor.command_line_display import CommandLineDisplay
from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.print.print_service import PrintService
from main.business.energymonitor.fritzbox_adapter import FritzboxAdapter
from main.business.lightswitch.lightswitch_service import LightSwitchService
from main.business.lightswitch.mock_light_switch_adapter import MockLightSwitchAdapter
from main.business.print.cups_print_adapter import CupsPrintAdapter
from main.web.server import Server

from waitress import serve

ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND = 2
def create_kitchen_light_service() -> LightSwitchService:
    return LightSwitchService(MockLightSwitchAdapter())

def create_energymonitor_service() -> EnergymonitorService:
    scheduler = sched.scheduler(time.time, time.sleep)
    return EnergymonitorService(FritzboxAdapter(), CommandLineDisplay(), scheduler, ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND)

def create_print_service() -> PrintService:
    return PrintService(CupsPrintAdapter())

if __name__ == '__main__':
    kitchen_light_service = create_kitchen_light_service()
    energymonitor_service = create_energymonitor_service()
    print_service = create_print_service()

    server = Server(kitchen_light_service, energymonitor_service, print_service)
    serve(server.app, host='0.0.0.0', port=5000)