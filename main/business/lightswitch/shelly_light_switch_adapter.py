from ipaddress import IPv4Address
import requests

from main.business.lightswitch.logic import LightSwitchAdapter

class ShellyLightSwitchAdapter(LightSwitchAdapter):

    def __init__(self, ip_adress: str):
        self.ip_adress = ip_adress

    def status(self):
        return requests.get(f'http://{self.ip_adress}/relay/0').json().get('ison', False)

    def on(self):
        requests.get(f'http://{self.ip_adress}/relay/0?turn=on')

    def off(self):
        requests.get(f'http://{self.ip_adress}/relay/0?turn=off')
