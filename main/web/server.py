from flask import Flask, request

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.lightswitch.lightswitch_service import LightSwitchService
from main.business.print.print_service import PrintService

class Server:

    def __init__(self, kitchen_light_service: LightSwitchService, energymonitor_service: EnergymonitorService, print_service: PrintService):
        self.kitchen_light_service = kitchen_light_service
        self.energymonitor_serivce = energymonitor_service
        self.print_service = print_service

        self.app = Flask(__name__, static_url_path='', static_folder='')

        self.app.add_url_rule('/', 'index', self.__index, methods=['GET'])

        self.app.add_url_rule('/kitchenlight', 'kitchen_light_status', self.__kitchen_light_status, methods=['GET'])
        self.app.add_url_rule('/kitchenlight/on', 'kitchen_light_on', self.__kitchen_light_on, methods=['POST'])
        self.app.add_url_rule('/kitchenlight/off', 'kitchen_light_off', self.__kitchen_light_off, methods=['POST'])

        self.app.add_url_rule('/energymonitor', 'energymonitor_status', self.__energymonitor_status, methods=['GET'])
        self.app.add_url_rule('/energymonitor/start', 'energymonitor_start', self.__energymonitor_start, methods=['POST'])
        self.app.add_url_rule('/energymonitor/stop', 'energymonitor_stop', self.__energymonitor_stop, methods=['POST'])

        self.app.add_url_rule('/print', 'print', self.__print, methods=['POST'])

    def __index(self):
        return self.app.send_static_file("index.html")

    def __kitchen_light_status(self):
        status = self.kitchen_light_service.status()
        return 'ON' if status else 'OFF', 200

    def __kitchen_light_on(self):
        self.kitchen_light_service.on()
        return '', 200

    def __kitchen_light_off(self):
        self.kitchen_light_service.off()
        return '', 200

    def __energymonitor_status(self):
        status = self.energymonitor_serivce.status()
        return 'ON' if status else 'OFF', 200

    def __energymonitor_start(self):
        self.energymonitor_serivce.start()
        return '', 200

    def __energymonitor_stop(self):
        self.energymonitor_serivce.stop()
        return '', 200

    def __print(self):
        if len(request.files) != 1:
            return 'Please provide exactly one file', 400

        file = next(iter(request.files.values()))
        if not file.filename.endswith('pdf'):
            return 'Please provide a valid pdf file', 400

        self.print_service.print(file)
        return '', 200

    def run(self, **kwargs):
        self.app.run(**kwargs)

