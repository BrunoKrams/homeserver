from main.business.lightswitch.logic import LightSwitchAdapter


class LightSwitchService:

    def __init__(self, light_switch_adapter:LightSwitchAdapter):
        self.light_switch_adapter = light_switch_adapter

    def status(self) -> bool:
        return self.light_switch_adapter.status()

    def on(self):
        print('Light on')
        self.light_switch_adapter.on()

    def off(self):
        print('Light off')
        self.light_switch_adapter.off()

    def switch(self):
        print('Light switched')
        if self.status():
            self.off()
        else:
            self.on()

