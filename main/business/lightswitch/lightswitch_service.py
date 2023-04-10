class LightswitchService:

    def __init__(self):
        self.is_on = self.status()

    def status(self) -> bool:
        return self.is_on

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False
