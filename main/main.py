from flask import Flask

from business.energymonitor.energy_monitor_service import EnergymonitorService
from business.lightswitch.lightswitch_service import LightswitchService

server = Flask(__name__, static_url_path='', static_folder='web')

lightswitch_service = LightswitchService()
energy_monitor_service = EnergymonitorService()

@server.route("/")
def index():
    return server.send_static_file("index.html")

@server.route("/lightswitch")
def lightswitch_status():
    is_on = lightswitch_service.status()
    return 'ON' if is_on else 'OFF', 200

@server.route("/lightswitch/on", methods=['POST'])
def lightswitch_switch_on():
    lightswitch_service.on()

@server.route("/lightswitch/off", methods=['POST'])
def lightswitch_switch_off():
    lightswitch_service.off()

@server.route("/energymonitor/start", methods=['POST'])
def energy_monitor_start():
    energy_monitor_service.start()

@server.route("/energymonitor/stop", methods=['POST'])
def energy_monitor_stop():
    energy_monitor_service.stop()

server.run()
