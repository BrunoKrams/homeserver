from main.business.lightswitch.logic import LightswitchAdapter


class LightswitchService:

    def __init__(self, lightswitch_adapter:LightswitchAdapter):
        self.lightswitch_adapter = lightswitch_adapter

    def status(self) -> bool:
        return self.lightswitch_adapter.status()

    def on(self):
        print('Light on')
        self.lightswitch_adapter.on()

    def off(self):
        print('Light off')
        self.lightswitch_adapter.off()

