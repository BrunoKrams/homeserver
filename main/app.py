from business.energymonitor.energymonitor_service import EnergymonitorService
from business.lightswitch.lightswitch_service import LightswitchService
from main.business.energymonitor.command_line_display import CommandLineDisplay
from main.business.energymonitor.fritzbox_adapter import FritzboxAdapter
from main.web.server import Server

lightswitch_service = LightswitchService()
energymonitor_service = EnergymonitorService(FritzboxAdapter(), CommandLineDisplay())

server = Server(lightswitch_service, energymonitor_service)

server.run()