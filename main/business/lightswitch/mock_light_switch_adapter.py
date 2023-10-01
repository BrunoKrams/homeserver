from main.business.lightswitch.logic import LightSwitchAdapter


class MockLightSwitchAdapter(LightSwitchAdapter):

    def status(self):
        print("status called")
        return True

    def on(self):
        print("on called")

    def off(self):
        print("off called")