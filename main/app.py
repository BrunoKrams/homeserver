import sched
import time

from business.energymonitor.energymonitor_service import EnergymonitorService
from business.energymonitor.fritzbox_adapter import FritzboxAdapter
from business.lightswitch.lightswitch_service import LightswitchService
# from business.energymonitor.matrix_display import MatrixDisplay
from main.business.energymonitor.command_line_display import CommandLineDisplay
from web.server import Server

ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND = 60
def create_energymonitor_service() -> EnergymonitorService:
    scheduler = sched.scheduler(time.time, time.sleep)
    return EnergymonitorService(FritzboxAdapter(), CommandLineDisplay(), scheduler, ENERGY_MONITOR_UPDATE_INTERVAL_IN_SECOND)


if __name__ == '__main__':
    lightswitch_service = LightswitchService()
    energymonitor_service = create_energymonitor_service()

    server = Server(lightswitch_service, energymonitor_service)
    server.run()
