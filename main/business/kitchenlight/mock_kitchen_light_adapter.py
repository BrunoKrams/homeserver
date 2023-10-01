from main.business.kitchenlight.logic import KitchenLightAdapter


class MockKitchenLightAdapter(KitchenLightAdapter):

    def status(self):
        print("status called")
        return True

    def on(self):
        print("on called")

    def off(self):
        print("off called")