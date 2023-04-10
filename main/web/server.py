from flask import Flask

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.lightswitch.lightswitch_service import LightswitchService


class Server:

    def __init__(self, lightswitch_service: LightswitchService, energymonitor_service: EnergymonitorService):
        self.lightswitch_service = lightswitch_service
        self.energymonitor_serivce = energymonitor_service

        self.app = Flask(__name__, static_url_path='', static_folder='')

        self.app.add_url_rule('/', 'index', self.__index, methods=['GET'])

        self.app.add_url_rule('/lightswitch', 'lightswitch_status', self.__lightswitch_status, methods=['GET'])
        self.app.add_url_rule('/lightswitch/on', 'lightswitch_on', self.__lightswitch_on, methods=['POST'])
        self.app.add_url_rule('/lightswitch/off', 'lightswitch_off', self.__lightswitch_off, methods=['POST'])

        self.app.add_url_rule('/energymonitor/start', 'energymonitor_start', self.__energy_monitor_start, methods=['POST'])
        self.app.add_url_rule('/energymonitor/stop', 'energymonitor_stop', self.__energy_monitor_stop, methods=['POST'])

    def __index(self):
        return self.app.send_static_file("index.html")

    def __lightswitch_status(self):
        status = self.lightswitch_service.status()
        return status, 200

    def __lightswitch_on(self):
        self.lightswitch_service.on()
        return '', 200

    def __lightswitch_off(self):
        self.lightswitch_service.off()
        return '', 200

    def __energy_monitor_start(self):
        self.energymonitor_serivce.start()
        return '', 200

    def __energy_monitor_stop(self):
        self.energymonitor_serivce.stop()
        return '', 200

    def run(self, **kwargs):
        self.app.run(**kwargs)

