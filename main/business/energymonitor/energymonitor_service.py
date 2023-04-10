import sched

from main.business.energymonitor.logic import MainCommand, Display, DataAdapter


class EnergymonitorService:
    UPDATE_INTERVAL_IN_SECONDS = 2

    def __init__(self, data_adapter: DataAdapter, display: Display, scheduler: sched.scheduler):
        self.scheduler = scheduler
        self.main_command = MainCommand(data_adapter, display)
        self.__running = False

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
            self.event = self.scheduler.enter(self.UPDATE_INTERVAL_IN_SECONDS, 1, self.__periodic, (action, actionargs))
            action(*actionargs)

    def __job(self):
        self.main_command.execute()
