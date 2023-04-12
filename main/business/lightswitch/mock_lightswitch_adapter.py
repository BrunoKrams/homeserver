from main.business.lightswitch.logic import LightswitchAdapter


class MockLightswitchAdapter(LightswitchAdapter):

    def status(self):
        print("status called")
        return True

    def on(self):
        print("on called")

    def off(self):
        print("off called")