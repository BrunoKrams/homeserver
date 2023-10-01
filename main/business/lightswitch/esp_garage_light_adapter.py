from main.business.lightswitch.logic import LightSwitchAdapter
import requests

class EspGarageLightSwitchAdapter(LightSwitchAdapter):

    BASE_URL = "http://garagenlampe"

    def status(self):
        response_status = requests.get(self.BASE_URL + "/status").text
        print(response_status)
        return True if response_status == '1' else False

    def on(self):
        requests.post(self.BASE_URL + "/on")

    def off(self):
        requests.post(self.BASE_URL + "/off")



