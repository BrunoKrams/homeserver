from flask import Flask

from main.business.energymonitor.energy_monitor_service import EnergyMonitorService
from main.business.lightswitch.lightswitch_service import LightswitchService


class Server:

    def __init__(self, lightswitch_service: LightswitchService, energy_monitor_service: EnergyMonitorService):
        self.lightswitch_service = lightswitch_service
        self.energy_monitor_serivce = energy_monitor_service

        self.app = Flask(__name__, static_url_path='', static_folder='')

        self.app.add_url_rule('/', 'index', self.__index, methods=['GET'])
        self.app.add_url_rule('/lightswitch/on', 'lightswitch_on', self.__lightswitch_on, methods=['POST'])


    def __index(self):
        return self.app.send_static_file("index.html")

    def __lightswitch_on(self):
        self.lightswitch_service.on()
        return '', 200


    def run(self, **kwargs):
        self.app.run(**kwargs)


if __name__ == "__main__":
    server = Server(LightswitchService(), EnergyMonitorService())
    server.run()
