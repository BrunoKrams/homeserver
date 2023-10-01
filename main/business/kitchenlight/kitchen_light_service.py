from main.business.kitchenlight.logic import KitchenLightAdapter


class KitchenLightService:

    def __init__(self, kitchen_light_adapter:KitchenLightAdapter):
        self.kitchen_light_adapter = kitchen_light_adapter

    def status(self) -> bool:
        return self.kitchen_light_adapter.status()

    def on(self):
        print('Light on')
        self.kitchen_light_adapter.on()

    def off(self):
        print('Light off')
        self.kitchen_light_adapter.off()

