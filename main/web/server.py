from flask import Flask, render_template

from main.business.energymonitor.energymonitor_service import EnergymonitorService
from main.business.lightswitch.lightswitch_service import LightSwitchService


class Server:

    def __init__(self, kitchen_light_service: LightSwitchService, kitchen_counter_light_service: LightSwitchService, garage_light_service: LightSwitchService, energymonitor_service: EnergymonitorService):
        self.kitchen_light_service = kitchen_light_service
        self.kitchen_counter_light_service = kitchen_counter_light_service
        self.garage_light_service = garage_light_service
        self.energymonitor_serivce = energymonitor_service

        self.app = Flask(__name__, static_url_path='', template_folder='', static_folder='')

        self.app.add_url_rule('/', 'index', self.__index, methods=['GET'])

        self.app.add_url_rule('/kitchenlight', 'kitchen_light_status', self.__kitchen_light_status, methods=['GET'])
        self.app.add_url_rule('/kitchenlight/on', 'kitchen_light_on', self.__kitchen_light_on, methods=['POST'])
        self.app.add_url_rule('/kitchenlight/off', 'kitchen_light_off', self.__kitchen_light_off, methods=['POST'])    
        
        self.app.add_url_rule('/kitchencounterlight', 'kitchen_counter_light_status', self.__kitchen_counter_light_status, methods=['GET'])
        self.app.add_url_rule('/kitchencounterlight/on', 'kitchen_counter_light_on', self.__kitchen_counter_light_on, methods=['POST'])
        self.app.add_url_rule('/kitchencounterlight/off', 'kitchen_counter_light_off', self.__kitchen_counter_light_off, methods=['POST'])

        self.app.add_url_rule('/garagelight', 'garage_light_status', self.__garage_light_status, methods=['GET'])
        self.app.add_url_rule('/garagelight/on', 'garage_light_on', self.__garage_light_on, methods=['POST'])
        self.app.add_url_rule('/garagelight/off', 'garage_light_off', self.__garage_light_off, methods=['POST'])

        self.app.add_url_rule('/energymonitor', 'energymonitor_status', self.__energymonitor_status, methods=['GET'])
        self.app.add_url_rule('/energymonitor/start', 'energymonitor_start', self.__energymonitor_start, methods=['POST'])
        self.app.add_url_rule('/energymonitor/stop', 'energymonitor_stop', self.__energymonitor_stop, methods=['POST'])

    def __index(self):
        return render_template("index.html")

    def __kitchen_light_status(self):
        status = self.kitchen_light_service.status()
        return 'ON' if status else 'OFF', 200

    def __kitchen_light_on(self):
        self.kitchen_light_service.on()
        return '', 200

    def __kitchen_light_off(self):
        self.kitchen_light_service.off()
        return '', 200

    def __kitchen_counter_light_status(self):
        status = self.kitchen_counter_light_service.status()
        return 'ON' if status else 'OFF', 200

    def __kitchen_counter_light_on(self):
        self.kitchen_counter_light_service.on()
        return '', 200

    def __kitchen_counter_light_off(self):
        self.kitchen_counter_light_service.off()
        return '', 200

    def __garage_light_status(self):
        status = self.garage_light_service.status()
        return 'ON' if status else 'OFF', 200

    def __garage_light_on(self):
        self.garage_light_service.on()
        return '', 200

    def __garage_light_off(self):
        self.garage_light_service.off()
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

    def run(self, **kwargs):
        self.app.run(**kwargs)

