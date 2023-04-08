from business.energymonitor.energymonitor_service import EnergymonitorService
from business.lightswitch.lightswitch_service import LightswitchService
from main.web.server import Server

lightswitch_service = LightswitchService()
energymonitor_service = EnergymonitorService()

server = Server(lightswitch_service, energymonitor_service)

server.run()