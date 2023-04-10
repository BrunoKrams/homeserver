import sched

from main.business.energymonitor.logic import DataAdapter, Display, MainCommand


class EnergymonitorService:

    def __init__(self, data_adapter: DataAdapter, display: Display, scheduler: sched.scheduler, update_interval_in_seconds: int):
        self.scheduler = scheduler
        self.main_command = MainCommand(data_adapter, display)
        self.update_interval_in_seconds = update_interval_in_seconds
        self.__running = False

    def status(self):
        return self.__running

    def start(self):
        self.__running = True
        self.__periodic(self.__job)
        self.scheduler.run()

    def stop(self):
        self.__running = False
        if self.scheduler and self.event:
            self.scheduler.cancel(self.event)

    def __periodic(self, action, actionargs=()):
        if self.__running:
            self.event = self.scheduler.enter(self.update_interval_in_seconds, 1, self.__periodic, (action, actionargs))
            action(*actionargs)

    def __job(self):
        self.main_command.execute()
