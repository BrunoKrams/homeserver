import sched

from main.business.energymonitor.logic import DataAdapter, Display


class EnergymonitorService:

    def __init__(self, data_adapter: DataAdapter, display: Display, scheduler: sched.scheduler, update_interval_in_seconds: int):
        self.data_adapter = data_adapter
        self.display = display
        self.scheduler = scheduler
        self.update_interval_in_seconds = update_interval_in_seconds
        self.__running = False

    def status(self):
        return self.__running

    def start(self):
        print('Energymonitor started')
        if (self.__running == True):
            return
        self.__running = True
        self.__periodic(self.__job)
        self.scheduler.run()

    def stop(self):
        print('Energymonitor stopped')
        self.__running = False
        if self.scheduler and self.event:
            self.scheduler.cancel(self.event)
        self.display.clear()

    def switch(self):
        print('Energymonitor switched')
        if self.__running:
            self.stop()
        else:
            self.start()

    def __periodic(self, action, actionargs=()):
        if self.__running:
            self.event = self.scheduler.enter(self.update_interval_in_seconds, 1, self.__periodic, (action, actionargs))
            action(*actionargs)

    def __job(self):
        enery_in_mw = self.data_adapter.get_energy_in_mw()
        self.display.update(enery_in_mw)

